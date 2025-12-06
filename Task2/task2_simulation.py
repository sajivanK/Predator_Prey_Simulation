# Task2/task2_simulation.py (Group C/D - Reduced Prey Reproduction)

from shared.world import World
import csv
import matplotlib.pyplot as plt
import random
import os

# ---------------- Ensure output folders exist ---------------- #
os.makedirs("Task2/results_csv/GroupD", exist_ok=True)
os.makedirs("Task2/plots/GroupD", exist_ok=True)

# ---------------- Simulation Settings (Task 2 Group C) ---------------- #

WORLD_SIZE = 50
TIME_STEPS = 80
INITIAL_PREY = 80
INITIAL_PREDATORS = 20

# ------------------------------------------------------ #

def run_simulation(run_id):
    world = World(size=WORLD_SIZE)

    # randomly place initial prey
    for _ in range(INITIAL_PREY):
        x, y = random.randint(0, WORLD_SIZE-1), random.randint(0, WORLD_SIZE-1)
        world.add_prey(x, y)

    # randomly place initial predators
    for _ in range(INITIAL_PREDATORS):
        x, y = random.randint(0, WORLD_SIZE-1), random.randint(0, WORLD_SIZE-1)
        world.add_predator(x, y, energy=5)

    prey_count_history = []
    predator_count_history = []

    # ---------------- Simulation Loop ---------------- #

    for step in range(TIME_STEPS):
        world.step()
        prey_count, predator_count = world.count()
        prey_count_history.append(prey_count)
        predator_count_history.append(predator_count)
        print(f"Group D - Run {run_id} - Step {step}: Prey={prey_count}, Predators={predator_count}")

    # Save CSV
    csv_file = f"Task2/results_csv/GroupD/runC{run_id}.csv"
    with open(csv_file, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Step", "Prey", "Predator"])
        for i in range(TIME_STEPS):
            writer.writerow([i, prey_count_history[i], predator_count_history[i]])

    # Save Plot
    plt.figure()
    plt.plot(prey_count_history, label="Prey")
    plt.plot(predator_count_history, label="Predator")
    plt.xlabel("Time Step")
    plt.ylabel("Population")
    plt.title(f"Task 2 - Group C Run {run_id}")
    plt.legend()
    plt.savefig(f"Task2/plots/GroupD/runC{run_id}_plot.png")
    plt.close()


# ---------------- Run 3 simulations for Group C ---------------- #

for run in range(1, 4):
    run_simulation(run)

print("Task 2 - Group D simulations completed!")
