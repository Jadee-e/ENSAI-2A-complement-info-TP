from abc import ABC, abstractmethod


class AbstractAttack(ABC):
    """
    """
    def __init__(self, power, name, description):
        self.power = power
        self.name = name
        self.description = description

    @abstractmethod
    def compute_damage(self, APkm1, APkm2):
        pass
