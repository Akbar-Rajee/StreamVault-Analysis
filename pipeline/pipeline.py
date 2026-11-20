import subprocess

steps = [
    "src/transform_data.py",
    "src/extract_directors.py",
    "src/extract_actors.py",
    "src/run_analysis.py",
]

for step in steps:
    print(f"\nRunning {step}")
    subprocess.run(["python", step], check=True)

print("\nPipeline completed successfully.")