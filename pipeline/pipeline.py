import subprocess
import sys

STEPS = [
    "src/transform_data.py",
    "src/extract_directors.py",
    "src/extract_actors.py",
    "tests/validation_checks.py",
    "src/franchise_rankings.py",
    "src/top_standalones.py",
    "src/director_analysis.py",
    "src/actor_analysis.py"
]

for step in STEPS:

    print(f"Running {step}")

    subprocess.run(
        [sys.executable, step],
        check=True
    )

print("\nPipeline completed successfully.")