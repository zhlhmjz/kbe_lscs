# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj

class card_10000108(GameObj):
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def onUse(self,targetID,selfPos):
		super().onUse(targetID,selfPos)
		self.avatar.getCard(2)

	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	