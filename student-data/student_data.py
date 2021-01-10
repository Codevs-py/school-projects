import functions as fn

while True:
    print('''
+-------------------------------+
| What do you want to do        |
| choose from menu              |
| 0 = see description           |
| 1 = login                     |
| 2 = signup                    |
| 3 = delete                    |
| 4 = exit                      |
+-------------------------------+
''')

    try:
        menu = int(input('type your option no. here : '))

        if menu == 1:
            if fn.login():
                fn.log_in = True
                print('\n')
                print('----------------------------------------------------')
                print('~ welcome you are logged in')
                print('----------------------------------------------------')
                print(' This is your personal data')
                print()
                for a in fn.data[fn.user_name]:
                    print(f'{a} = {fn.data[fn.user_name][a]}')
                print()
                print('This is your acadmic data \n ')
                for a in fn.acadmic[fn.user_name]:
                    if a == 'marks':
                        print('your marks ')
                        for sub in fn.data[fn.user_name]['subject']:
                            i = fn.data[fn.user_name]['subject'].index(sub)
                            print(f' {sub} = {fn.acadmic[fn.user_name][a][i]}')

                    else:
                        print()
                        print(f'{a} = {fn.acadmic[fn.user_name][a]}')    
                            
                while True:
                    print('''+------------------------------+            
|your further options are      |
| 1 = update                   |
| 2 = logout                   |
+------------------------------+  
''')
                    try:
                        option = int(input('type your option no. here : '))

                        if option == 1:
                            fn.update()
                            print('\n'*2)

                        elif option == 2:
                            fn.logout()
                            print('\n')
                            break

                        else:
                            print('Invalid option')

                    except:
                        print('invalid Option')

            print()
            input('Hit enter to continue')
            print()

        elif menu == 2:
            print('\n'*3)
            fn.signup()
            fn.data[fn.user]['name'] = input('give your name here :')
            while True:
                try:
                    fn.data[fn.user]['roll_no'] = int(input('your roll no. here : '))
                    break
                except:
                    print('invalid input')
            
            while True:
                n = input('your phone no. here : ')
                try:
                    if len(n) == 10:
                        fn.data[fn.user]['phone_no'] =str(n)
                        break
                    else:
                        print('~invalid phone no.')    
                except:
                    print('invalid phone no.')
            
            while True:
                try:
                    clas = int(input('your class here : '))
                    if clas <= 12:
                        fn.data[fn.user]['class'] = clas
                        break
                    else:
                        print('give correct class')
                except:
                    print('give correct class')
                
            fn.data[fn.user]['subject'] = list()
            fn.acadmic[fn.user]['marks'] = list()
            for s in range(5):
                sub = input('give your subject name : ').capitalize()
                fn.data[fn.user]['subject'].append(sub)
                while True:
                    try:
                        no = int(input(f'give your {sub} marks here : '))
                        if no <= 100:
                            fn.acadmic[fn.user]['marks'].append(no)
                            break
                        else:
                            print('max marks is 100')
                    except:
                        print('please give correct marks')
            fn.acadmic[fn.user]['total'] = sum(fn.acadmic[fn.user]['marks'])
            fn.acadmic[fn.user]['percentage'] = sum(fn.acadmic[fn.user]['marks'])/5        
            print()
            print(f'Successfully added {fn.user}')
            print('\n'*2)

        elif menu == 4:
            print(' Thanks for using :-)')
            break

        elif menu == 3:
            fn.delete()

        elif menu == 0:
            print()
            print('''
  This program stores data of students in form of user and password system.
  Each user can store data for one person which include -->
    1. Name
    2. Class
    3. Roll number
    4. Phone number
    5. Five Subjects
    6. And their marks respectively

  Each of above values are upgradable including username and password


From the menu you choose any of the following options...

 1> Login ==> This option let you to see details of existing user. But for this you must know his or her username and password.
              Under this you will find following options....

              1> Update => This let you to update any info including username and password by following options.
                           1= Username : To edit username.
                           2= Password : To edit Password.
                           3= Personal Data : To edit any other info about an user such as

                                n = Name : To change name
                                r = Roll no. : To change roll no.
                                p = Phone no. : To change phone no.
                                c = Class : To change class
                                s = Subject : To change subject name.

                            4= Marks : This can be used to change marks of any subject

                2> Logout => This brings back to menu by logging out user.

 2> Signup ==> This option is used to register new users and fill their info.

 3> Delte ==> This option let you to delete an existing user but password veryfication is must.
 
 4> Exit ==> This option is used to exit program 


            ''')

        else:
            print('Invalid option!!')        

    except:
        print('invalid option')
