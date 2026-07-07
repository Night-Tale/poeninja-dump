from src.service_client import fetch_market_data
from src.transform import transform_to_rows
from src.sheets_client import clear_raw_data, write_raw_data


def main():
    currency_list = fetch_market_data()
    rows = transform_to_rows(currency_list)

    clear_raw_data()
    write_raw_data(rows)


if __name__ == "__main__":
    main()
