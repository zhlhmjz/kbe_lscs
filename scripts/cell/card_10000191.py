# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj

class card_10000191(GameObj):
	#卡牌名称：严酷的监工
	#卡牌描述：<b>战吼：</b>对一个随从造成1点伤害，并使其获得+2攻击力。
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def battleCry(self,targetID,selfPos):

		params = {
			'attAdd':2
		}
		self.creatBuff(params,targetID)
		self.causeDamage(targetID, 1)

	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	