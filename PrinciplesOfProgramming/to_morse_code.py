def to_morse_code(mapping, input_message):
    output_string = ''
    skip_letters = " [(!)]"
    for letter in input_message:
        if letter not in skip_letters:
            output_string += mapping[letter.upper()] + " "
    print(output_string)


map = {'A':".-", 'B': "..-_"}
inp_msg = 'Ab A'

to_morse_code(map, inp_msg)