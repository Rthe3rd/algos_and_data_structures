# Given a list of integers and a value k, find the k-most common integers

def kth_frequency(input_array, k=2):
    frequency_hash = {}
    for element in input_array:
        if element in frequency_hash:
            frequency_hash[element] += 1
        else:
            frequency_hash[element] = 1
    holder = [[]] * len(input_array)
    # for key, value in frequency_hash.items():
    #     if holder[value] == []:
    #         holder[value] = key
    #     else:
    #         holder[value] = [holder[value], key]
    # sorted([(item[1], item[0]) for item in dict_1.items()])
    sorted_frequencies = sorted([(item[0], item[1]) for item in frequency_hash.items()], reverse=False)
    kth_elements = []
    for i in range(k):
        kth_elements.append(sorted_frequencies[i][0])
    # for index in range(len(holder) - 1, 0, -1):
    #     if holder[index]:
    #         kth_elements.append(holder[index])
    
    return kth_elements


# print(kth_frequency([1,1,1,1,1,2,3,3,4,4,4,4,4]))
print(kth_frequency([1,1,1,2,2,3]))
