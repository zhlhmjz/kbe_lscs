# -*- coding: utf-8 -*-
import KBEngine
import random
from KBEDebug import *
from interfaces.GameObj import GameObj

class card_20001006(GameObj):
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def onUse(self,targetID,selfPos):
		super(card_20001006, self).onUse(targetID,selfPos)
		ls = []
		for entity in self.avatar.followerList:
			ls.append(entity.cardID)
		l = [20002001,20002002,20002003,20002004]
		l2 = [20002001,20002002,20002003,20002004]
		for id0 in l2:
			#DEBUG_MSG('card_20001006:[%s]onUse:id0[%s] in ls:[%s]  ls:[%s]' % (self.id,id0, id0 in ls,str(ls)))
			if id0 in ls:
				l.remove(id0)

		if len(l) > 0:
			a = random.choice(l)
			self.summorFollower([a])


	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	