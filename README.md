# 🐺 Predator–Prey Simulation (Agent-Based Modeling)

This project simulates ecological predator–prey interactions using an Agent-Based Model (ABM). The system consists of predators and prey interacting in a toroidal 50×50 grid world, where populations evolve over discrete time steps based on movement rules, sensing, reproduction, and energy requirements.

The simulation is divided into three tasks to analyse how different parameter settings and new ecological rules impact population stability.

## 📌 Features
- Predator and prey as autonomous agents
- Predator energy and starvation behaviour
- Prey escape and reproduction logic
- Toroidal (wrap-around) world
- Parameter adjustments and new rules in Task 2 & 3
- Output saved as CSV datasets + plotted results


## 🧪 Experiment Groups

| Task | Group | Description | Output |
|------|------|-------------|--------|
| 1 | A & B | Initial model tests with two different initial populations | CSV + plots |
| 2 | C & D | Adjusted parameters to improve predator survival | CSV + plots |
| 3 | E & F | New rule: prey natural mortality + predator sensing boost | CSV + plots |

## ▶️ How to Run

Install dependency:
pip install matplotlib

Run experiment scripts:
python3 -m Task1.task1_simulation
python3 -m Task2.task2_simulation
python3 -m Task3.task3_simulation

All results will be saved into each task folder under:
- results_csv/
- plots/

## 📊 Example Output
Population graphs show:
- Predators often go extinct early in baseline model
- Improved survival with adjustments in later tasks
- Prey growth slows but still dominates long-term

(Plots included in repository folders)

## 👨‍💻 Technologies Used
- Python (Object-Oriented Programming)
- Matplotlib for visualization
- Agent-Based Modelling principles

## 🧑‍🎓 Author
Name: Sajivan Kunarethinam  
Student ID: IT23172296  

## 📈 Future Enhancements
- Introduce vegetation (three-level food chain)
- Carrying capacity and limited resources
- Smarter adaptive predator movement
- Multi-species expansions for more complex ecology

⭐ If you like this project, please consider starring the repository!
