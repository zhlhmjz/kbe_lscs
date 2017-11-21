# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj

class card_10000190(GameObj):
	#卡牌名称：背叛
	#卡牌描述：使一个敌方随从对其相邻的随从造成等同于其攻击力的伤害。
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def battleCry(self,targetID,selfPos):
		entity = self.getEntityByID(targetID)
		followerList = entity.avatar.followerList
		damageList = []
		for follower in followerList:
			if abs(int(follower.pos)-int(entity.pos)) == 1:
				damageList.append(follower)
		entity.causeDamages(damageList,self.att)

	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	