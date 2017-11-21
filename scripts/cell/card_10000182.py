# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj

class card_10000182(GameObj):
	#卡牌名称：奥金尼灵魂祭司
	#卡牌描述：你的恢复生命值的牌和技能改为造成等量的伤害。
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def beforeCauseHeal(self,source,target,healSum):
		super().beforeCauseHeal(source,target,healSum)
		if source.id == self.id and healSum > 0:
			healSum = -healSum
		return [target,healSum]

	def battleCry(self,targetID,selfPos):
		self.battlefiled.beforeCauseHealOpreateList.append(self)

	def onDead(self):
		self.battlefiled.beforeCauseHealOpreateList.remove(self)
	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	