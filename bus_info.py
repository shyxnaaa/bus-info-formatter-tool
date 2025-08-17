import json

def format_bus_info(data_strings):
    buses = []
    for entry in data_strings:
        parts = [p.strip() for p in entry.split(",")]
        if len(parts) != 5:
            print(f"⚠️ Skipping invalid entry: {entry}")
            continue
        
        bus = {
            "BusNo": int(parts[0]),
            "Source": parts[1],
            "Destination": parts[2],
            "Time": parts[3],
            "Fare": int(parts[4])
        }
        buses.append(bus)
    return buses


if __name__ == "__main__":
    # Example: multiple entries
    input_data = [
        "202, Rohtak, Delhi, 8:45 AM, 50",
        "105, Panipat, Ambala, 10:00 AM, 60",
        "410, Chandigarh, Delhi, 6:15 PM, 75"
    ]
    
    formatted = format_bus_info(input_data)

    # Save to JSON
    with open("bus_info.json", "w", encoding="utf-8") as f:
        json.dump(formatted, f, indent=4, ensure_ascii=False)

    print("✅ Bus info saved to bus_info.json")
    print(json.dumps(formatted, indent=4))
