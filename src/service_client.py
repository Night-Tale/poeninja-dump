from src.transform import extract_currency_list
from src.config_loader import load_config

import requests

def fetch_poe2_endpoint(url: str, league: str, type_: str) -> dict:
	params = {
        "league": league,
        "type": type_,
        "value": 'divine',
    }
	resp = requests.get(url, params=params, timeout=10)
	resp.raise_for_status()
	return resp.json()


def fetch_market_data() -> list[dict]:
	config = load_config('config/api_config.yml')['poe2']
	url = config["url"]
	league = config["league"]
	items = []

	for endpoint in config["endpoints"]:
		name = endpoint["name"]
		params = endpoint["params"]

		data = fetch_poe2_endpoint(
			url=url,
			league=league,
			type_=params["type"],
        )
		items.extend(extract_currency_list(data, source=name))

	return items
