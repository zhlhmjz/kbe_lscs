# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObj import GameObj


class card_10000157(GameObj):
    # 卡牌名称：命令怒吼
    # 卡牌描述：在本回合中，你的随从的生命值无法被降到1点以下。抽一张牌。
    def __init__(self):
        GameObj.__init__(self)

    # --------------------------------------------------------------------------------------------
    #                              Callbacks
    # --------------------------------------------------------------------------------------------
    def onUse(self, targetID, selfPos):
        super(card_10000157, self).onUse(targetID, selfPos)
        self.changePos('BUFF')

    def onRoundEnd(self, isSelf):
        if isSelf:
            DEBUG_MSG("card_10000157:[%s]:pos[%s]:onRoundEnd delSelf" % (self.id, self.pos))
            self.delSendBuff()
            self.changePos('USED')

    def onEnvirBuff(self, target):
        params = {
            'targetEntity': target
        }
        self.creatEnvirBuff(params)

    def envBuffConditon(self, target):
        return target != self and target.pos.isdigit() and target.playerID == self.playerID

    # --------------------------------------------------------------------------------------------
    #                              Effect
    # --------------------------------------------------------------------------------------------
    def onBeforeRecvDamageB(v, self, damage, srcID, targetID):
        hp = self.getEntityByID(targetID).HP
        if targetID != self.targetEntity.id:
            return
        if damage > hp - 1:
            damage = hp - 1
        return damage
