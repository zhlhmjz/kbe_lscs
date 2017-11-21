# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj

class card_10000062(GameObj):
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------

	def onUse(self,targetID,selfPos):
		super(card_10000062, self).onUse(targetID,selfPos)
		target = self.getEntityByID(targetID)
		if target == None:
			return
		self.causeDamage(targetID,1)


	def onKillFollower(self, targetID):
		super().onKillFollower(targetID)
		DEBUG_MSG("card_10000062:[%s] onKillFollower:targetID:[%s]" % (self.id, targetID))
		self.avatar.getCard(1)

	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	