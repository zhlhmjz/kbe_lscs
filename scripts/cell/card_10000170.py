# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj
import random

class card_10000170(GameObj):
	#卡牌名称：致命射击
	#卡牌描述：随机消灭一个敌方随从。
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------

	def battleCry(self,targetID,selfPos):
		targetLS = self.getFollowerAndHeroList(False)
		if len(targetLS) > 0:
			target = random.choice(targetLS)
			self.makeTargetDie(target.id)
	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	