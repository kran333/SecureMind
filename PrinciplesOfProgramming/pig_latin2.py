def pig_latin2_helper(input_text):
    vowels = 'aeiou'
    result = ''
    for letter in range(0, len(input_text)):
        if input_text[letter] in vowels:
            result = input_text[letter:] + input_text[:letter]
    return result

def pig_latin2(input_text):
    vowels = 'aeiou'
    if input_text[0] not in vowels:
        return pig_latin2_helper(input_text) + "ay"


res = pig_latin2("scram")
print(res)
