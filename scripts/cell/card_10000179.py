# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj

class card_10000179(GameObj):
	#卡牌名称：暗影狂乱
	#卡牌描述：直到回合结束，获得一个攻击力小于或等于3的敌方随从的控制权。
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def battleCry(self,targetID,selfPos):
		entity = self.getEntityByID(targetID)
		entity.changeController()
		params = {
			'changeControllerOnRoundEnd':1
		}
		self.creatBuff(params,targetID)

	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	