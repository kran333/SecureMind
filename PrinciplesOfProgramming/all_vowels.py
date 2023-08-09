def is_all_vowels(input_str):
    vowels = ("a", "e", "i", "o", "u")
    non_vowel_cnt = 0
    for ind_str in input_str:
        if ind_str.isalnum():
            if ind_str.lower() not in vowels:
                non_vowel_cnt = non_vowel_cnt + 1
        else:
            continue

    if non_vowel_cnt == 0:
        return True
    else:
        return False


print(is_all_vowels("a_e_iuU"))

