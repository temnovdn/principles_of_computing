def format_time(t):
    if t <= 9:
        A = '0'
        B = '0'
        C = '0'
    elif len(str(t)) == 2:
        A = '0'
        B = '0'
        C = (t // 10)
    else:
        A = (t // 600)
        t = (t % 600)
        if len(str(t)) == 3:
            B = ((t // 10) // 10)
            C = ((t // 10) % 10)
        elif len(str(t)) < 3:
            if t <= 59:
                B = '0'
                C = (t // 10)
            else:
                B = (((t % 60) // 10) % 10)
                C = (t // 10)
    D = (t % 10)
    return (((((str(A) + ':') + str(B)) + str(C)) + '.') + str(D))


TEST_CASES = [0, 30, 55, 400, 209, 600, 606, 630, 637, 676]

for case in TEST_CASES:
    print(format_time(case))

