import math

record_in_sek = float(input())
distance_in_meters = float(input())
time_in_sek = float(input())

climb = distance_in_meters * time_in_sek
climb_plus_time = (math.floor(distance_in_meters / 50)) * 30
total_time = climb + climb_plus_time

if record_in_sek <= total_time:
    diff = total_time - record_in_sek
    print(f"No! He was {diff:.2f} seconds slower.")
else:
    print(f"Yes! The new record is {total_time:.2f} seconds.")
