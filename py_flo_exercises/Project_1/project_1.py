# Flag creator
flag_width = int(input("Flag width:\n"))
flag_height = int(input("Flag height:\n"))
width_height = (('#' * (int(flag_width / 2))) + ('-' * (int(flag_width / 2))) + '\n') * (int(flag_height/2)) + (('-' * (int(flag_width)) + '\n') * int(flag_height/2))
print(width_height)

