# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj

class card_10000200(GameObj):
	#卡牌名称：暗影烈焰
	#卡牌描述：消灭一个友方随从，对所有敌方随从造成等同于其攻击力的伤害。
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def battleCry(self,targetID,selfPos):
		entity = self.getEntityByID(targetID)
		harm = entity.att
		self.makeTargetDie(targetID)
		self.causeDamageToAllOppo(harm,False)
	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	