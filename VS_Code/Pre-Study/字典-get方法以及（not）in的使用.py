customer = {
    "name": "AkiKagura",  #注意逗号！也注意不要写成了等号
    "age": 22,
    "gender": "Man",
    "is_verified": True
}
print(customer["name"])
customer["name"] = 'Akikagura.lqc'  #修改字典中key所对应的值
print(customer.get('birthday'))  #使用gat函数来获得key所对应的的值，并且不会发生错误，若寻找的key不在字典里则只会返回None
print(customer.get('birthday'),'Oct 5 1998')  #get的两个参数：要取得其值的key以及没有这个key时返回的备用值
customer['birthday'] = 'Oct 5 1998'  #我们可以在字典外进行key的增加
print(customer.get('birthday'))
print('birthday' in customer)  #用in或者not in来判断某元素是否位于字典里 更准确的可以使用customer.keys()或者customer.value()来寻找