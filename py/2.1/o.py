hours = int(input())
minutes = int(input())
duration = int(input())
delivery_hours = (hours + (minutes + duration) // 60) % 24
delivery_minutes = (minutes + duration) % 60
print(f"{str(delivery_hours):0>2}:{str(delivery_minutes):0>2}")
