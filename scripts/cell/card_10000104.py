# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj
import random

class card_10000104(GameObj):
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def onUse(self,targetID,selfPos):
		super().onUse(targetID,selfPos)
		ls = [20000112,20000113,20000114]
		t = random.choice(ls)
		ls = [t]
		self.summorFollower(ls)

	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	