# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj

class card_10000181(GameObj):
	#卡牌名称：自然平衡
	#卡牌描述：消灭一个随从，你的对手抽两张牌。
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def battleCry(self,targetID,selfPos):
		self.makeTargetDie(targetID)
		self.getOppoAvatar().getCard(2)

	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	