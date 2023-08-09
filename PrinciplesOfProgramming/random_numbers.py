from random import randint
def print_random(num_cnt):
    temp_cnt = 0
    while num_cnt != temp_cnt:
        temp_cnt += 1
        print(f"number {temp_cnt} : {randint(1,10)}")



print_random(3)