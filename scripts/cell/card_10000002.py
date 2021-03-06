# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj

class card_10000002(GameObj):
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------


	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	def onUse(self,targetID,selfPos):
		GameObj.onUse(self,targetID,selfPos)
		entity = self.getEntityByID(targetID)
		if entity == None:
			return

		entity.recvHeal(self.id,2)