# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj

class card_10000051(GameObj):
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------

	def onUse(self,targetID,selfPos):
		GameObj.onUse(self,targetID,selfPos)
		self.avatar.armor += 5
		self.avatar.getCard()
	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	