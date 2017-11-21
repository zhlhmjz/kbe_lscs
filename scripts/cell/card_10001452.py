# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj

class card_10001452(GameObj):
	#卡牌名称：砰砰博士
	#卡牌描述：<b>战吼：</b>召唤两个1/1的砰砰机器人。<i>警告：该机器人随时可能爆炸。</i>
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------

	def onUse(self,targetID,selfPos):
		super(card_10001452, self).onUse(targetID,selfPos)
		ls = [10001487,10001487]
		self.summorFollower(ls,self.id,self.pos)
	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	