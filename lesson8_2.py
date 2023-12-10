def sayHello():
    print('Hello World!')

sayHello()
sayHello()
sayHello()


def sayHello2(name,age,is_male=None):
    if age<18:
        alias = "少年"
    elif age < 30:
        alias = "中年"
    elif age < 50:
        alias = "壯年"
    else:
        alias = "老年"
    
    print(f'Hello! {alias}:{name}!')

#引數值的呼叫要依順序
sayHello2("徐國堂",13)
sayHello2("robert",25)
sayHello2("jenny",45)
sayHello2("alice",65)

#引數名稱的呼叫
#可以不依順序
sayHello(name="徐國堂",age=13)
sayHello(age=25,name="robert")

#混合呼叫
#引數值呼叫在前面,引數名稱在後面
#使用引數名稱後,後面全部要使引數名稱的呼叫
sayHello("徐國堂",age=13)
sayHello("robert",age=25)


