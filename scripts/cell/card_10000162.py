# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj

class card_10000162(GameObj):
	#卡牌名称：飞刀杂耍者
	#卡牌描述：每当你召唤一个随从时，对一个随机敌方角色造成1点伤害。
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------

	def onSummonFollower(self,followerEntityID):
		super(card_10000162, self).onSummonFollower(followerEntityID)
		self.randomCauseDamageToOppo(1)
	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	