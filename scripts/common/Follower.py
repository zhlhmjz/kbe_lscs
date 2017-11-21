# -*- coding: utf-8 -*-
import KBEngine
import d_card_dis
import random
import types
from KBEDebug import *
from array import *

class Follower:

	self.property = dict()

	def __init__(self,property,BattleField):
		DEBUG_MSG("test creat a follower success" )
		self.property = property
		