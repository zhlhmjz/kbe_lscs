# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj

class card_10000064(GameObj):
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def onUse(self,targetID,selfPos):
		super(card_10000064, self).onUse(targetID,selfPos)
		params = {
			'targetEntity':self.getEntityByID(targetID)
		}
		self.creatBuff(params)

	# --------------------------------------------------------------------------------------------
	#                              Effect
	# --------------------------------------------------------------------------------------------
	# --------------------------------------------------------------------------------------------
	#                              buffEffent
	# --------------------------------------------------------------------------------------------
	def onRoundStartB(v,self,isSelf):
		if isSelf:
			self.targetEntity.die()