# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj

class card_10000086(GameObj):
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------

	def onUse(self,targetID,selfPos):
		super().onUse(targetID,selfPos)
		ls = self.getFollowerAndHeroList()
		for e in ls:
			if e.playerID == self.playerID:
				self.causeHeal(e.id,2)
			else:
				self.causeDamage(e.id,2)
	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	