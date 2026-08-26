import subprocess
import sys


EXERCISES = [
    "ex0/ft_command_quest.py",
    "ex1/ft_score_analytics.py",
    "ex2/ft_coordinate_system.py",
    "ex3/ft_achievement_tracker.py",
    "ex4/ft_inventory_system.py",
    "ex5/ft_data_stream.py",
    "ex6/ft_data_alchemist.py",
]


def main() -> None:
    for exercise in EXERCISES:
        print(f"\n=== Running {exercise} ===", flush=True)
        result = subprocess.run([sys.executable, exercise])
        if result.returncode != 0:
            print(f"{exercise} finished with code {result.returncode}")


if __name__ == "__main__":
    main()
