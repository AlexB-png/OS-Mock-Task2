import json

with open("src/HotelBookings.json", "r") as file:
    data = json.load(file)

for room in data.values():
    room["start_date"] = []
    room["end_date"] = []
    room["user_id"] = []

with open("src/HotelBookings.json", "w") as file:
    json.dump(data, file, indent=4)
