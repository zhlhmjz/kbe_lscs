# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj

class card_10000081(GameObj):
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def onEnvirBuff(self,target):
		params = {
			'HPAdd':1,
			'targetEntity':target
		}
		self.creatEnvirBuff(params)

	def envBuffConditon(self,target):
		return target != self and target.pos.isdigit() and target.playerID == self.playerID and target.race == '图腾'

	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	