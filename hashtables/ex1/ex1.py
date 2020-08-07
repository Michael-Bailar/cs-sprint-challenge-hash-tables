def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    weight_list_cache = {}
    for i in range(length):
        weight_list_cache[weights[i]] = i
    print(weight_list_cache)
    print(weights)
    weight_counter = 0
    for item in weight_list_cache.items():

        print(limit, item[0], limit - weights[weight_counter], end=": ")
        print(limit - weights[weight_counter])
        weight_counter += 1
    #print(weight_list_cache[15])
    
    return None
