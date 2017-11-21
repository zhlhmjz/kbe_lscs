# -*- coding: utf-8 -*-
import KBEngine
import random
import time
from skills import skillBase
from KBEDebug import *

class Hall(KBEngine.Base):
	"""
	大厅管理器实体
	该实体管理该服务组上所有的大厅
	"""




	def __init__(self):
		DEBUG_MSG("Hall init")
		KBEngine.Base.__init__(self)

		#储存大厅
		KBEngine.globalData["Halls"] = self
		
		# 存放所有正在匹配玩家mailbox
		self.OnMarchingPlayer = []

		# 存放所有在线玩家mailbox
		self.player = []
		
		# 检测是否正在匹配
		self.OnMarch = 0

		
		#定时更新当前玩家
		self.addTimer(3, 6, 1)
		#匹配程序
		self.addTimer(5,2,2)

		self.bb = skillBase.test
		self.msg = "shishi"
		self.bb(self)

		
	def onTimer(self, id, userArg):

		#DEBUG_MSG(id, userArg)
		#更新在线人数
		if userArg == 1:
			self.UpdataPlayer()
		if userArg ==2:
			self.March()
			#self.test()




	def test(self):
		if len(self.OnMarchingPlayer)==1:
			self.CreatBattleField(self.OnMarchingPlayer[0],self.OnMarchingPlayer[0])

	def March(self):
		#DEBUG_MSG("English print::eng")
		#DEBUG_MSG("Chinese print::中文")
		#正在匹配则返回
		if self.OnMarch == 1:
			return

		self.OnMarch = 1
		#DEBUG_MSG("Server Start A March")
		for i in range(len(self.OnMarchingPlayer)):
			IsSuccessed = 0
			for j in range(len(self.OnMarchingPlayer)):
				if i == j:
					continue
				if self.OnMarchingPlayer[j].Data["rank"] > self.OnMarchingPlayer[i].Data["rank"]*(1-0.01*self.OnMarchingPlayer[i].HaveMarchSum) - self.OnMarchingPlayer[i].HaveMarchSum and self.OnMarchingPlayer[j].Data["rank"] < self.OnMarchingPlayer[i].Data["rank"]*(1+0.01*self.OnMarchingPlayer[i].HaveMarchSum) + self.OnMarchingPlayer[i].HaveMarchSum:
					DEBUG_MSG("March Successed player1:%i player2:%i" %(self.OnMarchingPlayer[i].id,self.OnMarchingPlayer[j].id))
					self.CreatBattleField(self.OnMarchingPlayer[i],self.OnMarchingPlayer[j])
					IsSuccessed = 1
			if IsSuccessed == 0:
				self.OnMarchingPlayer[i].HaveMarchSum +=1
			else:
				break
	# 匹配成功后跳出匹配 防止再次匹配时再弄到J那个
	# 通过添加定时器调用此函数

		self.OnMarch = 0


	def CreatBattleField(self,player1,player2):
		#成功匹配完成后再调用一次匹配 增加匹配的效率
		DEBUG_MSG("Start a battle player1:%i player2:%i" %(player1.id,player2.id))
		if player1.isDestroyed or player2.isDestroyed:
			if player1.isDestroyed:
				self.OnMarchingPlayer.remove(player1)
			if player2.isDestroyed:
				self.OnMarchingPlayer.remove(player2)
			DEBUG_MSG("March Fail because One is destroyed")
			return
		DEBUG_MSG("Battle March Successed player1:%i player2:%i" %(player1.id,player2.id))


		prarm = {
			"player0":player1,
			"player1":player2			
			}

		BattleField = KBEngine.createBaseAnywhere("BattleField", prarm)
		if player1 in self.OnMarchingPlayer:
			self.OnMarchingPlayer.remove(player1)
		if player2 in self.OnMarchingPlayer:		
			self.OnMarchingPlayer.remove(player2)
		self.March()


	def UpdataPlayer(self):

		#此函数更新在线人数和正在匹配的玩家人数 删除实体被销毁的

		for i in range(len(self.player)):
			if self.player[i].isDestroyed == True:
				DEBUG_MSG("del_self.player::player")
				del self.player[i]
				self.UpdataPlayer()
				return

		for i in range(len(self.OnMarchingPlayer)):
			if self.OnMarchingPlayer[i].isDestroyed == True:
				DEBUG_MSG("del_self.OnMarchingPlayer::OnMarchingPlayer")
				del self.OnMarchingPlayer[i]
				self.UpdataPlayer()
				return


		#DEBUG_MSG("onlineSum:%i" % len(self.player))
		#DEBUG_MSG("OnMarchingSum:%i" % len(self.OnMarchingPlayer))


	def reqAddPlayer(self,player):

		#此函数添加上线玩家入列表

		if player in self.player: 
			return
		DEBUG_MSG("Account[%i].reqAddPlayer:" % player.id)
		self.player.append(player)

	def reqPlayerSum(self,player):
		
		#此函数是为了获得在线人数
		#此函数是为了获得正在匹配人数
		#DEBUG_MSG("Account[%i].reqPlayerSum:" % player.id)
	
		player.OnPlayerSum(len(self.player),len(self.OnMarchingPlayer))


	def reqAddMarcher(self,player):

		#此函数添加匹配玩家入列表
		DEBUG_MSG("Account[%i].reqAddMarcher:" % player.id)

		if player in self.OnMarchingPlayer: 
			return

		player.HaveMarchSum =0

		self.OnMarchingPlayer.append(player)

	def reqDelMarcher(self,player):

		#此函数删除匹配玩家从列表
		DEBUG_MSG("Account[%i].reqDelMarcher:" % player.id)
		if player not in self.OnMarchingPlayer: 
			return

		self.OnMarchingPlayer.remove(player)
