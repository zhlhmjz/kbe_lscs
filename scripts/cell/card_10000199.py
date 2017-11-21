# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj
import random

class card_10000199(GameObj):
	#卡牌名称：控心术
	#卡牌描述：随机复制对手的牌库中的一张随从牌，并将该随从置入战场。
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def battleCry(self,targetID,selfPos):
		ls = self.getAllEntity()
		kzls = []
		for f in ls:
			if f.playerID == self.another(self.playerID) and f.pos == 'KZ' and f.type == 3:
				kzls.append(f)
		if self.hasPostion():
			if len(kzls) > 0:
				target = random.choice(kzls)
				self.avatar.creatCardEntity(target.cardID,'6')
				self.avatar.followerPosReassigned()


	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	