def reverse(input_str):
    if input_str != '':
        return input_str[-1] + reverse(input_str[:-1])
    else:
        return ''


print(reverse("Hi you!"))