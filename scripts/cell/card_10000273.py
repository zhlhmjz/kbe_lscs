# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj

class card_10000273(GameObj):
	#卡牌名称：裂颅之击
	#卡牌描述：对敌方英雄造成2点伤害；<b>连击：</b>在下个回合将其移回你的手牌。
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------


	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	