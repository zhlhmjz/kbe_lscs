import KBEngine
import d_card_dis
import random
import types
from KBEDebug import *
from array import *

class CardList(KBEngine.Base):

	def __init__(self):

		DEBUG_MSG("cardList init")
		KBEngine.Base.__init__(self)

		#储存自己
		KBEngine.globalData["cardList"] = self

		self.havingQueryList = dict()
		self.nocardReturn1 = 10000001

	def queryList(self,infor,searchRank = 0):
		DEBUG_MSG("queryList  infor:[%s]" %(infor))
		if infor in self.havingQueryList.keys():
			return self.havingQueryList[infor]
		else:
			cardList = []
			if 'S' == infor[0:1]:#模式1：S+5位前缀 获取指定列表
				index = infor[1:]
				for i in range(1000):
					key = int(index+'000')+i
					if key in d_card_dis.datas.keys():
						cardList.append(key)
					else:
						continue
				if len(cardList) > 0:
					self.havingQueryList[infor] = cardList

				else:
					DEBUG_MSG("cardList not found ::infor:[%s]"%infor)
					return
			if infor[0:1] == 'C':#模式二 C+数字 表示几费的牌
				cost = int(infor[1:])
				for key in d_card_dis.datas.keys():
					if int(d_card_dis.datas[key]['cost']) == cost:
						if d_card_dis.datas[key]['searchRank'] < searchRank+1:
							cardList.append(int(key))
				if len(cardList) > 0:
					self.havingQueryList[infor] = cardList
			if infor[0:1] == 'X':#模式三 X+键/值
				infos = infor[1:].split('/')
				key = infos[0]
				value = infos[1] 
				for key in d_card_dis.datas.keys():
					if str(d_card_dis.datas[key][str(key)]) == str(value):
						if d_card_dis.datas[key]['searchRank'] < searchRank+1:
							cardList.append(int(key))
				if len(cardList) > 0:
					self.havingQueryList[infor] = cardList

			DEBUG_MSG("queryList  infor:[%s] ans:[%s]" %(infor,str(cardList)))          
			return cardList			



	def queryCard(self,infor):
		list = self.queryList(infor)
		ans = random.choice(list)
		DEBUG_MSG("queryCard  infor:[%s] ans:[%s]" %(infor,ans))
		return ans

	def ifHasConditonCard(self,cardIDlist,conditon):
		conditonList = self.queryList(conditon)
		for ID in cardIDlist:
			if ID in conditonList:
				return True
		return False

	def ifHasEnoughConditonCard(self,cardIDlist,conditon,Needsum):
		conditonList = self.queryList(conditon)
		sum = 0
		for ID in cardIDlist:
			if ID in conditonList:
				sum += 1
		if sum>=Needsum:
			return True
		return False

		