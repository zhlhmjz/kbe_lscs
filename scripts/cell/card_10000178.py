# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj

class card_10000178(GameObj):
	#卡牌名称：噩梦
	#卡牌描述：使一个随从获得+5/+5，在你的下一个回合开始时，消灭该随从。
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def battleCry(self,targetID,selfPos):
		params = {
			'attAdd':5,
			'HPAdd':5
		}
		self.creatBuff(params,targetID)

	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------

	def onRoundStartB(v,self,isSelf):
		if isSelf:
			self.die()