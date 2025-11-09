# examples/run_all.py
"""
Batch Run of Moth-Flame Optimization Algorithm
==============================================
This script runs the MFO algorithm on all available fitness functions
(both 2D and N-dimensional) and saves reports and convergence plots.
"""

from pathlib import Path
from mfo_algorithm.mfo import MFO
from mfo_algorithm.fitnessfunctions import FitnessFunctions

def main():
    output_dir = Path("reports")
    plot_dir = Path("plots")
    output_dir.mkdir(parents=True, exist_ok=True)
    plot_dir.mkdir(parents=True, exist_ok=True)

    ff_obj = FitnessFunctions()
    
    # Get all fitness functions
    all_funcs = ff_obj.get_functions_name()

    for func_name in all_funcs:
        # Determine the dimension automatically
        func_meta = ff_obj.args(func_name)
        dimension = func_meta['dim']
        if dimension == 0:
            # N-D function, assign default dimension if not specified
            dimension = 5

        print(f"\nRunning MFO on '{func_name}' (dimension={dimension})...")

        mfo = MFO(
            max_iteration=50,
            number_of_moths=30,
            fitnessfunction=func_name,
            dimension=dimension
        )

        # Start optimization
        mfo.start()

        # Save report
        header, report = mfo.get_report()
        report_file = output_dir / f"{func_name}_report.txt"
        with report_file.open("w") as f:
            f.write(f"Moth-Flame Optimization Report\n\n")
            f.write(f"Fitness Function: {func_name}\n")
            f.write(f"Dimension: {dimension}\n")
            f.write(f"Number of Iterations: 50\n")
            f.write(f"Number of Moths: 30\n")
            f.write("\nBest moth's score and position in each iteration:\n")
            for r in report:
                f.write(f"{r}\n")
        print(f"Report saved to {report_file.resolve()}")

        # Save convergence plot
        mfo.draw_the_plot(plot_dir, f"{func_name}_convergence")
        print(f"Convergence plot saved to {plot_dir / (func_name + '_convergence.png')}")

if __name__ == "__main__":
    main()
