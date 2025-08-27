# 2x2-rubik-solver-python
Basic 2x2 Rubik's cube solver built in Python using Tkinter

## OVERVIEW
This project is a Python based 2x2 Rubik's Cube solver that utilises modular programming and a Tkinter based GUI. It takes the cube's initial configuration as input, computes the solution using pre-defined algorithms and outputs the sequence of moves required to solve the cube efficiently.

## FEATURES
* **Modular structure:** Separate python files handle cube intialisation, move definitions and solving logic.
* **Tkinter GUI:** Interactive interface to input cube states and visulaise the solution in 2D.
* **Optimised solving algorithm:** Implements logic for efficient solution generation
* **Readable code structure:** Easily extensible for future improvements

## PROJECT STRUCTURE
```text
project/
├── 02-10_integrated_final.py
├── cubesolve.py
├── initialstatecube.py
├──finalstatecube.py
├──movesmodule.py
└── __pycache__/
```

## INSTALLATION & USAGE
**Clone the repository:**
```bash
git clone https://github.com/TanishkaSridhar/2x2-rubik-solver-python.git
cd 2x2-rubik-solver-python
```

**Install dependencies:**
```bash
pip install -r pytwisty
```

**1. Run the solver:**
```bash
python 02-10_integrated_final.py
```

**2. Input the cube state** through the GUI and click **solve**

**3.** The application will **display the optimal sequence of moves** to solve the cube.

## LICENSE
This project is licenced under the [MIT License](LICENSE)

## FUTURE IMPROVEMENTS
* Extended solver for 3x3 cubes.
* Enhance GUI with real-time 3D cube visualisation.
* Implement heuristic algorithms for faster solutions.