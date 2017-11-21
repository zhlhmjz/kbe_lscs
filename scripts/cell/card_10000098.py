# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj

class card_10000098(GameObj):
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def onUse(self,targetID,selfPos):
		super().onUse(targetID,selfPos)
		params = {
			'attAdd':2,
			'HPAdd':2
		}
		self.creatBuff(params,targetID)
		self.sendTaunt(targetID)

	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	