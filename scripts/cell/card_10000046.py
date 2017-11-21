# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj

class card_10000046(GameObj):
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------

	def onUse(self,targetID,selfPos):
		super(card_10000046, self).onUse(targetID,selfPos)
		params = {
			'attAdd':4,
			'targetEntity':self.avatar,
			'delOnRoundEnd':1
		}
		self.creatBuff(params)
	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	