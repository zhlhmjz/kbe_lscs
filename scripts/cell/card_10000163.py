# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj

class card_10000163(GameObj):
	#卡牌名称：剑刃乱舞
	#卡牌描述：摧毁你的武器，对所有敌方随从造成等同于其攻击力的伤害。
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------

	def onUse(self,targetID,selfPos):
		super(card_10000163, self).onUse(targetID,selfPos)
		weapon = self.getSelfWeapon()
		if weapon == None:
			return
		damage = weapon.att
		self.causeDamageToAllOppo(damage,False)
		self.avatar.loseWeapon()
	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	