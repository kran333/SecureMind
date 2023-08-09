from random import randint

def random_walk(stp_cnt):
    temp_cnt = 0
    max_num = 0
    totl_num = 0
    if stp_cnt >= 0:
        while stp_cnt != temp_cnt:
            temp_cnt += 1
            totl_num += randint(-1, 1)
            print(f"Position = {totl_num}")
            if totl_num > max_num:
                max_num = totl_num
        print(f"Finished after {stp_cnt} step(s)")
        print(f"Max position = {max_num}")

random_walk(7)




