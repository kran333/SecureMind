def pig_latin(input_file):
    vowels = ['a', 'e', 'i', 'o', 'u']
    f = open(input_file)
    txt_data = f.readlines()
    # print(txt_data)
    for lines in txt_data:
        if lines == '\n':
            print()
            continue
        lines = lines.replace('\n', '')
        lines_list = lines.split(" ")
        for word in lines_list:
            if word[0] in vowels:
                print(word + "yay ", end="")
            else:
                print(word[1:] + word[0] + "ay ", end="")
        print()




pig_latin("sample.txt")


