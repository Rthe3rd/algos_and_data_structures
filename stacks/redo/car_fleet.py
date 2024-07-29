def carFleet(target, position, speed):
    positions_speeds = [[p,s] for p,s in zip(position, speed)]
    car_fleet_times = []

    for postition, speed in sorted(positions_speeds)[::-1]:
        # add current cars time to the finish to the stack
        car_fleet_times.append((target - postition)/speed)
        if len(car_fleet_times) >= 2 and car_fleet_times[-1] <= car_fleet_times[-2]:
            car_fleet_times.pop()
    return len(car_fleet_times)

target1 = 12
position1 = [10,8,0,5,3]
speed1 = [2,4,1,1,3]

target2 = 10
position2 = [6,8]
speed2 = [3,2]

target3 = 100
position3 = [0,2,4]
speed3 = [4,2,1]

# print(carFleet(target1, position1, speed1))
print(carFleet(target2, position2, speed2))
# print(carFleet(target3, position3, speed3))