def floyds_triangle(k):
    if k <= 0:
        print('')
    else:
        num_cnt = 1
        for row in range(k + 1):
            for _ in range(row):
                print(f"{num_cnt} ", end="")
                num_cnt += 1
            print()

floyds_triangle(7)