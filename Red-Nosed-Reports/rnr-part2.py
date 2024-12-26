def myfunc():
    # print("Hello from myfunc")
    l1 = []
    while True:
        val = input()
        # print(val)
        if val:
            # print("End of input")
            l1.append(val.split())
        else:
            break
    # print("l1", l1)
    # print(len(l1), "l12222222222222222222")
    safe = set()
    l2=[]
    for i in l1:
        print(i, "i")
        ctl = 0
        ctr = 0
        for j in range(len(i) - 1):
            if int(i[j]) - int(i[j + 1]) >= -3 and int(i[j]) - int(i[j + 1]) <= -1:
                ctl += 1
            elif int(i[j]) - int(i[j + 1]) <= 3 and int(i[j]) - int(i[j + 1]) >= 1:
                ctr += 1
            else:
                break
        if ctl == (len(i) - 1) or ctr == (len(i) - 1):
            safe.add(tuple(i))
            continue
        else:
            for k in range(len(i)):
                ctl = 0
                ctr = 0
                cto = 0
                now = i[0:k] + i[k + 1 : len(i)]
                print("now", now)
                for j in range(len(now) - 1):
                    # while not found:
                    if (
                        int(now[j]) - int(now[j + 1]) >= -3
                        and int(now[j]) - int(now[j + 1]) <= -1
                    ):
                        print("ascending")
                        ctl += 1
                    elif (
                        int(now[j]) - int(now[j + 1]) <= 3
                        and int(now[j]) - int(now[j + 1]) >= 1
                    ):
                        print("descending")
                        ctr += 1
                    elif int(now[j]) - int(now[j + 1]) == 0:
                        print("stagnant")
                        cto += 1
                    # else:
                    #     continue

                if ctl == (len(now) - 1) or ctr == (len(now) - 1):
                    safe.add(tuple(now))
                    print("Now is safe", now)
                    break
                        # found = True

    print(len(safe))
    print((safe))







    # for i in l1:

    #     found = False





    # print(safe)
    # print(i[j])

    # dist = 0
    # # assuming l1 and l2 are of same length


# 77 84 81 84 81
# 40 43 45 42 38
# 58 61 64 71 73
# 54 58 61 62 65 68 68 74
# 7 8 11 14 18 21 23
# 13 10 9 8 7 6 6
# 38 41 39 37 34 30 29 26


if __name__ == "__main__":
    myfunc()
