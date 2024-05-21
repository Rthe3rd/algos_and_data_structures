# 853. Car Fleet
# There are n cars going to the same destination along a one-lane road. The destination is target miles away.

# You are given two integer array position and speed, both of length n, where position[i] is the position of the ith car and speed[i] is the speed of the ith car (in miles per hour).

# A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed. The faster car will slow down to match the slower car's speed. The distance between these two cars is ignored (i.e., they are assumed to have the same position).

# A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.

# If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

# Return the number of car fleets that will arrive at the destination.

def car_fleets(target, position, speed):
    times_to_reach_target = []
    time_counter = {}
    time_speed = list(zip(position, speed))

    # for index in range(len(position)):
    #     time_to_target = (target - position[index])/speed[index]
    #     if times_to_reach_target:
    #         for time in times_to_reach_target:
    #             if time > time_to_target and times_to_reach_target[index][1] > position[index]:
    #                 time_counter[time] += 1

    #     times_to_reach_target.append([time_to_target, position[index]])
    #     time_counter[time_to_target] = 1

    return time_speed



def car_fleet(target, position, speed):
    pair = [[p,s] for p,s in zip(position, speed)]
    stack = []
    for position, speed in sorted(pair)[::-1]: # Reverse sorted order
        stack.append((target - position) / speed)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
    return len(stack)

print(car_fleet(12, [10,8,0,5,3], [2,4,1,1,3]))
print(car_fleet(10, [6,8], [3,2]))