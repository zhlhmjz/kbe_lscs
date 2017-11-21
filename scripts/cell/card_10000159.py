# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj

class card_10000159(GameObj):
	#卡牌名称：暮光幼龙
	#卡牌描述：<b>战吼：</b>你每有一张手牌，便获得+1生命值。
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def onUse(self,targetID,selfPos):
		super(card_10000159, self).onUse(targetID,selfPos)
		ls = self.getSelfHandCardList()
		params = {
			'HPAdd':len(ls),
			'targetEntity':self
		}
		self.creatBuff(params)

	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	