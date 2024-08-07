import time
import subprocess
import os

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))
export_script_path = os.path.join(current_dir, 'export.py')

errors = []

for i in range(1, 1080):
    print(f"Running iteration {i}")
    result = subprocess.run(["python", export_script_path, str(i)])
    if result.returncode != 0:
        errors.append(i)

print(f"Errors encountered at pages: {errors}")