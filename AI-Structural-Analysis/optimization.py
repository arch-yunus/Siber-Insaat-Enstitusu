import numpy as np
from scipy.optimize import minimize

class BeamOptimizer:
    """
    Simplistic AI-driven Weight/Strength Optimizer for a 2D Beam.
    Goal: Minimize weight while keeping deflection under a limit.
    """
    def __init__(self, load, limit_deflection):
        self.load = load  # Applied vertical load (N)
        self.limit_deflection = limit_deflection

    def calculate_deflection(self, parameters):
        # parameters: [width, height, length]
        w, h, L = parameters
        E = 200e9 # Young's Modulus for Steel (Pa)
        I = (w * (h**3)) / 12  # Moment of Inertia
        deflection = (self.load * (L**3)) / (48 * E * I)
        return deflection

    def objective_function(self, parameters):
        # Weight (Volume * Density)
        w, h, L = parameters
        return w * h * L * 7850 # Steel density: 7850 kg/m3

    def constraint(self, parameters):
        # Deflection must be less than limit
        return self.limit_deflection - self.calculate_deflection(parameters)

    def optimize(self, initial_guess):
        cons = {'type': 'ineq', 'fun': self.constraint}
        res = minimize(self.objective_function, initial_guess, 
                       constraints=cons, bounds=[(0.01, 1.0), (0.01, 1.0), (1.0, 10.0)])
        return res

if __name__ == "__main__":
    opt = BeamOptimizer(load=5000, limit_deflection=0.005)
    initial_guess = [0.1, 0.1, 5.0]
    result = opt.optimize(initial_guess)
    print(f"Optimal Dimensions (w, h, L): {result.x}")
    print(f"Minimized Weight: {result.fun:.2f} kg")
