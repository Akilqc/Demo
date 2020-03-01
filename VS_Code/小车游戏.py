print('Welcom to the game, you can enter help to get rules.')
income_sel = ""
# old_income_sel = ""
flag_start = False      #很好的一个思想：使用一个布尔类型的flag来代表小车的状态 简单易懂
while True:
    income_sel = input('> ')
    # if old_income_sel.lower() == income_sel.lower() and income_sel.lower() == 'start':
    #     print('The car has already started! Please enter again!\n')
    #     continue
    # elif old_income_sel.lower() == income_sel.lower() and income_sel.lower() == 'stop':
    #     print('The car has already stopped! Please enter again!\n')
    #     continue
    # else:
    if income_sel.lower() == 'help':
        print('''
start - to start the car
stop - to stop the car
quit - to exit\n
        ''' )
    elif income_sel.lower() == 'start':
        if flag_start:
            print('The car has already started! Please enter again!\n')
            continue
        else:
            print('Car started...Ready to go!\n')
        flag_start = True
    elif income_sel.lower() == 'stop':
        if not flag_start:
            print('The car has already stopped! Please enter again!\n')
            continue
        else:
            print('Car stopped.\n')
        flag_start = False
    elif income_sel.lower() == 'quit':
        break
    else:
        print("I don't understand that...\n")
        # old_income_sel = income_sel
print('Gane Over!')
