# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj

class card_10000184(GameObj):
	#卡牌名称：叫嚣的中士
	#卡牌描述：<b>战吼：</b>本回合中，使一个随从获得+2攻击力。
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def battleCry(self,targetID,selfPos):
		params = {
			'attAdd':2,
			'delOnRoundEnd':1
		}
		self.creatBuff(params,targetID)

	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	