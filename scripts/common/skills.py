# -*- coding: utf-8 -*-
from KBEDebug import *
class skillBase():
	def __init__(self):
		pass

	def test(self):
		DEBUG_MSG("Hall init %s"%self.msg)

	def onRoundStart(self,isSelf):
		pass

	def onUse(self,targetID):
		pass

	def onDead(self):
		pass

	def onHeroUseSkill(self,isSelf):
		pass

	def onBeDamaged(self,source,target,sum):
		pass

	def onRoundEnd(self,isSelf):
		pass

	def onUseSkillCard(self,isSelf,cardID):
		pass

	def onUseCard(self,isSelf,cardID):
		pass

	def onUseFollowerCard(self,isSelf,cardID):
		pass

#class card_10000001(skillBase):
	

	
