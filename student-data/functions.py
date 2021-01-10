''' 
This program stores all fn that are required for the porject.
All fn have been used in student_data project
'''

users = {'naveen':'1234'} #contains all usernames and passwords

data = {'naveen':{'name':'Naveen','roll_no': 18,'phone_no': '8910352867','class': 11,'subject': ['Maths','Physics', 'Chemistry', 'Computer', 'English']
}}   #data stores record of students basic data

acadmic= {'naveen':{'marks':[91, 92, 95, 96, 89], 'total': 437,  'percentage':437/5}} #acadmic strores marks and percentage

if __name__ == 'name':
    user_name= ''
def login():
    '''This function check avalibility of user'''
    global user_name
    user_name = input('user name : ').lower()
    password = input('password : ')
    if user_name in users and password == users[user_name]:
        return True
    else:
        print('user name or password is wrong')
        return False
user = ''
def signup():
    '''This function adds new user'''
    global user
    user = input('new user name : ').lower()
    password = input('new password : ')
    users[user] = password
    data[user] = {}
    acadmic[user] = {}

def delete():
    '''This deletes data of a user'''
    if login():
        ask = input('are you sure to delete this user y/n')
        if ask=='y':
            del users[user_name]
            del data[user_name]
            if user_name in acadmic:
                del acadmic[user_name]
    else:
        print('username and password doesn`t match')

log_in = False
def update():
    '''This updates data of user '''
    global user_name
    if log_in == True:
        try:
            ask = int(input('''
choose option 
1 = uesrname
2 = password
3 = personal data
4 = marks
0 = back
type here : '''))
        except:
            print('not a valid option')
        if ask == 1:
            new_name = input('new username : ')
            users[new_name], data[new_name], acadmic[new_name]={}, {}, {}      #added new blank data
            users[user_name], users[new_name]  =  users[new_name], users[user_name]  
            data[user_name], data[new_name]  =  data[new_name], data[user_name]
            acadmic[user_name], acadmic[new_name]  =  acadmic[new_name], acadmic[user_name]
            del users[user_name]
            del data[user_name]
            del acadmic[user_name]
            user_name = new_name
            update()

        elif ask==2:    #changes password
            new_pass = input('new password : ')
            users[user_name] = new_pass
            update()

        elif ask == 3:
            while True:
                print('''
what do you want to update
n = name
r = roll no.
p = phone no.
c = class
s = subject
0 = back
''')
                print()
                choice = input('type here : ')

                if choice == 'n':
                    change = input('give name here : ')
                    data[user_name]['name'] = change

                elif choice == 'r':
                    try:
                        change = int(input('give roll_no here : '))
                        data[user_name]['roll_no'] = change
                    except:
                        print('sorry invalid input')
                        
                elif choice == 'p':
                    change = input('give phone no. here : ')
                    data[user_name]['phone_no'] = change

                elif choice == 'c':
                    try:
                        change = int(input('give your class here : '))
                        if change <= 12:
                            data[user_name]['class'] = change
                        else:
                            print('invalid class given')
                    except:
                        print('invalid class given')
                    
                elif choice == 's':
                    print('your current subjects are :')
                    print(data[user_name]['subject'])
                    sub = input('type wrong subject name here : ').capitalize()
                    if sub in data[user_name]['subject']:
                        i = data[user_name]['subject'].index(sub)
                        change = input('give new subject name : ').capitalize()
                        data[user_name]['subject'][i] = change
                    else:
                        print("subject don't exist")

                elif choice == '0':
                    break

                else:
                    print('~invalid choice')

        elif ask == 4:
            while True:
                sub = input('enter subect name : ').capitalize()
                if sub in data[user_name]['subject']:
                    i = data[user_name]['subject'].index(sub)
                    try:
                        no = int(input('give your correct marks here : '))
                        if no <= 100:
                            acadmic[user_name]['marks'][i] = no
                            acadmic[user_name]['total'] = sum(acadmic[user_name]['marks'])
                            acadmic[user_name]['percentage'] = sum(acadmic[user_name]['marks'])/5


                        else:
                            print('max marks is 100')
                    except:
                        print('please give correct marks')
                else:
                    print('subject don\'t exist')

                option = input('want to update more marks y/n :').lower()
                if option == 'n':
                    break
        elif ask == 0:
            pass
        else:
            print('invalid choice')


def logout():
    '''This function remove given user form record'''
    global log_in
    if log_in == True:
        log_in = False
        print('sucessful')
