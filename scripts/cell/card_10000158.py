# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj

class card_10000158(GameObj):
	#卡牌名称：紫罗兰教师
	#卡牌描述：每当你施放一个法术，召唤一个1/1的紫罗兰学徒。
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------

	def onUseCard(self,playerID,cardEntityID,cardID):
		entity = self.getEntityByID(cardEntityID)
		if entity == None:
			return
		if entity.type == '1' and entity.playerID == self.playerID:
			ls = [10000399]
			self.summorFollower(ls,self.id,self.pos)
	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	