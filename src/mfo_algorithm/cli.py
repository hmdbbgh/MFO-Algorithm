# examples/run.py

"""
MFO Algorithm CLI
=================
Command-line interface to run Moth-Flame Optimization algorithm easily.
"""

from pathlib import Path
import typer
from typing import Optional

from mfo_algorithm.mfo import MFO
from mfo_algorithm.fitnessfunctions import FitnessFunctions
from tabulate import tabulate

app = typer.Typer(help="Moth-Flame Optimization (MFO) CLI")


def _validate_file_name(file_name: str, output_dir: Path) -> Path:
    """Ensure that the report file name does not already exist."""
    report_path = output_dir / f"{file_name}.txt"
    if report_path.exists():
        typer.echo(f'File "{report_path}" already exists in {output_dir}.')
        raise typer.Exit()
    return report_path


def _write_report(report_path: Path, fitness: str, iterations: int, moths: int, header: list, report: list):
    """Write MFO optimization report to a text file."""
    with report_path.open("w") as f:
        f.write(f"Moth-Flame Optimization Algorithm Report\n\n")
        f.write(f"Fitness Function: {fitness}\n")
        f.write(f"Number of Iterations: {iterations}\n")
        f.write(f"Number of Moths: {moths}\n\n")
        f.write("Best moth's score and position in each iteration:\n\n")
        f.write(tabulate(report, headers=header, tablefmt="fancy_grid", showindex=range(1, iterations + 1)))
    typer.echo(f"Report saved to {report_path.resolve()}")


@app.command()
def run(
    fitness: str = typer.Option(..., help="Fitness function name to optimize"),
    iterations: int = typer.Option(50, help="Maximum number of iterations"),
    moths: int = typer.Option(30, help="Number of moths"),
    dimension: Optional[int] = typer.Option(None, help="Dimension of the problem (required for N-dimensional functions)"),
    output: Path = typer.Option(Path("reports"), help="Directory to save reports")
) -> None:
    """
    Run the Moth-Flame Optimization algorithm with specified parameters.

    Args:
        fitness: Name of the fitness function to optimize.
        iterations: Maximum number of iterations.
        moths: Number of moths in the population.
        dimension: Problem dimension (required for N-dimensional functions).
        output: Directory to save reports and plots.

    Returns:
        None. Saves report and plot files to disk.
    """

    # Initialize fitness functions
    ff_obj = FitnessFunctions()
    all_fitness_names = ff_obj.get_functions_name()
    n_dimension_funcs = ff_obj.get_n_dimension_functions_name()

    if fitness not in all_fitness_names:
        typer.echo(f"Fitness function '{fitness}' not found. Available: {all_fitness_names}")
        raise typer.Exit()

    # Ensure output directory exists
    output.mkdir(parents=True, exist_ok=True)

    # Initialize MFO object
    if fitness in n_dimension_funcs:
        if dimension is None:
            typer.echo(f"Dimension must be specified for fitness function '{fitness}'")
            raise typer.Exit()
        mfo_obj = MFO(
            max_iteration=iterations,
            number_of_moths=moths,
            fitnessfunction=fitness,
            dimension=dimension
        )
    else:
        mfo_obj = MFO(
            max_iteration=iterations,
            number_of_moths=moths,
            fitnessfunction=fitness
        )

    typer.echo(f"Running MFO on '{fitness}' with {moths} moths for {iterations} iterations...")
    mfo_obj.start()

    # Prepare report
    header, report = mfo_obj.get_report()
    report_file_path = _validate_file_name(f"{fitness}_report", output)
    _write_report(report_file_path, fitness, iterations, moths, header, report)

    # Generate convergence plot
    plot_file_name = output / f"{fitness}_convergence.png"
    mfo_obj.draw_the_plot(output, f"{fitness}_convergence")
    typer.echo(f"Convergence plot saved to {plot_file_name.resolve()}")


if __name__ == "__main__":
    app()
