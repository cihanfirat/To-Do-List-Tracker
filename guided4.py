
def show_todo_list():
    #pass
    with open("todos.txt", "r") as f:
        todo_list = f.readlines()
    #print(todo_list)
    n=1
    if not todo_list:
        print("Nothing in the list!")
    else:
        for line in todo_list:
            line = line.strip()
            print('  * (' + str(n) + ') ' + line)
            n+= 1
    f.close()


def add_to_todo_list(item):
   # pass
    with open("todos.txt","a") as f:
        f.write(item + "\n")
        f.close()

def remove_from_todo_list(number):
    #pass
    f=open("todos.txt","r")
    new=""
    count=1
    for line in f:
        if count != number:
            new+=line
        count+=1
    f.close()
    f=open("todos.txt","w")
    f.write(new)
    f.close()

def main():
    command = ''
    while command != 'exit':
        command = input('show, add, remove, or exit? ')
        if command == 'show':
            show_todo_list()
        elif command == 'add':
            task = input('What task needs to be added? ')
            add_to_todo_list(task)
        elif command == 'remove':
            number = int(input('What item number should be removed? '))
            remove_from_todo_list(number)
    print('Goodbye!')

main()