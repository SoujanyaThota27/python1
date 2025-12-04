#1
'''a=10
for i in range(1,11)        # syntax error
    print(i)'''

#2
'''a,b=10,20
def add():
print(a+b)'''    #identation error     

#3
'''l=10
w=5
area=l+w   
 # logical error    --by formula area=l*w
print(area)'''

#4
'''a=10
b=0
print(a/b)'''  # division by zero at runtime

#5
'''x="5"
y=2
print(x*y)
print(x+y)''' # runtime error
#type error: can't add str and int

#6
'''num=int("hello")'''
#value error: cannot convert a non-numeric string to integer

#7
'''file=open("not_existing_file.text","r")'''
# error:file does not exist

#8
'''d={"name":"sou"}
print(d["age"])'''
#key error

#9
'''print(a)
a=50'''
#name error

#10
'''l=[1,2,3]
print(l[5])'''
#index error