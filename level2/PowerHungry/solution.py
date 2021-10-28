# Python 2.7.13
# level2 - Power Hungry
# https://github.com/Romansko/Foobar/blob/main/level2/PowerHungry/solution.py

def solution(xs):
    if not xs or type(xs) is not list:
        return str(0)

    # This shit took me 1 hour to detect. if xs is a single negative element, return that element and not 0.
    if len(xs) == 1:
        return str(xs[0])

    # Build positive and negative numbers list
    posList = filter(lambda x: x > 0, xs)
    negList = filter(lambda x: x < 0, xs)

    # remove first occurrence of unproductive odd number if negative list is odd.
    if len(negList) % 2:
        negList.remove(max(negList))

    # empty lists.. (check after possible removal of negative item).
    if (len(posList) == 0) and (len(negList) == 0):
        return str(0)

    # calculate product and return as string
    product = 1
    for n in posList:
        product *= n
    for n in negList:
        product *= n
    return str(product)  # required str on return


if __name__ == '__main__':
    # Some tests
    tests = [
        [[2, 0, 2, 2, 0], str(8)],
        [[-2, -3, 4, -5], str(60)],
        [[1000] * 50, str(pow(1000, 50))],  # maximum values
        [[-1], str(-1)],
        [[-1, 0], str(0)],
        [[1], str(1)],
        [[0], str(0)],
        [[0, 0], str(0)],
        [[0, 0, -15], str(0)],
        [[-1, -1], str(1)],
        [[-1, -1, -1], str(1)],
        [[-1, -1, 1], str(1)],
        [[-1, 1, 1], str(1)],
        [[1, 1, 1], str(1)]
    ]
    for test, expected in tests:
        assert expected == solution(test)
    print("Tests done")
