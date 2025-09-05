from business_object.pokemon.abstract_pokemon import AbstractPokemon


class AttackerPokemon(AbstractPokemon):
    """
        Pokemon Attacker type
    """
    # def __init__(self, speed_current, attack_current): implicitement hérité
    #     super().__init__()

    def get_pokemon_attack_coef(self) -> float:
        """
        Compute a damage multiplier related to the Attacker type.

        Returns :
            float : the multiplier
        """
        multiplier = 1 + (self.speed_current + self.attack_current) / 200
        return multiplier
