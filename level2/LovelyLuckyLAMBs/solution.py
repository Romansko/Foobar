# Python 2.7.13
# level2 - Lovely Lucky LAMBs
# https://github.com/Romansko/Foobar/blob/main/level2/LovelyLuckyLAMBs/solution.py

def generous(total_lambs):
    """ pay lambs generously. return payroll. assume total_lambs > 0. """
    payroll = []
    i = 0
    while True:   # main 2^i series construction loop
        lambs = pow(2, i)
        if lambs > total_lambs:
            break
        payroll.append(lambs)
        total_lambs -= lambs
        i += 1
    return payroll


def stingy(total_lambs):
    """ pay lambs stingily. return payroll. assume total_lambs > 0. """
    if total_lambs == 1:
        return [1]
    if total_lambs == 2:
        return [1, 1]
    payroll = [1, 1]
    total_lambs -= 2
    i = 2
    while True:    # main fibonacci series construction loop
        lambs = payroll[i - 1] + payroll[i - 2]
        if lambs > total_lambs:
            break
        payroll.append(lambs)
        total_lambs -= lambs
        i += 1
    return payroll


def solution(total_lambs):
    if (total_lambs <= 0) or (type(total_lambs) is not int):
        return 0
    return len(stingy(total_lambs)) - len(generous(total_lambs))


def validate(payroll):
    """ validate payroll list to comply with requirements. For testing only. """
    if not payroll:
        return False
    if payroll[0] != 1:  # Req1. X1 = 1.
        return False
    henchman = len(payroll)
    if henchman == 1:
        return True
    i = 0
    while i < (len(payroll) - 1):
        if payroll[i + 1] > 2 * payroll[i]:  # Req2. Xi+1 <= 2Xi.
            return False
        i += 1
    i = 0
    while i < (len(payroll) - 2):
        if payroll[i + 2] < payroll[i + 1] + payroll[i]:  # Req3. Xi+2 >= Xi+1 + Xi.
            return False
        i += 1
    return True


if __name__ == '__main__':
    # Some tests
    p = generous(143)
    print("generous 143", p)
    assert validate(p)
    p = stingy(143)
    print("stingy 143", p)
    assert validate(p)

    assert solution(143) == 3
    assert solution(10) == 1

