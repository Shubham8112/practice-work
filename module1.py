list1=["hi","hello","lists"]
print(list1[0])
print(list1[1])
print(list1[2])
list1[2]="python"
print(list1)
list1.append("Code is life")
print(list1)
list1.extend([45,67,89])
print(list1)'''
data=input("data:")
list1=data.split(",")
element=input("element:")
if element in list1:
    print("true")
else:
    print("false")
data = input("data:")
list1= data.split(",")
for i in range (0,len(list1)):
    list1[i]=int(list1[i])
if(list1[0]==3)or(list[-1]==3):
    print("true")
else:
    print("false")
class ct1:
    def __init__(self):
        self.test(7)
    def test(self, x):
        self.x = 3 * x;
    class ct2(ct1):
        def __init__(self):
            super().__(self)
            print(self.x)

         def test(self,x):
            self.x = 5 * x;
        check = ct2()

