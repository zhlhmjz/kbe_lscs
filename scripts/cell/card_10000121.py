# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj

class card_10000121(GameObj):
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def onUse(self,targetID,selfPos):
		super().onUse(targetID,selfPos)
		params = {
			'attAdd':2,
			'delOnRoundEnd':1
		}
		ls = self.getFollowerAndHeroList()
		for e in ls:
			if e.playerID != self.playerID:
				ls.remove(e)
		self.creatBuffs(params,ls)

	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	