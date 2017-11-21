# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj

class card_10000160(GameObj):
	#卡牌名称：鱼人领军
	#卡牌描述：所有其他鱼人获得+2/+1。
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def onEnvirBuff(self,target):
		params = {
			'attAdd':2,
			'HPAdd':1,
			'targetEntity':target
		}
		self.creatEnvirBuff(params)

	def envBuffConditon(self,target):
		return target != self and target.pos.isdigit() and target.playerID == self.playerID and target.race == '鱼人'

	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	