def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    return_list = []

    for i in range(len(a)):
        check = a[i]
        inverse = a[i] * -1
        # if check > -1:
        try:
            cache.get(cache[inverse])
            cache[check] = check
            return_list.append(abs(check))
        except KeyError:
            cache[check] = check
        cache[check] = check

    return return_list


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
