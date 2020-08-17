def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []

    for num in a:
        if num < 0:
            if abs(num) in a:
                result.append(abs(num))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
