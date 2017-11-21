# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj

class card_10000176(GameObj):
	#卡牌名称：风险投资公司雇佣兵
	#卡牌描述：你的随从牌的法力值消耗增加3点。
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def envBuffConditon(self,target):
		return target.pos == 'HAND' and target.playerID == self.playerID

	def onEnvirBuff(self,target):
		params = {
			'costAdd':1,
			'targetEntity':target
		}
		self.creatEnvirBuff(params)

	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	