customer = {
    "name": "AkiKagura",  #注意逗号！也注意不要写成了等号
    "age": 22,
    "gender": "Man",
    "is_verified": True
}
print(customer["name"])
customer["name"] = 'Akikagura.lqc'  #修改字典中key所对应的值
print(customer.get('birthday'))  #使用gat函数来获得key所对应的的值，并且不会发生错误，若寻找的key不在字典里则只会返回None
print(customer.get('birthday'),'Oct 5 1998')  #使用get函数的时候我们也可以进行一个初始值的赋予，就算字典中没有这个key，我们也可以得到一个初始值
customer['birthday'] = 'Oct 5 1998'  #我们可以在字典外进行key的增加
print(customer.get('birthday'))

numbers = {
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four'
}
phone = input('Phone: ')
output = ''
for ch in phone:
    output = output + numbers.get(ch, '!') + ' '
print(output)