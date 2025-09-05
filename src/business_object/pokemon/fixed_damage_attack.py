from business_object.pokemon.abstract_attack import AbstractAttack


class FixedDamageAttack(AbstractAttack):
    """
    """
    def compute_damage(self, APkm1, APkm2):
        return self.power

    
