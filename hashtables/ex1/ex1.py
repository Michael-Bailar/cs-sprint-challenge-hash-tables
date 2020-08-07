def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    weight_list_cache = {}

    for i in range(length):
        comparison_value = limit - weights[i]
        if comparison_value in weight_list_cache:
            complement = weight_list_cache[comparison_value]
            answer = (i, complement)
            return answer

        else:
            weight_list_cache[weights[i]] = i

    return None
    # for weight in weights:
    #     weight_list_cache[weight] = limit - weight
    # print(weight_list_cache)

    # for weight in weights:
    #     if weight_list_cache[weight] in weights:
    #         answer = ( weights.index(limit - weight), weights.index(weight))
    #         return answer

if __name__ == '__main__':
    weights_2 = [4, 4]
    answer_2 = get_indices_of_item_weights(weights_2, 2, 8)
    print(answer_2)