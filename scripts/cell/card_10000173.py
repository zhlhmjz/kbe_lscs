# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj
from interfaces.Buff import Buff

class card_10000173(GameObj):
	#卡牌名称：狂暴
	#卡牌描述：使一个受伤的随从获得+3/+3。
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def battleCry(self,targetID,selfPos):
		params = {
			'attAdd':3,
			'HPAdd':3
		}
		self.creatBuff(params,targetID)

	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	