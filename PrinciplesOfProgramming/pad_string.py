def pad_string(inp_str, inp_cnt):
    return (inp_str + " "*(inp_cnt - len(inp_str)))

opt = pad_string("elephant", 10)
print(opt)