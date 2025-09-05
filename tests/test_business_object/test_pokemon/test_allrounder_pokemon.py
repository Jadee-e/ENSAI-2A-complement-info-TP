from business_object.pokemon.allrounder_pokemon import AllRounderPokemon
from business_object.statistic import Statistic


class TestAttackerPokemon:
    def test_get_coef_damage_type(self):
        # GIVEN
        snorlax = AllRounderPokemon(stat_current=Statistic(attack=100, defense=100))

        # WHEN
        multiplier = snorlax.get_pokemon_attack_coef()

        # THEN
        assert multiplier == 1.0


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
