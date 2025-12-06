# shared/world.py

from shared.agent_classes import Prey, Predator
import random

class World:
    def __init__(self, size=50):
        self.size = size
        self.prey_list = []
        self.predator_list = []

    def add_prey(self, x, y):
        self.prey_list.append(Prey(x, y))

    def add_predator(self, x, y, energy=5):
        self.predator_list.append(Predator(x, y, energy))

    def is_prey(self, x, y):
        return any(p.x == x and p.y == y for p in self.prey_list)

    def is_predator(self, x, y):
        return any(pr.x == x and pr.y == y for pr in self.predator_list)

    # ---------------- Movement Phase ---------------- #

    def move_all(self):
        # Prey move first
        for prey in self.prey_list:
            prey.move(self)

        # Predators move after prey
        for predator in self.predator_list:
            predator.move(self)

    # ---------------- Eating Phase ---------------- #

    def eating_phase(self):
        for predator in self.predator_list[:]:
            for prey in self.prey_list[:]:
                if predator.x == prey.x and predator.y == prey.y:
                    self.prey_list.remove(prey)     # eat ONE prey
                    predator.energy += 8
                    break  # stop after 1 prey eaten

    # ---------------- Reproduction Phase ---------------- #

    def reproduction_phase(self):
        # Prey reproduction (15% chance)
        babies = []
        for prey in self.prey_list:
            if random.random() < 0.10:
                nx = (prey.x + random.randint(-1, 1)) % self.size
                ny = (prey.y + random.randint(-1, 1)) % self.size
                babies.append(Prey(nx, ny))
        self.prey_list.extend(babies)

        # Predator reproduction (energy >= 12)
        new_preds = []
        for predator in self.predator_list:
            if predator.energy >= 12:
                nx = (predator.x + random.randint(-1, 1)) % self.size
                ny = (predator.y + random.randint(-1, 1)) % self.size
                new_preds.append(Predator(nx, ny, energy=6))  # baby's initial energy
                predator.energy -= 6
        self.predator_list.extend(new_preds)

    # ---------------- One Simulation Step ---------------- #

    def step(self):
        self.move_all()

        # NEW: Predators lose 1 energy every timestep
        for predator in self.predator_list:
            predator.energy -= 1

        # Remove predators that starve before eating
        self.predator_list = [p for p in self.predator_list if p.energy > 0]

        # NEW: Natural prey death chance (2%)
        self.prey_list = [p for p in self.prey_list if random.random() > 0.02]


        self.eating_phase()
        self.reproduction_phase()

    def count(self):
        return len(self.prey_list), len(self.predator_list)
