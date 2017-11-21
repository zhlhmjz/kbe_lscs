# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj
import random

class card_10000169(GameObj):
	#卡牌名称：误导
	#卡牌描述：<b>奥秘：</b>当一个角色攻击你的英雄时，改为该角色攻击另一个随机角色。
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def onUse(self,targetID,selfPos):
		super(card_10000169, self).onUse(targetID,selfPos)
		self.battlefiled.onGetAttTargetOpreateList.append(self)

	def onDead(self):
		self.battlefiled.onGetAttTargetOpreateList.remove(self)

	def onGetAttTarget(self,source,target):
		super(card_10000169, self).onGetAttTarget(source,target)
		if source.playerID != self.playerID and target.playerID == self.playerID:
			allTargetList = self.getAllEntity()
			targetList= []
			for tr in allTargetList:
				if self.posIsInBattleFiled(tr.pos):
					targetList.append(tr)
			DEBUG_MSG('card_10000169:[%s]onGetAttTarget::sourceID:[%s] targetID:[%s] lenofTargetList:[%s]' % (self.id, source.id,target.id,len(targetList)))
			target = random.choice(targetList)
			if self in self.battlefiled.onGetAttTargetOpreateList:
				self.battlefiled.onGetAttTargetOpreateList.remove(self)
			self.changePos('USED')
		return target


	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	