def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    #
    result = None
    limit_diff = {}

    # Populate [weight] = limit - weight
    for index, weight in enumerate(weights):
        if weight not in limit_diff:
            limit_diff[weight] = (index, limit - weight)

    for key, value in limit_diff.items():
        diff = value[1]
        if diff in weights:
            diff_index = limit_diff[diff][0]
            if diff_index == value[0]:
                diff_index = weights[diff_index + 1:].index(diff) + diff_index + 1
                if diff_index == None: continue
            result = (diff_index, value[0])
            break

    return result

weights_2 = [4, 4]
answer_2 = get_indices_of_item_weights(weights_2, 2, 8)
print(answer_2)
