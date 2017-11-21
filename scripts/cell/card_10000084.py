# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj

class card_10000084(GameObj):
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------

	def onUse(self,targetID,selfPos):
		super().onUse(targetID,selfPos)
		ls = self.getFollowerAndHeroList(False)
		for e in ls:
			if e.playerID != self.playerID:
				ls.remove(e)
		params = {
			'attAdd':3,
			'delOnRoundEnd':1
		}
		self.creatBuffs(params,ls)


	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	