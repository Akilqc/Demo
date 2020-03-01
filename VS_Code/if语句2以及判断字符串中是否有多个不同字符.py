weight = int(input('Pleas input your weight: '))
sel = input('The weight unit you entered is (L)bs or (K)g: ')
print(sel == 'k')
while not (sel == 'l' or sel == 'L' or sel == 'K' or sel == 'k'):  #使用==或者使用in都是可以的
    sel = input('please select the right selection: ')
if 'L' in sel or 'l' in sel:
    true_weight = weight * 0.45
    print(f'The weight is:{true_weight} pounds')
elif 'K' in sel or 'k' in sel:
    true_weight = weight / 0.45
    print(f'The weight is:{true_weight} kilos')



# while not(sel.upper() == 'L' or sel.upper() == 'K')
# if sel.upper() == 'L':
#     true_weight = weight * 0.4
# elif sel.upper() == 'K':
#     true_weight = weight / 0.4
# 更简便的方法：使用upper或者lower函数，它们不会改变原来的选项，用于判断正好
