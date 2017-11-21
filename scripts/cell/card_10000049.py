# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj

class card_10000049(GameObj):
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def onUse(self,targetID,selfPos):
		GameObj.onUse(self,targetID,selfPos)
		target = self.getEntityByID(targetID)
		if target == None:
			return
		params = {
			'attAdd':2,
			'targetEntity':target
		}
		self.creatBuff(params)
		target.rush()

	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	