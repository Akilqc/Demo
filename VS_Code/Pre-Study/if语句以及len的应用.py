import time
name_temp = input('Creat Your Name: ')
time.sleep(1)
while len(name_temp) < 3 or len(name_temp) > 10:
    if len(name_temp) < 3:
        name_temp = input('The name must be at least 3 charactres!\nPleas re-enter the name: ')
    elif len(name_temp) > 10:
        name_temp = input("The name can be a maximum of 10 characters!\nPleas re-enter the name: ")
print(f"Your name is:{name_temp}. It looks good!")