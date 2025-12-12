import os
import json

ENV_PATH = ".env"  # path to your local .env
    
def update_env_var(key, value):
    # read current .env
    lines = []
    if os.path.exists(ENV_PATH):
        with open(ENV_PATH, "r") as f:
            lines = f.readlines()

    # check if key exists
    key_exists = False
    for i, line in enumerate(lines):
        if line.startswith(f"{key}="):
            lines[i] = f'{key}={json.dumps(value)}\n'
            key_exists = True
            break

    if not key_exists:
        lines.append(f'{key}={json.dumps(value)}\n')

    with open(ENV_PATH, "w") as f:
        f.writelines(lines)