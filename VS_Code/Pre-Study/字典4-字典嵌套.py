def check_all(all_list, item):
    count = 0
    for brought_list in all_list.values():
        count = count + brought_list.get(item, 0)
    return count


allBrought = {
    'Alice': {'Apple': 2, 'Peach': 5},
    'Bob': {'Banana': 3, 'Cake': 8},
    'Jack': {'Cake': 5, "Apple": 3}
}
print('- Apples ' + str(check_all(allBrought, 'Apple')))
print('- Peach ' + str(check_all(allBrought, 'Peach')))
print('- Banana ' + str(check_all(allBrought, 'Banana')))
print('- Cake ' + str(check_all(allBrought, 'Cake')))