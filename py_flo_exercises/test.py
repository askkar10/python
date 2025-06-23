data_file = open('todo.txt','r')
first_line = data_file.readlines()
i = 1
while i <= len(first_line):
    print(f"* ({i}) {first_line[i-1].strip()} ")
    i += 1

def line_remove(line):
    data_file = open('todo.txt','r')
    list = data_file.readlines()
    del list[line-1]
    x = ''.join(list)
    new_file = open('todo.txt','w')
    new_file.write(x)
    new_file.close()

line_remove(3)
