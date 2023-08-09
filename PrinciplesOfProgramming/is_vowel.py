def is_vowel(input_str):
    vowels = 'aeiou'
    result = False
    # if (len(input_str) != 0) and (input_str.lower() in vowels):
    #     result = True
    return (len(input_str) != 0) and (input_str.lower() in vowels)




opt = is_vowel("obama")
print(opt)