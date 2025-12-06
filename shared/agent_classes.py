# shared/agent_classes.py

import random

class Prey:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def sense_predator(self, world, distance=5):
        # Check north, south, east, west
        directions = [(0,-1),(0,1),(-1,0),(1,0)]
        for dx, dy in directions:
            for step in range(1, distance+1):
                nx = (self.x + dx*step) % world.size
                ny = (self.y + dy*step) % world.size
                if world.is_predator(nx, ny):
                    return True
        return False

    def move(self, world):
        # If predator nearby -> run away (later we improve this)
        if self.sense_predator(world):
            self.run_away(world)
        else:
            self.random_move(world)

    def random_move(self, world):
        moves = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        dx, dy = random.choice(moves)
        self.x = (self.x + dx) % world.size
        self.y = (self.y + dy) % world.size

    def run_away(self, world):
        # Simple version — choose random safe move for now
        self.random_move(world)


class Predator:
    def __init__(self, x, y, energy=5):
        self.x = x
        self.y = y
        self.energy = energy

    def sense_prey(self, world, distance=3):
        directions = [(0,-1),(0,1),(-1,0),(1,0)]
        for dx, dy in directions:
            for step in range(1, distance+1):
                nx = (self.x + dx*step) % world.size
                ny = (self.y + dy*step) % world.size
                if world.is_prey(nx, ny):
                    return (nx, ny)
        return None

    def move(self, world):
        target = self.sense_prey(world)
        if target:
            self.chase(target, world)
        else:
            self.random_move(world)

    def chase(self, target, world):
        tx, ty = target
        dx = 1 if tx > self.x else -1 if tx < self.x else 0
        dy = 1 if ty > self.y else -1 if ty < self.y else 0

        steps = random.choice([1,2])
        self.x = (self.x + dx * steps) % world.size
        self.y = (self.y + dy * steps) % world.size
        self.energy -= steps

    def random_move(self, world):
        moves = [(-1,0),(1,0),(0,-1),(0,1)]
        dx, dy = random.choice(moves)
        self.x = (self.x + dx) % world.size
        self.y = (self.y + dy) % world.size
        self.energy -= 1
