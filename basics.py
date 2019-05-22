li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 

def filterNums(x):

    if(x%2 != 0):
        return False
    else:
        return True

filterNum = filter(filterNums, li)

# for x in filterNum:
#     print(x)

#########without lambda####################
final_list = filter(lambda x: (x%2 != 0) , li)

for x in final_list:
    print(x)

class Person:
    def __init__(any, name, age):
        any.name = name
        any.age = age

    def getAge(any):
        print("Hello my name is " + any.name)

p1 = Person("John", 36)
# p1.getAge()

