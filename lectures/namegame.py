def song(name):
    line_one = f"{name}, {name}, bo-b{name[1:]}\n"
    line_two = f"Banana-fana fo-f{name[1:]}\n"
    line_three = f"Fee-fi-mo-m{name[1:]}\n"
    line_four = f"{name}!"

    print(line_one + line_two + line_three + line_four)
