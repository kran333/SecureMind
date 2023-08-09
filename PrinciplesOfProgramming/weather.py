input_file = input("Input file? ")
# input_file = 'weather.txt'
alphabets = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ:)(! '

with open(input_file) as f_obj:
    data = f_obj.readlines()

# print(data)

updated_data_list = []
for element in data:
    temp = ''
    for ele in element:
        if ele not in alphabets:
            temp += ele
            # print(f"temp: '{temp}'")
        if (ele == ' ' or ele == '\n') and len(temp) >= 3:
            # print(f"ele: '{ele}'")
            temp = float(temp)
            updated_data_list.append(temp)
            # print(f"updated lis: {updated_data_list}")
            temp = ''

# print(updated_data_list)

for index in range(0, len(updated_data_list) - 1):
    index1 = updated_data_list[index+1]
    index2 = updated_data_list[index]
    diff = round(index1 - index2, 1)
    print(f"{updated_data_list[index]} to {updated_data_list[index+1]}, change = {diff}")

