# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj

class card_10000161(GameObj):
	#卡牌名称：战争古树
	#卡牌描述：<b>抉择：</b>+5攻击力；或者+5生命值并具有<b>嘲讽</b>。
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------

	def chooseStrLs(self):
		return [
				'+5攻击',
				'+5生命值并具有<b>嘲讽</b>'
			]

	def choose0(self,targetID,needPos):
		params = {
			'attAdd': 5,
			'targetEntity': self
		}
		self.creatBuff(params)

	def choose1(self,targetID,needPos):
		params = {
			'HPAdd':5,
			'targetEntity':self
		}
		self.creatBuff(params)
		self.sendTaunt(self.id)

	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	