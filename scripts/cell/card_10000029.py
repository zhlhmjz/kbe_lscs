# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj

class card_10000029(GameObj):
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------

	def onBeDamaged(self,srcID,sum):
		super().onBeDamaged(srcID,sum)
		if self.silent == 1:
			return
		params = {
			'attAdd':3,
			'targetEntity':self
		}
		self.creatBuff(params)
	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	