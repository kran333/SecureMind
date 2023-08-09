def mystery(dictionary):
    result = {}
    for key in dictionary:
        if key < dictionary[key]:
            result[key] = dictionary[key]
        else:
            result[dictionary[key]] = key
    # print(sorted(result.keys()))
    print(f"Unsorted dict: {result}")
    myKeys = list(result.keys())
    myKeys.sort()
    sorted_dict = {i: result[i] for i in myKeys}
    print(f"Sorted dict: {sorted_dict}")



dict1 = {'two': 'deux', 'five': 'cinq', 'one': 'un',  'three': 'trois', 'four': 'quatre'}
# dict2 = {'skate': 'board', 'drive': 'car', 'program': 'computer', 'play': 'computer'}
dict2 = {'drive': 'car', 'play': 'computer', 'program': 'computer', 'skate': 'board'}
# dict3 = {'siskel': 'ebert', 'girl': 'boy', 'H': 'T', 'ready': 'begin', 'first': 'last', 'begin': 'end'}
dict3 = {'H': 'T', 'begin': 'end', 'first': 'last', 'girl': 'boy', 'ready': 'begin', 'siskel': 'ebert'}
dict4 = {'cotton': 'shirt', 'tree': 'violin', 'seed': 'tree', 'light': 'tree', 'rain': 'cotton'}

# mystery(dict1)
# mystery(dict2)
mystery(dict3)
# mystery(dict4)