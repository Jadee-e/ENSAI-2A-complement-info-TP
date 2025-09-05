from business_object.pokemon.abstract_pokemon import AbstractPokemon


class AllRounderPokemon(AbstractPokemon):
    """
    Pokemon AllRounder type
    """
       
    def get_pokemon_attack_coef(self) -> float:
        """
        Compute a damage multiplier related to the AllRounder type.

        Returns :
            float : the multiplier
        """
        multiplier = 1 + (self.sp_atk_current + self.sp_def_current) / 200
        return multiplier
