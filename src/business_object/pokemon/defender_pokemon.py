from business_object.pokemon.abstract_pokemon import AbstractPokemon


class DefenderPokemon(AbstractPokemon):
    """
    Pokemon Attacker type
    """

    def get_pokemon_attack_coef(self) -> float:
        """
        Compute a damage multiplier related to the Defender type.

        Returns :
            float : the multiplier
        """
        multiplier = 1 + (self.speed_current + self.defense_current) / 200
        return multiplier
