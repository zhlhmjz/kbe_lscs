# -*- coding: utf-8 -*-
import KBEngine
import d_card_dis
import d_task
import random
import types
from KBEDebug import *
from array import *
import copy


class Account(KBEngine.Proxy):


	def __init__(self):
		KBEngine.Proxy.__init__(self)

		"""
		在在线玩家列表注册自己
		"""
		KBEngine.globalData["Halls"].reqAddPlayer(self)

		self.cardSum = 134
		
        # 存放将要使用的卡组
		self.willUseKz = -1
		self.getClientTimeID = 0
		# 存放已经匹配过的次数 在匹配过程中会用
		self.HaveMarchSum = 0

		self.autoAddTask()
		self.battleResult = -1
		self.clientControl = True


		if self.Data["rank"]<1000:
			self.Data["rank"] = 1000

		self.onPlayingBattlefiled = None
		self.onPlayingDestroy = False



		
	def onTimer(self, id, userArg):
		"""
		KBEngine method.
		使用addTimer后， 当时间到达则该接口被调用
		@param id		: addTimer 的返回值ID
		@param userArg	: addTimer 最后一个参数所给入的数据
		"""
		DEBUG_MSG(id, userArg)

		if userArg == 1:
			self.GiveCardList()

		elif userArg == 2:
			self.onGetClient()
	


	def onEntitiesEnabled(self):
		"""
		KBEngine method.
		该entity被正式激活为可使用， 此时entity已经建立了client对应实体， 可以在此创建它的
		cell部分。
		"""
		INFO_MSG("account[%i] entities enable. mailbox:%s" % (self.id, self.client))
		if len(self.Avatar_List) == 0:
			self.randomInitKZ()


	def onLogOnAttempt(self, ip, port, password):
		"""
		KBEngine method.
		客户端登陆失败时会回调到这里
		"""
		INFO_MSG(ip, port, password)
		return KBEngine.LOG_ON_ACCEPT
		
	def onClientDeath(self):
		"""
		KBEngine method.
		客户端对应实体已经销毁
		"""
		DEBUG_MSG("Account[%i].onClientDeath:" % self.id)
		if self.onPlayingBattlefiled == None:
			self.destroy()
		else:
			self.onPlayingDestroy = True

	def reqName(self):
		INFO_MSG("reqName")
		self.client.onName(self.Name)
		
	def reqInf(self):
		INFO_MSG("reqInf")
		self.client.onInf("测试版本，不代表最终品质！~")
	


	def reqCreateName(self,nameset):
		INFO_MSG("ResetName")
		self.Name=nameset
		self.Data['name'] =nameset

	def reqMoney(self):
		INFO_MSG("reqMoney")
		self.client.onMoney(self.Money)

	def reqRMB(self):
		INFO_MSG("reqRMB")
		self.client.onRMB(self.RMB)

	def reqData(self):
		INFO_MSG("reqData")
		self.client.onData(self.Data)

	def reqBuyWithGold(self,sum1):
		DEBUG_MSG("Account[%i].BuyWithGold:" % self.id)
		sum=int(sum1)
		if self.Data['money'] > sum*100-1:
			self.Data['money']=self.Data['money']-sum*100
			self.Data['kabao']=self.Data['kabao']+sum
			self.client.onbuycard(0)
		else:
			self.client.onbuycard(1)

	def reqBuyWithRMB(self,sum1):
		DEBUG_MSG("Account[%i].BuyWithGold:" % self.id)
		sum=int(sum1)
		if self.Data['RMB'] > sum*2-1:
		    self.Data['RMB']=self.Data['RMB']-sum*2
		    self.Data['kabao']=self.Data['kabao']+sum
		    self.client.onbuycard(0)
		else:
			self.client.onbuycard(1)


	def reqOpeningPack(self):
		DEBUG_MSG("Account[%i].reqOpeningPack:" % self.id)
		self.Data['kabao']=self.Data['kabao']-1
		data =  {'card1':0, 'card2':0, 'card3':0, 'card4':0, 'card5':0}
		namedata =  {'card1':"", 'card2':"", 'card3':"", 'card4':"", 'card5':""}
		for i in range(5): 
			data['card%i'%(i+1)]=random.randint(10000001,10000000+self.cardSum)
			namedata['card%i'%(i+1)]=(d_card_dis.datas[data['card%i'%(i+1)]]["name"])
			self.Card_Data['values'].append(data['card%i'%(i+1)])

		self.client.onOpeningPackResult(data,namedata)

	def reqAccountCardData(self):
		self.client.onAccountCardData(self.Card_Data)

	def reqAddCardGroup(self,group):
		if len( self.Card_Group) > 9:
			self.client.OnAddCardGroupErr(0)
		else :
			if len(group)!=32:
				self.client.OnAddCardGroupErr(1)
			else:
				self.Card_Group.append(group)

		self.client.OnGetKz(self.Card_Group)

	def reqDelCardGroup(self,index):
		DEBUG_MSG("Account[%i].reqDelCardGroup[%i]:" % (self.id,index))
		if len(self.Card_Group) > index - 1:
			del self.Card_Group[index]
		else:
			self.client.OnDelCarErr(0)

		for i in range(len(self.Card_Group)):
			self.Card_Group[i][31] = i

		self.client.OnGetKz(self.Card_Group)

	def reqUpdataCardGroup(self,group):
		DEBUG_MSG("Account[%i].reqUpdataPack:" % self.id)
		self.Card_Group[group[31]] = group

	def reqGetKz(self):
		DEBUG_MSG("Account[%i].reqGetKz abo:KZsum:[%s]" % (self.id,len(self.Card_Group)))

	def reqPlayerSum(self):
		KBEngine.globalData["Halls"].reqPlayerSum(self)

	def OnPlayerSum(self,PlayerSum,MarcherSum):
		self.client.onGetPlayerSum(PlayerSum)
		self.client.OnMarcherSum(MarcherSum)

	def reqStartMarch(self,whichKz):
		DEBUG_MSG("Account[%i].reqStartMarch: Kzid[%i]" % (self.id,whichKz))
		self.OnClientMsg_March("正在匹配对手")
		KBEngine.globalData["Halls"].reqAddMarcher(self)
		self.willUseKz = whichKz

	def reqStopMarch(self):
		DEBUG_MSG("Account[%i].reqStopMarch" % self.id)
		KBEngine.globalData["Halls"].reqDelMarcher(self)
		self.willUseKz = -1

	def OnEnterBattelField(self,battlefiled,_playerID):
		DEBUG_MSG("Account[%i].OnEnterBattelField" % self.id)
		self.BattleField = battlefiled
		self.playerID = _playerID
		self.BattleField.AccountReady(self.playerID)

	def OnClientMsg_March(self,msg):
		if self.client == None:
			return
		self.client.onMarchMsg(msg)

	def BattleFailed(self):#战斗匹配失败
		DEBUG_MSG("Account[%i].BattleInitFailed" % self.id)
		
		if not self.hasClient:
			if self.Avatar0 == None:
				self.destroy()
			else:
				self.Avatar0.BattleFailed()

			return

		self.reqStartMarch(self.willUseKz)

	def onGetClient(self):
		DEBUG_MSG("Account[%s]::onGetClient" % (self.id))
		if self.getClientTimeID == 0:
			self.getClientFailSum = 0
			if self.client!=None and self.clientControl:
				self.getClientPrc()
			else:
				self.getClientTimeID = self.addTimer(1,1,2)
		else:
			if self.client!=None and self.clientControl:
				self.getClientPrc()
				self.delTimer(self.getClientTimeID)
				self.getClientTimeID = 0
				self.getClientFailSum = 0
			else:
				self.getClientFailSum += 1
				if self.getClientFailSum > 5:
					self.delTimer(self.getClientTimeID)
					self.destroy()

	def waitClient(self):
		pass

	def reqGetClient(self):
		DEBUG_MSG("Account[%s]::reqGetClient" % (self.id))
		self.clientControl = True


	def getClientPrc(self):
		DEBUG_MSG("Account[%s]::getClientPrc battleResult:[%s]" % (self.id,self.battleResult))
		if self.battleResult == -1:
			pass
			#self.client.gotoMain()
		else:
			self.battleResultClientDisplay()

	def BattleEndResult(self,result):#1成功 0失败
		DEBUG_MSG("Account[%s]::BattleEndResult  result[%s]" % (self.id, result))

		if self.isDestroyed:
			DEBUG_MSG("Account[%s]::BattleEndResult processResultFail  self is destroyed" % (self.id))
			return

		if result == 1:
			self.Data["rank"] +=  8 + self.WinStreakSum*self.WinStreakSum
			self.WinStreakSum += 1

		else:
			self.Data["rank"] = int(0.996*	self.Data["rank"])
			self.WinStreakSum = 0

		
		self.onPlayingBattlefiled = None

		#self.Data["rank"] = 1000
		if self.onPlayingDestroy:
			self.destroy()
			return


		if self.client is not None:
			self.battleResultClientDisplay(result)
		else:
			self.battleResult = result

	def battleResultClientDisplay(self,success = -1):
		if success == -1:
			success == self.battleResult
		self.battleResult = -1

		if success == -1:
			self.getClientPrc()
			return

		rank = self.Data["rank"]

		if self.client == None:
			return

		self.client.battleResultClientDisplay(success,rank)


	def displayBattleResult(self):
		pass

	def onInitBattleField(self,oppoHero):
		self.client.onInitBattleField(oppoHero)

	def autoAddTask(self):
		DEBUG_MSG("autoAddTask  Account[%i]" %(self.id))
		taskll = []
		for i in range(len(self.Task)):
			taskll.append(self.Task[i][0])

		for key,task in d_task.datas.items():
			if task['autoAdd'] == 0:
				continue
			if task['ID'] in self.FinishedTask:
				continue
			if task['ID'] in taskll:
				continue

			list = [task['ID'],0]
			self.Task.append(list)
			DEBUG_MSG("autoAddTask  task[%s]" %(task['ID']))
			
	def updateTask(self):
		tasklist = ''
		for i in range(len(self.Task)):
			ID = self.Task[i][0]
			name = d_task.datas[ID]['name']
			des = d_task.datas[ID]['des']
			require = d_task.datas[ID]['require']
			finishSum = self.Task[i][1]
			needSum = d_task.datas[ID]['needSum']
			reward = d_task.datas[ID]['reward']
			list = str(i)+':'+str(name)+':'+str(des)+':'+str(require)+':'+str(finishSum)+':'+str(needSum)+':'+str(reward)
			tasklist += list+'#'

		#print(tasklist)
		self.client.onGetTaskList(tasklist)

	def reqUpdateTask(self):
		self.updateTask()

	def reqFinishTask(self,index):
		#是否完成任务判断 待加

		self.reward(d_task.datas[self.Task[index][0]]['sysReward'])
		self.FinishedTask.append(self.Task[index][0])
		del self.Task[index]
		self.updateTask()

	def reward(self,reward):
		rewards = reward.split('#')
		for obj in rewards:
			DEBUG_MSG("Account[%i].detail[%s]" % (self.id,obj))
			detail = obj.split(':')
			item = detail[0]
			sum = detail[1]


			if detail[0] == 'kabao':
				self.Data['kabao'] += int(sum)

		self.reqData()

	def reqChangeAvatar(self,roleType,cardList,name,index):
		DEBUG_MSG("reqChangeAvatar Account[%s]  roleType[%s]    cardList[%s] index[%s]" % (self.id,roleType,str(len(cardList))+"__"+str(cardList),index))

		if index == -1:
			if len(self.Avatar_List) > 17:
				self.client.onChangeAvatar('卡组添加失败达到上限')
				return

			props = {
				"name"				: name,
				"roleType"			: roleType,
				"cardList"			: cardList
				}

			self.Avatar_List.append(props)
			self.client.onChangeAvatar('卡组添加成功')
		else:
			DEBUG_MSG("reqChangeAvatar Account[%s]  index[%s]  cardList[%s]" % (self.id,index,str(len(cardList))+"__"+str(cardList)))
			if index > len(self.Avatar_List)-1:
				self.client.onChangeAvatar('序号出错，大于上限')
				return		
			self.Avatar_List[int(index)]['cardList'] = cardList
			if name != '':
				self.Avatar_List[int(index)]['name'] = name
			self.client.onChangeAvatar('修改卡组成功')
		self.reqAvatarList()

	def randomInitKZ(self):
		ls = []
		for i in range(30):
			ls.append(random.randint(10000001,10000000+self.cardSum))
		roleType = 0
		name = "随机生成卡组"
		index = -1
		self.reqChangeAvatar(roleType,ls,name,index)

	def reqRemoveAvatar(self, index):
		"""
		exposed.
		客户端请求删除一个角色
		"""
		DEBUG_MSG("Account[%i].reqRemoveAvatar: %s" % (self.id, index))

		if index > len(self.Avatar_List)-1:
			self.client.onChangeAvatar('序号出错，大于上限')
			return
		del self.Avatar_List[int(index)]
		self.client.onChangeAvatar('删除卡组成功')
		self.reqAvatarList()

		
	def reqAvatarList(self):
		"""
		exposed.
		客户端请求查询角色列表
		"""
		DEBUG_MSG("Account[%i].reqAvatarList: size=%i." % (self.id, len(self.Avatar_List)))
		self.client.onReqAvatarList(self.Avatar_List)

	def creatAvatar(self,battleFiled):
		'''
		'''
		DEBUG_MSG("Account[%i].creatAvatar" %(self.id))
		prarm = {
			"battlefiled":battleFiled,
			'nameA':self.Name,
			'roleType':self.Avatar_List[self.willUseKz]['roleType'],
			'cardList':self.Avatar_List[self.willUseKz]['cardList'],
			'playerIDB':self.playerID,
			'account':self					
			}
		self.Avatar0 = KBEngine.createBaseLocally("Avatar", prarm)
		self.client.onInitBattleField()
		self.onPlayingBattlefiled = battleFiled

	def reqHasEnteredBattlefiled(self):
		DEBUG_MSG("Account[%i].reqHasEnteredBattlefiled" %(self.id))
		self.giveClientTo(self.Avatar0)
		self.clientControl = False
		self.Avatar0.onClientInit()



	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------

	def onGiveClientToFailure(self):
		ERROR_MSG("Account::onGiveClientToFailure:(%i)" % (self.id))
		


