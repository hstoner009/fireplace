from ..utils import *


# Injured Blademaster
class CS2_181:
	def action(self):
		self.hit(self, 4)


# Young Priestess
class EX1_004:
	def OWN_TURN_END(self):
		other_minions = [t for t in self.controller.field if t is not self]
		if other_minions:
			target = random.choice(other_minions)
			target.buff("EX1_004e")


# Alarm-o-Bot
class EX1_006:
	def OWN_TURN_BEGIN(self):
		minions = self.controller.hand.filterByType(CardType.MINION)
		if minions:
			self.bounce()
			self.controller.summon(random.choice(minions))


# Angry Chicken
class EX1_009:
	class Enrage:
		Atk = 5


# Twilight Drake
class EX1_043:
	def action(self):
		for card in self.controller.hand:
			self.buff(self, "EX1_043e")


# Questing Adventurer
class EX1_044:
	def OWN_CARD_PLAYED(self, card):
		self.buff(self, "EX1_044e")


# Coldlight Oracle
class EX1_050:
	def action(self):
		self.controller.draw(2)
		self.controller.opponent.draw(2)


# Mana Addict
class EX1_055:
	def OWN_CARD_PLAYED(self, card):
		if card.type == CardType.SPELL:
			self.buff(self, "EX1_055o")


# Sunfury Protector
class EX1_058:
	def action(self):
		for minion in self.adjacentMinions:
			minion.taunt = True


# Crazed Alchemist
class EX1_059:
	action = buffTarget("EX1_059e")

class EX1_059e:
	def apply(self, target):
		atk = target.atk
		self.setAtk(target.health)
		self.setHealth(atk)


# Pint-Sized Summoner
class EX1_076:
	class Aura:
		Name = "Pint-Sized Summoner Virtual Aura"
		targeting = TARGET_FRIENDLY_HAND
		Cost = -1
		def isValidTarget(self, target):
			return not self.controller.minionsPlayedThisTurn


# Secretkeeper
class EX1_080:
	def CARD_PLAYED(self, card):
		if card.tags.get(GameTag.SECRET):
			self.buff(self, "EX1_080e")


# Mind Control Tech
class EX1_085:
	def action(self):
		if len(self.controller.opponent.field) >= 4:
			self.controller.takeControl(random.choice(self.controller.opponent.field))


# Arcane Golem
class EX1_089:
	def action(self):
		self.controller.opponent.maxMana += 1


# Defender of Argus
class EX1_093:
	def action(self):
		for target in self.adjacentMinions:
			self.buff(target, "EX1_093e")


# Gadgetzan Auctioneer
class EX1_095:
	def OWN_CARD_PLAYED(self, card):
		if card.type == CardType.SPELL:
			self.controller.draw()


# Abomination
class EX1_097:
	def deathrattle(self):
		for target in self.controller.getTargets(TARGET_ALL_CHARACTERS):
			self.hit(target, 2)


# Coldlight Seer
class EX1_103:
	def action(self):
		for minion in self.controller.field:
			if minion.race == Race.MURLOC:
				self.buff(minion, "EX1_103e")


# Azure Drake
class EX1_284:
	action = drawCard


# Murloc Tidecaller
class EX1_509:
	def MINION_SUMMON(self, player, minion):
		if minion.race == Race.MURLOC and minion != self:
			# NOTE: We have to check against ourselves here because the
			# Battlecry happens when we are already in play
			self.buff(self, "EX1_509e")


# Ancient Mage
class EX1_584:
	def action(self):
		for target in self.adjacentMinions:
			self.buff(target, "EX1_584e")


# Imp Master
class EX1_597:
	def OWN_TURN_END(self):
		self.hit(self, 1)
		self.controller.summon("EX1_598")


# Mana Wraith
class EX1_616:
	class Aura:
		Name = "Mana Wraith Virtual Aura"
		targeting = TARGET_ANY_HAND
		Cost = 1
		def isValidTarget(self, target):
			return target.type == CardType.MINION


# Knife Juggler
class NEW1_019:
	def OWN_MINION_SUMMON(self, minion):
		self.hit(random.choice(self.controller.getTargets(TARGET_ALL_ENEMY_CHARACTERS)), 1)


# Wild Pyromancer
class NEW1_020:
	def AFTER_OWN_CARD_PLAYED(self, card):
		if card.type == CardType.SPELL:
			for target in self.controller.getTargets(TARGET_ALL_MINIONS):
				self.hit(target, 1)


# Bloodsail Corsair
class NEW1_025:
	def action(self):
		weapon = self.controller.opponent.hero.weapon
		if self.controller.opponent.hero.weapon:
			weapon.durability -= 1


# Violet Teacher
class NEW1_026:
	def OWN_CARD_PLAYED(self, card):
		if card.type == CardType.SPELL:
			self.controller.summon("NEW1_026t")


# Master Swordsmith
class NEW1_037:
	def OWN_TURN_END(self):
		other_minions = [t for t in self.controller.field if t is not self]
		if other_minions:
			target = random.choice(other_minions)
			self.buff(target, "NEW1_037e")


# Stampeding Kodo
class NEW1_041:
	def action(self):
		targets = [t for t in self.controller.opponent.field if t.atk <= 2]
		if targets:
			random.choice(targets).destroy()
