# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj

class card_20001004(GameObj):
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------

	def onUse(self,targetID,selfPos):
		super(card_20001004, self).onUse(targetID,selfPos)
		params = {
			'attAdd': 1,
			'targetEntity': self.avatar,
			'delOnRoundEnd':1
		}
		self.creatBuff(params)
		self.avatar.getArmor(1)
	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	