import os
import yaml
from pathlib import Path

# Env
FUNC_PATH = os.environ.get("FUNC_PATH")
SUFFIX = os.environ.get("SUFFIX")
SLS_FUNC_PATH = os.environ.get("SLS_FUNC_PATH")
PREFIX = os.environ.get("PREFIX")

# Check for the existence of the file, if not, create it
export_file = Path("./export.yml")
export_file.touch(exist_ok=True)

# Create list
func_list = []
files = os.listdir(FUNC_PATH)
func_list = [f for f in files if os.path.isfile(os.path.join(FUNC_PATH, f))]

# Create YAML
with open(r"export.yml", "w") as f:
    for func_name in func_list:
        func_name = func_name.removesuffix(SUFFIX)
        func_name_lower_camelcase = func_name
        func_name_upper_camelcase = func_name[0].upper() + func_name[1:]
        
        handler_pass = f"{SLS_FUNC_PATH}" + func_name_lower_camelcase + ".handler"
        func_name_all = f"{PREFIX}" + func_name_upper_camelcase

        data = {
            func_name_upper_camelcase: {
                "handler": handler_pass,
                "memorySize": 1024,
                "name": func_name_all,
                "timeout": 30,
            }
        }
        yaml.dump(data, f)
        f.write("\n")
