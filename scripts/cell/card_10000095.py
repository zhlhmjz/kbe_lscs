# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj
import random

class card_10000095(GameObj):
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def onUse(self,targetID,selfPos):
		super().onUse(targetID,selfPos)
		ls = []
		if len(self.avatar.cardEntityList) < 3:
			ls = self.avatar.cardEntityList
		else:
			ls = random.sample(self.avatar.cardEntityList,3)
		idls = []
		for e in ls:
			idls.append(e.id)
		self.avatar.chooseCardWithEntityID(idls)

	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	