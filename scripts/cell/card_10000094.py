# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj
import random

class card_10000094(GameObj):
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def onUse(self,targetID,selfPos):
		super().onUse(targetID,selfPos)
		oa = self.getOppoAvatar()
		idls = []
		for e in oa.cardEntityList:
			if e.pos == 'HAND':
				idls.append(e.cardID)
		if len(idls)==0:
			return
		card = random.choice(idls,1)
		self.getCardWithCardID(card)

	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	