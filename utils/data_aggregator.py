def aggregate_data(first, second):
    sorted_second = sorted(second)
    result = []

    i = 0
    while i < len(sorted_second):
        current = sorted_second[i]
        indexes = [j for j in range(len(second)) if second[j] == current]
        total = sum(first[j] for j in indexes)
        result.append(total)
        i += len(indexes)

    return result
