# Daily Temperatures
# You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.

# Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. 
# If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.


def daily_temps(temperatures):
    days_holder = []

    for current_day in range(len(temperatures)):
        hotter_day = current_day
        while hotter_day <= len(temperatures) - 1:
            if temperatures[hotter_day] > temperatures[current_day]:
                days_holder.append(hotter_day - current_day)
                break
            else:
                hotter_day += 1

    return days_holder


# print(daily_temps([73,74,75,71,69,72,76,73]))
# print(daily_temps([30,40,50,60]))


def daily_temperatures(temps):
    result = [0] * len(temps)
    stack = [] # pair [temp, index]

    for index, value in enumerate(temps):
        while stack and value > stack[-1][0]:
            stack_temperature, stack_index = stack.pop()
            result[stack_index] = index - stack_index
        stack.append([value, index])
    return result

print(daily_temperatures([73,74,75,71,69,72,76,73]))
print(daily_temperatures([30,40,50,60]))