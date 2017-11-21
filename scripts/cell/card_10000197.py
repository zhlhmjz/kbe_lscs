# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj

class card_10000197(GameObj):
	#卡牌名称：末日预言者
	#卡牌描述：在你的回合开始时，消灭所有随从。
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def onRoundStart(self,isSelf):
		if isSelf:
			ls = self.getFollowerAndHeroList(False)
			ls.remove(self)
			for follower in ls:
				self.makeTargetDie(follower.id)
			self.die()


	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	