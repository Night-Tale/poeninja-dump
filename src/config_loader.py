from pathlib import Path
import yaml

def load_config(path: str) -> dict:
	config_path = Path(path)
	with config_path.open("r", encoding="utf-8") as f:
		data = yaml.safe_load(f)
	if not isinstance(data, dict):
		raise ValueError("Config YAML должен содержать словарь на верхнем уровне.")
	return data