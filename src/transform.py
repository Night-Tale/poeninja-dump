def build_item_index(data):
	items = data.get("items")
	return {item["id"]: item['name'] for item in items}


def extract_currency_list(data, source):
	lines = data.get("lines", [])
	id_to_name = build_item_index(data)

	currency_list = []

	for line in lines:
		cid = line.get("id")
		name = id_to_name.get(cid, cid)
		value_divine = float(line['primaryValue'])
		currency_list.append((source, name, value_divine))

	return currency_list


def transform_to_rows(currency_list):
	rows: list[list[str]] = [['Source', 'Currency', 'Divine Value']]
	for source, name, value in currency_list:
		rows.append([source, name, str(value).replace('.', ',')])

	return rows
