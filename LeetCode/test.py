def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    appl_cnt, org_cnt = 0, 0
    for x in range(0, len(apples)):
        apples[x] = apples[x] + a
        if apples[x] >= s and apples[x] <= t:
            appl_cnt += 1
    for x in range(0, len(oranges)):
        oranges[x] = oranges[x] + b
        if oranges[x] >= s and oranges[x] <= t:
            org_cnt += 1
    print(appl_cnt)
    print(org_cnt)



s = [86,30,0,16,51,53,42,48,22,69,12,27,34,24,95,16,32,22,52,56,71,95]
res = countApplesAndOranges(7,11, 5, 15, [-2,2, 1], [5,-6])


