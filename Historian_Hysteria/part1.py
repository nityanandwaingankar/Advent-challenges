def myfunc():
    print("Hello from myfunc")
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
        dist += abs(int(l1[i]) - int(l2[i]))
    print(dist)


if __name__ == "__main__":
    myfunc()
