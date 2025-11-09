"""
Example Run of Moth-Flame Optimization Algorithm
================================================
This script demonstrates how to run the MFO algorithm programmatically.
"""

from mfo_algorithm.mfo import MFO

def main():
    # Example parameters
    fitness_function_name = "sphere"
    max_iterations = 50
    number_of_moths = 30

    # Initialize MFO
    mfo = MFO(
        max_iteration=max_iterations,
        number_of_moths=number_of_moths,
        fitnessfunction=fitness_function_name
    )

    # Start optimization
    mfo.start()

    # Get report
    header, report = mfo.get_report()

    # Print final best score
    best_score = report[-1][0]
    print(f"Best score after {max_iterations} iterations: {best_score}")

    # Optionally, draw convergence plot
    mfo.draw_the_plot("plots", f"{fitness_function_name}_convergence_example")


if __name__ == "__main__":
    main()
