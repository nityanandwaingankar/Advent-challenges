def myfunc():
    # print("Hello from myfunc")
    l1 = []
    l2 = []
    while True:
        val = input()
        # print(val)
        if val:
            # print("End of input")
            l1.append(val.split()[0])
            l2.append(val.split()[1])
        else:
            break
    l1.sort()
    l2.sort()

    dist = 0
    # assuming l1 and l2 are of same length
    for i in range(len(l1)):
        ct = 0
        for j in range(len(l2)):
            if int(l1[i]) == int(l2[j]):
                ct += 1
        # if l1[i] in l2:

        dist += int(l1[i]) * ct
    print(dist)


if __name__ == "__main__":
    myfunc()
