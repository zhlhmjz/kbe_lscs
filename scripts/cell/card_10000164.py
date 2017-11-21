# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj

class card_10000164(GameObj):
	#卡牌名称：猛击
	#卡牌描述：对一个随从造成2点伤害，如果它依然存活，则抽一张牌。
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def onUse(self,targetID,selfPos):
		super().onUse(targetID,selfPos)
		self.causeDamage(targetID,2)#对目标造成2伤害
		entity = self.getEntityByID(targetID)#获取目标
		if entity.pos.isdigit():#仍然活着
			self.getCard()#抽牌

	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	