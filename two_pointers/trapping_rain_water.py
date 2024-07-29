# Trapping Rain Water

# def trapping_rain_water(height):
#     current_height_index = 0
#     next_height_index = 1
#     total_volume = 0
#     sum_of_heights_seen = 0
#     while next_height_index < len(height):
#         if height[current_height_index] >= height[next_height_index]:
#             sum_of_heights_seen += height[next_height_index]
#             next_height_index += 1
#         else:
#             total_volume += (height[current_height_index] * (next_height_index - current_height_index - 1)) - sum_of_heights_seen
#             current_height_index = next_height_index
#             next_height_index += 1
#             sum_of_heights_seen = 0
#     return total_volume

def trapping_rain_water(height):
    local_max = 0
    left_max = [0]*len(height)
    right_max = [0]*len(height)
    for i in range(1, len(height)):
        local_max = max(local_max, height[i-1])
        left_max[i] = local_max
    
    local_max = 0
    for i in range(len(height) - 2, - 1, -1):
        local_max = max(local_max, height[i+1])
        right_max[i] = local_max
    
    rain_trapped = 0
    for i in range(len(height)):
        water = min(left_max[i], right_max[i]) - height[i]
        if water > 0:
            rain_trapped += water 

    return rain_trapped

# heights = [0,1,0,2,1,0,1,3,2,1,2,1]
heights = [4,2,0,3,2,5]
print(trapping_rain_water(heights)) 