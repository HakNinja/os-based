import os

while True:
    print('\n\n')
    print('*'*35)
    print('\t\tMENU')
    print('*'*35)
    print('Press 1 to open editor.')
    print('Press 2 to open vlc')
    print('Press 3 to open browser')
    print('Press 0 to exit')
    print('Enter Query:',end='')
    user_input=input()
    if user_input=='1':
        os.system('nano')
    elif user_input=='2':
        os.system('vlc')
    elif user_input=='3':
        os.system('firefox') 
    elif user_input=='0':
        break
    else:
        print('\nError : Input Not Supported!!!')
        print('Try Again with different input...')
    print('*'*35)
print('*'*35)
print("\nHope you log-in again...\nBye!!!")