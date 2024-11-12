import convert

def gather_numbers() -> list[float]:
    float_list = []
    done = True
    while done:
        floatitem = input("Enter something into here please")
        floatitems = convert.str_to_float(floatitem)
        if floatitems != None:
            float_list.append(floatitems)
        else:
            continue
        value = (input("type done if you are done adding items into list")).lower()
        if value == 'done':
            done = False
        else:
            continue
    return float_list

if __name__ == '__main__':
    print(gather_numbers())
