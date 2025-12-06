
"""# Task3/task3_simulation.py (Group E - Natural Prey Mortality)

from shared.world import World
import csv
import matplotlib.pyplot as plt
import random
import os

# ---------------- Ensure output folders exist ---------------- #
os.makedirs("Task3/results_csv", exist_ok=True)
os.makedirs("Task3/plots", exist_ok=True)

# ---------------- Simulation Settings (Task 3 Group E) ---------------- #

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
        prey, pred = world.count()
        prey_count_history.append(prey)
        predator_count_history.append(pred)
        print(f"Task 3 - Run {run_id} - Step {step}: Prey={prey}, Predators={pred}")

    # Save CSV results
    csv_file = f"Task3/results_csv/runE{run_id}.csv"
    with open(csv_file, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Step", "Prey", "Predator"])
        for i in range(TIME_STEPS):
            writer.writerow([i, prey_count_history[i], predator_count_history[i]])

    # Save plot
    plt.figure()
    plt.plot(prey_count_history, label="Prey")
    plt.plot(predator_count_history, label="Predator")
    plt.xlabel("Time Step")
    plt.ylabel("Population")
    plt.title(f"Task 3 - Group E Run {run_id}")
    plt.legend()
    plt.savefig(f"Task3/plots/runE{run_id}_plot.png")
    plt.close()


# ---------------- Run 3 simulations for Group E ---------------- #

for run in range(1, 4):
    run_simulation(run)

print("Task 3 - Group E simulations completed!") """

# Task3/task3_simulation.py (Group F - Increased Predator Sensing Range)

from shared.world import World
import csv
import matplotlib.pyplot as plt
import random
import os

# ---------------- Ensure output folders exist ---------------- #
os.makedirs("Task3/results_csv/GroupF", exist_ok=True)
os.makedirs("Task3/plots/GroupF", exist_ok=True)

# ---------------- Simulation Settings (Task 3 Group F) ---------------- #

WORLD_SIZE = 50
TIME_STEPS = 80
INITIAL_PREY = 80
INITIAL_PREDATORS = 20

# ------------------------------------------------------ #

def run_simulation(run_id):
    world = World(size=WORLD_SIZE)

    for _ in range(INITIAL_PREY):
        x = random.randint(0, WORLD_SIZE-1)
        y = random.randint(0, WORLD_SIZE-1)
        world.add_prey(x, y)

    for _ in range(INITIAL_PREDATORS):
        x = random.randint(0, WORLD_SIZE-1)
        y = random.randint(0, WORLD_SIZE-1)
        world.add_predator(x, y, energy=5)

    prey_history = []
    predator_history = []

    for step in range(TIME_STEPS):
        world.step()
        prey, pred = world.count()
        prey_history.append(prey)
        predator_history.append(pred)
        print(f"Group F - Run {run_id} - Step {step}: Prey={prey}, Predators={pred}")

    # Save CSV
    with open(f"Task3/results_csv/GroupF/runF{run_id}.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Step", "Prey", "Predator"])
        for i in range(TIME_STEPS):
            writer.writerow([i, prey_history[i], predator_history[i]])

    # Save Plot
    plt.figure()
    plt.plot(prey_history, label="Prey")
    plt.plot(predator_history, label="Predator")
    plt.xlabel("Time Step")
    plt.ylabel("Population")
    plt.title(f"Task 3 - Group F Run {run_id}")
    plt.legend()
    plt.savefig(f"Task3/plots/GroupF/runF{run_id}_plot.png")
    plt.close()


# ---------------- Run 3 simulations for Group F ---------------- #

for run in range(1, 4):
    run_simulation(run)

print("Task 3 - Group F simulations completed!")



