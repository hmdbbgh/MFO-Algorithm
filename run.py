import os
import sys
from typing import Tuple, List

import typer
from tabulate import tabulate

from Models.mfo import MFO
from Models.fitnessfunctions import FitnessFunctions

app = typer.Typer(help="Moth-Flame Optimization (MFO) Algorithm CLI")

REPORTS_DIR = os.path.join(os.getcwd(), "reports")


def _ensure_reports_dir() -> None:
    """Ensure the reports directory exists."""
    os.makedirs(REPORTS_DIR, exist_ok=True)


def _get_unique_report_path(report_name: str) -> str:
    """Return a unique path for the report."""
    path = os.path.join(REPORTS_DIR, report_name)
    if os.path.exists(path):
        typer.echo(f'Report "{report_name}" already exists!')
        sys.exit(1)
    os.makedirs(path)
    return path


def _write_report(
    header: List[str],
    report: List[List[float]],
    max_iteration: int,
    report_path: str,
    report_name: str,
    fitness_function_name: str,
    dimension: int,
    lb: float,
    ub: float,
    initial_positions,
) -> None:
    """Write the optimization report to a txt file."""
    file_path = os.path.join(report_path, f"{report_name}.txt")
    with open(file_path, "w") as f:
        f.write("Moth-Flame Optimization Algorithm Report\n\n\n")
        f.write(f"Fitness Function: {fitness_function_name}\n\n")
        f.write(f"Moth's Position Domain: [{lb}, {ub}]\n\n")
        f.write(f"Moth's Position Dimension: {dimension}-dimensional space\n\n")
        f.write(f"Number of Iterations: {max_iteration}\n\n\n")
        f.write("Initial Position of Moths\n")
        f.write(tabulate(initial_positions))
        f.write("\n\n\nBest moth's score and position in each iteration:\n")
        f.write(
            tabulate(
                report,
                headers=header,
                tablefmt="fancy_grid",
                showindex=range(1, max_iteration + 1),
                colalign=("center",) * (len(header) + 1),
            )
        )


@app.command()
def run(
    max_iteration: int = typer.Option(..., prompt=True, help="Max number of iterations"),
    number_of_moths: int = typer.Option(..., prompt=True, help="Number of moths"),
    fitness_function_id: int = typer.Option(..., prompt=True, help="ID of the fitness function"),
    dimension: int = typer.Option(None, help="Dimension for n-dimension functions"),
    report_name: str = typer.Option(..., prompt=True, help="Name for the report"),
):
    """
    Run the Moth-Flame Optimization Algorithm.
    """
    _ensure_reports_dir()
    report_path = _get_unique_report_path(report_name)

    ff_obj = FitnessFunctions()
    all_functions = ff_obj.get_functions_name()
    n_dimension_functions = ff_obj.get_n_dimension_functions_name()

    if not 1 <= fitness_function_id <= len(all_functions):
        typer.echo("Invalid fitness function ID!")
        sys.exit(1)

    fitness_function_name = all_functions[fitness_function_id - 1]

    # Initialize MFO
    if fitness_function_name in n_dimension_functions and dimension is None:
        typer.echo(f"Function {fitness_function_name} requires a dimension parameter!")
        sys.exit(1)

    mfo_obj = MFO(
        max_iteration=max_iteration,
        number_of_moths=number_of_moths,
        fitnessfunction=fitness_function_name,
        dimension=dimension if dimension else 0,
    )

    # Run optimization
    mfo_obj.start()

    # Write report and plot
    header, report = mfo_obj.get_report()
    initial_positions = mfo_obj.initial_position_of_moths

    mfo_obj.draw_plot(report_path, report_name)
    _write_report(
        header=header,
        report=report,
        max_iteration=max_iteration,
        report_path=report_path,
        report_name=report_name,
        fitness_function_name=fitness_function_name,
        dimension=mfo_obj.dimension,
        lb=mfo_obj.lower_bound[0],
        ub=mfo_obj.upper_bound[0],
        initial_positions=initial_positions,
    )

    typer.echo(f"SUCCESS! Check '{report_path}' for outputs.")


if __name__ == "__main__":
    app()
