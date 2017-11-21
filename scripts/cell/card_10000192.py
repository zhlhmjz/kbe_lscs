# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj

class card_10000192(GameObj):
	#卡牌名称：蒸发
	#卡牌描述：<b>奥秘：</b>当一个随从攻击你的英雄，将其消灭。
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def onGetAttTarget(self,source,target):
		if target == self.avatar and source.pos.isdigit():
			target = None
			self.makeTargetDie(source)
			self.changePos('USED')


	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	