from business_object.pokemon.abstract_attack import AbstractAttack 
import random as rd


class AbstractFormulaAttack(AbstractAttack):
    """
    """

    def compute_damage(self, APkm1, APkm2):
        attack = APkm1.get_attack_stat(APkm1)
        defense = APkm2.get_defense_stat(APkm2)
        random = rd.randfoat(0.85, 1.0)
        level = APkm1.level
        power = self.power
        damage = ((2*level/5+2)*power*attack/(defense*50) + 2)*random
        return damage
