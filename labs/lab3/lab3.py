"""
Name: Sean Faust
Lab3.py

Problem: This lab takes inputs of the numbers of days a car counter was installed and how many
vehicles used the road and outputs the total number of cars that used the road on certain days and
how many cars used the road on average.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def traffic():
    total_cars = 0
    roads = eval(input("How many roads were surveyed?"))
    for i in range(1, roads + 1):
        total_day_cars = 0
        print("How many days was road", i, "surveyed?")
        days = eval(input(""))
        for j in range(1, days + 1):
            print("How many cars used the road on day", j, "?")
            total_day_cars += eval(input(""))
            avg_cars = total_day_cars / days
        total_cars += total_day_cars
        print("The average amount of cars that used road", i, "was:", avg_cars)
    print("The total number of cars using the roads was", total_cars)
    avg_c_road = total_cars / roads
    print("The average number of cars per road was:", round(avg_c_road, 2))

