import os

def display_list():
	#Check if the file exists; if so, print the list.
    fhand=open('todo.txt','r')
    if os.path.getsize('todo.txt') == 0:
        print('\033[1mTo-do List is empty\033[0m')
    else:
        print('\033[1m','To-do List','\033[0m')
        lines=fhand.readlines()
        counter=1
        for line in lines:
            print(counter,"-",line)
            counter=counter+1
    fhand.close()

while True:
    try:
        ch=int(input("""1.Add item  2.Delete item  """
        	"""3.Delete to-do-list  4.Display list  5.Stop\nEnter your choice : """))
    except:
        print("Enter valid numeric value. ")
        continue
    if ch == 1 :
        val=input("Enter to-do item: ")
        val=val+"\n"
        fhand=open('todo.txt','a')
        fhand.write(val)
        fhand.close()
        display_list()
    elif ch == 2 :
        if os.path.getsize('todo.txt') == 0:
            print('\033[1mTo-do List is empty\nCannot delete to-do item\033[0m')
            continue
        inp=int(input("Enter to-do number which you want to delete : "))
        #read and store lines in temp
        fhand=open('todo.txt','r')
        temp=[]
        for line in fhand:
            temp.append(line)
        fhand.close()
        #remove mentioned to-do item from temp
        temp.pop(inp-1)
        #store temp back into the file
        fhand=open('todo.txt','w')
        for line in temp:
            fhand.write(line)
        fhand.close()
        display_list()
    elif ch == 3 :
        fhand=open('todo.txt','r+')
        if os.path.getsize('todo.txt') == 0:
            print('\033[1mTo-do List is empty\033[0m')
        else:
            fhand.truncate(0)
        fhand.close()
        display_list()
    elif ch == 4 :
        display_list()
    elif ch == 5 :
        break
    else:
        print('Enter valid choice. ')
