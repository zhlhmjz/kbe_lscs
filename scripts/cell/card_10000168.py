# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj

class card_10000168(GameObj):
	#卡牌名称：烈焰小鬼
	#卡牌描述：<b>战吼：</b>对你的英雄造成3点伤害。
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def onUse(self,targetID,selfPos):
		super(card_10000168, self).onUse(targetID,selfPos)
		self.causeDamage(self.avatarID,3)

	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	