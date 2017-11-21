# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj

class card_10000172(GameObj):
	#卡牌名称：灵魂虹吸
	#卡牌描述：消灭一个随从，为你的英雄恢复#3点生命值。
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def battleCry(self,targetID,selfPos):
		self.makeTargetDie(targetID)
		self.causeHeal(self.avatarID,3)

	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	