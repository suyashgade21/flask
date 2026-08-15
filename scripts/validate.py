import os
import sys


required_files = [
    "app/app.py",
    "tests/test_app.py",
    "requirements.txt"
]


print("Starting project validation...")

for file in required_files:
    if os.path.isfile(file):
        print(f"PASS: {file} exists")
    else:
        print(f"FAIL: {file} is missing")
        sys.exit(1)

print("Project validation successful!")
