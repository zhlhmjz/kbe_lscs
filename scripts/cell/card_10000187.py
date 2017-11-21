# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj

class card_10000187(GameObj):
	#卡牌名称：冷血
	#卡牌描述：使一个随从获得+2攻击力；<b>连击：</b>改为获得+4攻击力。
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def battleCry(self,targetID,selfPos):
		attAdd = 2
		if self.avatar.uesCardSumInRound > 0:
			attAdd = 4
		params = {
			'attAdd':attAdd
		}
		self.creatBuff(params,targetID)

	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	