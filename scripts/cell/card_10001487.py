# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj
import random

class card_10001487(GameObj):
	#卡牌名称：砰砰机器人
	#卡牌描述：<b>亡语：</b>对一个随机敌人造成1到4点伤害。
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def onDead(self):
		damage = random.randint(1,4)
		self.randomCauseDamageToOppo(damage)

	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	