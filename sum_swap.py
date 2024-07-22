
def findMinimumEqualSum(rowA, rowB):
    hash_table = {}
    sumA = 0
    sumB = 0

    for i, num in enumerate(rowA):
        sumA += num
        hash_table[num] = i

    for num in rowB:
        sumB += num

    shift_amount = abs((sumA - sumB)) // 2

    for i, num in rowB:

        if num + shift_amount in hash_table:
            return (num, num + shift_amount)
        elif num - shift_amount in hash_table:
            return (num, num - shift_amount)

    return -1


def minimumSum(rowA, rowB):
    sumA = sum(x for x in rowA if x != 0)
    sumB = sum(x for x in rowB if x != 0)

    zerosA = rowA.count(0)
    zerosB = rowB.count(0)

    if zerosA == zerosB:
        return max(sumA, sumB) if sumA == sumB else -1

    if (abs(sumA - sumB) % abs(zerosA - zerosB)) != 0:
        return -1

    return max(sumA, sumB) + (abs(sumA - sumB) // abs(zerosA - zerosB))
