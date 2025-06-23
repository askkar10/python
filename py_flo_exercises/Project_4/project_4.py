# To Do List

def show_todo_list():
    try:
        f = open('todo.txt','r')
        first_line = f.readlines()
        i = 1
        while i <= len(first_line):
            print(f"* ({i}) {first_line[i-1].strip()}")
            i += 1
    except FileNotFoundError:
        print('Nie ma jeszcze pliku todo.txt! Dodaj jakieś zadanie.')

def add_task(task):
    f = open('todo.txt','a')
    f.write('\n' + task)
    f.close()

def remove_task(line):
    data_file = open('todo.txt','r')
    list = data_file.readlines()
    del list[line-1]
    x = ''.join(list)
    new_file = open('todo.txt','w')
    new_file.write(x)
    new_file.close()

    
    
def main():
    flag = True
    while flag:
        question = input('What u want to do? show, add, remove or exit: ')
        if question == 'show':
            show_todo_list()
        if question == 'add':
            add = input("Co chcesz dodać? ")
            add_task(add)
        if question == 'exit':
            print("Dziekuej za skorzystanie z programu!")
            flag = False
        if question == 'remove':
            remove = input("Które zadanie chcesz usunać? Podaj index zadania:  ")
            remove_task(int(remove))

main()

