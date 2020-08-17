def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    inter = {}

    for list in arrays:
        for num in list:
            if num not in inter:
                inter[num] = 1
            else:
                inter[num] += 1
                if inter[num] == len(arrays):
                    result.append(num)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
