
total_battery_capacity = 62 #kwh
energy_consumption_per_100km= 15.6 #kWh/100km


def vehicle_autonomy(battery_level):
    if  battery_level <= 0:
     battery_level=0

    if battery_level >100:
        battery_level = 100

    available_battery = total_battery_capacity * battery_level/100


    estimated_available_range = (available_battery * 100) / energy_consumption_per_100km
    
    return round(estimated_available_range, 2)

result = vehicle_autonomy(100)

print(result)

