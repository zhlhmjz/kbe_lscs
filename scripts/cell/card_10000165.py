# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj

class card_10000165(GameObj):
	#卡牌名称：大法师安东尼达斯
	#卡牌描述：每当你施放一个法术，将一张“火球术”法术牌置入你的手牌。
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def onUseCard(self,playerID,cardEntityID,cardID):
		super(card_10000165, self).onUseCard(playerID,cardEntityID,cardID)
		if playerID == self.playerID:
			entity = self.getEntityByID(cardEntityID)
			if entity != None:
				if entity.type == 1:
					self.createHandCard(10000106)

	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	