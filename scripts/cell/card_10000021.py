# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj

class card_10000021(GameObj):
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------

	def onUse(self,targetID,selfPos):
		super().onUse(targetID,selfPos)
		target = self.getEntityByID(targetID)
		if target == None:
			return
		params = {
			'attAdd':1,
			'HPAdd':1,
			'targetEntity':target
		}
	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	