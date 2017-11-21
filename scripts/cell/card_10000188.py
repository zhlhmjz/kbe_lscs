# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj

class card_10000188(GameObj):
	#卡牌名称：秘教暗影祭司
	#卡牌描述：<b>战吼：</b>获得一个攻击力小于或等于2的敌方随从的控制权。
	def __init__(self):
		GameObj.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def battleCry(self,targetID,selfPos):
		entity = self.getEntityByID(targetID)
		if entity == None:
			DEBUG_MSG("card_10000188::battleCry:[%i].  targetID:[%s]noUse" % (self.id, targetID))
			return
		entity.changeController()

	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	