# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj

class card_10000082(GameObj):
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def onEnvirBuff(self,target):
		params = {
			'attAdd':2,
			'targetEntity':target
		}
		self.creatEnvirBuff(params)

	def envBuffConditon(self,target):
		return target != self and target.pos.isdigit() and abs(int(target.pos) - int(self.pos)) == 1 and target.playerID == self.playerID

	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	