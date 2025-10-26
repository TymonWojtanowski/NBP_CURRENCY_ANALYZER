import requests
import json

#NBP API URl for Table A (average exchange rates)
npb_api_url = "https://api.nbp.pl/api/exchangerates/tables/A?format=JSON"

try:
    response = requests.get(npb_api_url)
    response.raise_for_status()
    print("Connected to NPB")

    data_from_api = response.json()

# --- Step 3: Examine the structure of the fetched data ---
    print("\n--- Data Structure (Full Response) ---")
    # Use json.dumps for pretty printing with indentation
    # ensure_ascii=False is important for Polish characters in currency names
    print(json.dumps(data_from_api, indent=2, ensure_ascii=False))

    # Print only the effective date
    # Remember, the API returns a list [], we take the first element [0]
    effective_date = data_from_api[0]['effectiveDate']
    print(f"\n🗓 Effective Date: {effective_date}")

    # Print the list of rates (first 5 for readability)
    rates_list = data_from_api[0]['rates']
    print("\n--- Rates List (First 5) ---")
    # Use json.dumps for pretty printing
    print(json.dumps(rates_list[:5], indent=2, ensure_ascii=False))

    # Example iteration through the rates list
    print("\n--- Sample data from the list ---")
    if rates_list: # Check if the list is not empty
        first_currency = rates_list[0]
        currency_name = first_currency['currency']
        currency_code = first_currency['code']
        rate = first_currency['mid'] # 'mid' is the key for the average rate
        print(f"First currency: {currency_name} ({currency_code}), Rate: {rate}")

except requests.exceptions.RequestException as e:
    print(f" API connection error: {e}")
except (KeyError, IndexError) as e:
    print(f" Error in JSON data structure: Expected key or index not found. {e}")
    print("   Check if the API response structure has changed.")
except json.JSONDecodeError:
    print(" Error: Failed to decode JSON response. Check if the API is working correctly.")