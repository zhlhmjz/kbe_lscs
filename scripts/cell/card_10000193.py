# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj

class card_10000193(GameObj):
	#卡牌名称：劫持者
	#卡牌描述：<b>连击：</b>将一个随从移回其拥有者的手牌。
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def battleCry(self,targetID,selfPos):
		entity = self.getEntityByID(targetID)
		if entity != None:
			entity.changePos('HAND')

	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	