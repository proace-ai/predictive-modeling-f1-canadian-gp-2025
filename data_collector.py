# data_collector.py

import fastf1
import pandas as pd

# Enable cache for FastF1
fastf1.Cache.enable_cache('./cache')


def get_canadian_gp_results(years):
    all_results = []

    for year in years:
        try:
            session = fastf1.get_session(year, 'Canadian Grand Prix', 'R')
            session.load()
            result = session.results[['DriverNumber', 'FullName', 'TeamName', 'Position', 'Time', 'Status']]
            result['Year'] = year
            all_results.append(result)
        except Exception as e:
            print(f"Error fetching data for {year}: {e}")

    combined_df = pd.concat(all_results, ignore_index=True)
    combined_df.to_csv("canadian_gp_history.csv", index=False)
    print("✅ Past Canadian GP results saved.")


def create_driver_profiles():
    # Updated full 2025 driver grid with attributes
    data = pd.read_json("2025_f1_driver_profiles.json")
    data.to_csv("driver_profiles.csv", index=False)
    print("✅ Full 2025 driver profiles saved.")


if __name__ == "__main__":
    get_canadian_gp_results([2019, 2022, 2023, 2024])
    create_driver_profiles()
