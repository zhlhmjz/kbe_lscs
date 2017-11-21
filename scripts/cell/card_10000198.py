# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj

class card_10000198(GameObj):
	#卡牌名称：救赎
	#卡牌描述：<b>奥秘：</b>当一个你的随从死亡时，使其回到战场，并具有1点生命值。
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def onFollowerDie(self,followerEntity):
		if followerEntity.playerID == self.playerID:
			if len(self.followerList) <= 6:
				followerEntity.HP = 1
				self.avatar.followerPosAssigned(followerEntity.id,6)
			self.changePos('USED')


	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	