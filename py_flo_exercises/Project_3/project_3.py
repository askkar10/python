def print_hair(hair, eye):
    first_line = hair * 12 + '\n'
    second_line = hair + '|' + (' ' * 8) + '|' + hair + '\n'
    third_line = hair + '|' + (' ' * 2) + eye + (' ' * 2) + eye + (' ' * 2) + '|' + hair + '\n'
    fourth_line = ' ' + '|' + (' ' * 3) + '/\\' + (' ' * 3 ) + '| ' + '\n'
    five_line = ' |' + (' ' * 8) + '| ' + '\n'
    six_line = ' \\' + '  ' + '\'--\'' + '  ' + '/ ' + '\n'
    seven_line = '   ------   '
    return first_line + second_line + third_line + fourth_line + five_line + six_line + seven_line

def body_printing(height, arm):
    body_height = ((height - 11) // 2) - 1
    body = '     XX     ' + '\n'
    arms = arm + '----XX----' + arm + '\n'
    i = 0
    next_arms = ''
    while i <= body_height:
        next_arms += '    XXXX' + '\n'
        i += 1
    return body + arms + next_arms

def reverse_shoe(shoe_string):
    return (shoe_string[::-1])

def legs_print(height, shoe):
    first_line = '    ====' + '\n'
    leg_height = ((height - 11) // 2) - 1
    i = 0
    legs = ''
    while i <= leg_height:
        legs += '   ||  ||' + '\n'
        i += 1
    shoee = ' ' + shoe + '  ' + reverse_shoe(shoe)
    return first_line + legs + shoee

def main():
    print('Welcome to the custom character creator tool!')
    height = input("Overall character height: ")
    hair = input("Character for the hair: ")
    eyes = input("Character for the eyes: ")
    arms = input("Character for the arms: ")
    shoes = input("4- character string for the shoes: ")
    print(print_hair(hair,eyes))
    print(body_printing(int(height), arms), end="")
    print(legs_print(int(height),shoes), end="")


main()

