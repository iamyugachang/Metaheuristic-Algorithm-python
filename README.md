# Metaheuristic Algorithm Python

This repository contains implementations of various metaheuristic algorithms in Python. Metaheuristic algorithms are optimization techniques inspired by natural phenomena, used to solve complex optimization problems.

## Features

- Implementation of popular metaheuristic algorithms.
- Modular and extensible codebase for easy experimentation.
- Suitable for solving optimization problems in various domains.

## Algorithms Included

- Genetic Algorithm (GA)
- Particle Swarm Optimization (PSO)
- Simulated Annealing (SA)
- Ant Colony Optimization (ACO)
- Tabu Search (TS)
- Differential Evolution (DE)
- Harmony Search (HS)
- Firefly Algorithm (FA)
- Artificial Bee Colony (ABC)
- Grey Wolf Optimizer (GWO)
- Whale Optimization Algorithm (WOA)
- Cuckoo Search (CS)
- Bat Algorithm (BA)
- And more...

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Metaheuristic-Algorithm-python.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Metaheuristic-Algorithm-python
   ```
3. (Optional) Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Dependencies

The project uses the following Python libraries:
- `numpy` for numerical computations.
- `matplotlib` for visualizing results.
- `scipy` for optimization-related utilities.

Install them using:
```bash
pip install numpy matplotlib scipy
```

## Usage

1. Choose the algorithm you want to use from the `algorithms` directory.
2. Customize the parameters in the respective script.
3. Run the script:
   ```bash
   python script_name.py
   ```

### Example

For example, to run the Genetic Algorithm:
```bash
python algorithms/genetic_algorithm.py
```

You can modify parameters like population size, mutation rate, and number of generations in the script.

## Future Work

- Add more metaheuristic algorithms such as Tabu Search and Differential Evolution.
- Improve visualization of optimization progress.
- Add benchmarking tools to compare algorithm performance.
- Create a user-friendly interface for parameter tuning.
