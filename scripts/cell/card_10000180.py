# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj

class card_10000180(GameObj):
	#卡牌名称：忏悔
	#卡牌描述：<b>奥秘：</b>在你的对手召唤一个随从后，使该随从的生命值降为1。
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def onSummonFollower(self,followerEntityID):
		entity = self.getEntityByID(followerEntityID)
		if entity.playerID == self.playerID:
			return
		params = {
			'HP':1
		}
		self.creatBuff(params,followerEntityID)
		self.changePos('USED')

	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	