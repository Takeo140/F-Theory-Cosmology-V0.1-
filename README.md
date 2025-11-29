# F-Theory Cosmological Physics: Expansion Simulation (V0.1)

This project serves as a conceptual starting point for simulating the universe's expansion, based on the **Obverse-Reverse Model** presented in the associated F-Theory Cosmological Physics paper.

[cite_start]The implementation numerically solves the **Friedmann Equations** (Reverse) [cite: 25, 26][cite_start], which are derived from the **Extremal Principle** (Axiom 1) [cite: 11][cite_start], using the density parameters for matter and dark energy (Obverse) [cite: 15, 27] to calculate the time evolution of the scale factor $a(t)$.

## Requirements

* Python 3.9+
* NumPy
* SciPy
* Matplotlib

## How to Run

1.  Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```
2.  Execute the main script:
    ```bash
    python src/main_expansion.py
    ```
3.  A graph showing the evolution of the scale factor $a(t)$ will be generated.
