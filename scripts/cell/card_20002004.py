# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj

class card_20002004(GameObj):
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def onRoundEnd(self,isSelf):
		super().onRoundEnd(isSelf)
		if isSelf:
			ls = self.getSelfFollowerAndHeroList(False)
			for e in ls:
				self.causeHeal(e,1)


	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	