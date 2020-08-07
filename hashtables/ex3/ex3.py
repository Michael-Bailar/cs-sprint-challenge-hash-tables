def intersection(arrays):
    """
    YOUR CODE HERE
    """
    cache = {}
    print_list = []

    for i in range(len(arrays)):
        cache[i] = {}
        for j in range(len(arrays[i])):
            cache[i][arrays[i][j]] = arrays[i][j]

    row = 1
    while row < len(arrays):
        for i in range(len(arrays[0])):
            try:
                value = cache[row].get(arrays[0][i])
                if value is not None and value not in print_list:
                    print_list.append(value)
            except KeyError:
                print("can't find")
        row += 1

    return print_list



if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
