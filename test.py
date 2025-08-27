import os
from pathlib import Path

env_file = Path('.env')
print(f".env file exists: {env_file.exists()}")
if env_file.exists():
    print(f".env file content:")
    print(env_file.read_text())