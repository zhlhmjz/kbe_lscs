# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj

class card_10000171(GameObj):
	#卡牌名称：帝王眼镜蛇
	#卡牌描述：消灭任何受到该随从伤害的随从。
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------


	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	