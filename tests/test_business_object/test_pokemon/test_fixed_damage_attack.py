from business_object.pokemon.fixed_damage_attack import FixedDamageAttack


class TestFixedDamageAttack:
    def test_compute_damage(self):
        # GIVEN
        attack = FixedDamageAttack(150, "jade", "PokemonAttaque")

        # WHEN
        power = attack.compute_damage(200, 200)

        # THEN
        assert power == attack.power


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
