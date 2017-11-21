# -*- coding: utf-8 -*-		self.
import KBEngine
from KBEDebug import *
import d_card_dis

class Buff(KBEngine.Entity):
	def __init__(self):
		KBEngine.Entity.__init__(self)	
		'''
		self.pos
		HAND		手牌
		KZ			卡组中
		0-6			场上1-7号
		HERO		英雄
		WEAPON		武器
		SKILL		技能
		DEAD		死过的卡（随从）
		USED		用过的卡（法术）
		SECRET		奥秘
		'''
		self.isFirst = True
		self.targetEntity.addBuff(self)
		#self.onAddBuff()

	def onAddBuff(self):
		self.onAddDefaultProcess()

	def onRemoveBuff(self):
		pass

	def delBuff(self):
		self.onRemoveBuff()
		self.targetEntity.onRemoveBuff(self.id)
		if self.envir == 1:
			self.sourceEntity.onRemoveSendBuff(self.id)
		self.destroy()

	def delBuffDir(self):
		self.targetEntity.onRemoveBuff(self.id)
		if self.envir == 1:
			self.sourceEntity.onRemoveSendBuff(self.id)
		self.destroy()

	def remove(self):
		self.delBuff()

	def onAddDefaultProcess(self):
		DEBUG_MSG("BUFF::onAddDefaultProcess: %i, targetEntity:%s," % ( self.id, self.targetEntity))
		if self.att > -1:
			self.targetEntity.att = self.att
		if self.attAdd > -1:
			self.targetEntity.att += self.attAdd
		if self.HP > -1:
			self.targetEntity.maxHP = self.HP
		if self.HPAdd > -1:
			self.targetEntity.maxHP += self.HPAdd
		if self.cost > -1:
			self.targetEntity.cost = self.cost
		if self.costAdd != -999:
			self.targetEntity.cost += self.costAdd

		if self.isFirst:
			if self.HP > -1:
				self.targetEntity.HP = self.HP
			if self.HPAdd > -1:
				self.targetEntity.HP += self.HPAdd
			self.isFirst = False

		if self.spellPower != 0 and self.targetEntity == self.targetEntity.avatar:
			self.targetEntity.spellPower += self.spellPower


	def onRemoveDefaultProcess(self):
		pass

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def onTimer(self, tid, userArg):
		"""
		KBEngine method.
		引擎回调timer触发
		"""
		#DEBUG_MSG("%s::onTimer: %i, tid:%i, arg:%i" % (self.getScriptName(), self.id, tid, userArg))

	def onRestore(self):
		"""
		KBEngine method.
		entity的cell部分实体被恢复成功
		"""
		
	def onDestroy(self):
		"""
		KBEngine method.
		当前entity马上将要被引擎销毁
		可以在此做一些销毁前的工作
		"""
		DEBUG_MSG("onDestroy(%i)" % self.id)

	def onBuffTick(self,situation):
		"""
		buff的tick
		此处可以轮询所有的buff，将需要执行的buff执行
		"""
		DEBUG_MSG("onBuffTick")

	#--------------------------------------------------------------------------------------------
	#                              Effect
	#--------------------------------------------------------------------------------------------
	def onRoundStart(self,isSelf):
		self.sourceEntity.onRoundStartB(self,isSelf)

	def onRoundEnd(self,isSelf):
		if isSelf:
			if self.changeControllerOnRoundEnd > 0:
				self.targetEntity.changeController()
			if self.delOnRoundEnd > 0:
				self.delBuff()

	def onUse(self,targetID,selfPos):
		pass

	def onDead(self):
		pass

	def onHeroUseSkill(self,isSelf):
		pass

	def onBeDamaged(self,srcID,sum):
		pass

	def onUseSkillCard(self,isSelf,cardID):
		pass

	def onUseCard(self,isSelf,cardID):
		pass

	def onUseFollowerCard(self,isSelf,cardID):
		pass

	def onBeAtted(self,srcID):
		pass

	def onAtt(self):
		pass

	def onCauseDamage(self,targetID,damage):
		pass

	def onTargetPosChange(self):
		pass

	def onBeforeRecvDamage(self, damage, targetID, srcID):
		damage = self.sourceEntity.onBeforeRecvDamageB(self,damage,targetID,srcID)
		return damage

	#--------------------------------------------------------------------------------------------
	#                              Base Method
	#--------------------------------------------------------------------------------------------

	def getEntityByID(self,ID):
		entity = KBEngine.entities.get(ID,None)	
		return entity

	def getOppoAvatar(self):
		playerID = self.targetEntity.playerID
		if playerID == 0:
			return self.targetEntity.battlefiled.avatarList[1]
		elif playerID == 1:
			return self.targetEntity.battlefiled.avatarList[0]
		else:
			ERROR_MSG('getOppoAvatarErr:playerID:'%playerID)
