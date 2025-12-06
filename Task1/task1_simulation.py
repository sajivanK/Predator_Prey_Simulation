# Task1/task1_simulation.py (Group B)

from shared.world import World
import csv
import matplotlib.pyplot as plt
import random
import os

# ---------------- Ensure output folders exist ---------------- #
os.makedirs("Task1/results_csv/GroupB", exist_ok=True)
os.makedirs("Task1/plots/GroupB", exist_ok=True)

# ---------------- Simulation Settings (Group B) ---------------- #

WORLD_SIZE = 50
TIME_STEPS = 80
INITIAL_PREY = 60
INITIAL_PREDATORS = 30

# ------------------------------------------------------ #

def run_simulation(run_id):
    world = World(size=WORLD_SIZE)

    # spawn initial prey
    for _ in range(INITIAL_PREY):
        x, y = random.randint(0, WORLD_SIZE-1), random.randint(0, WORLD_SIZE-1)
        world.add_prey(x, y)

    # spawn initial predators
    for _ in range(INITIAL_PREDATORS):
        x, y = random.randint(0, WORLD_SIZE-1), random.randint(0, WORLD_SIZE-1)
        world.add_predator(x, y, energy=5)

    prey_count_history = []
    predator_count_history = []

    for step in range(TIME_STEPS):
        world.step()
        prey_count, predator_count = world.count()
        prey_count_history.append(prey_count)
        predator_count_history.append(predator_count)
        print(f"Group B - Run {run_id} - Step {step}: Prey={prey_count}, Predators={predator_count}")

    # Save CSV
    csv_file = f"Task1/results_csv/GroupB/runB{run_id}.csv"
    with open(csv_file, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Step", "Prey", "Predator"])
        for i in range(TIME_STEPS):
            writer.writerow([i, prey_count_history[i], predator_count_history[i]])

    # Plot
    plt.figure()
    plt.plot(prey_count_history, label="Prey")
    plt.plot(predator_count_history, label="Predator")
    plt.xlabel("Time Step")
    plt.ylabel("Population")
    plt.title(f"Task 1 - Group B Run {run_id}")
    plt.legend()
    plt.savefig(f"Task1/plots/GroupB/runB{run_id}_plot.png")
    plt.close()


# ---------------- Run 3 simulations for Group B ---------------- #

for run in range(1, 4):
    run_simulation(run)

print("Group B simulations completed!")
