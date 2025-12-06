#code 1:
'''try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
else:
    print("Division executed without error")'''

#code 2

'''try:
    a = int(input("Enter index: "))
    l = [1, 2, 3, 4]
    print(l[a])
except IndexError :
    print("index out of range")
except ValueError:
    print("index is a not a alphabet")
else:
    print("List accessed successfully")'''

#code 3
'''try:
    data={"name":"soujanya"}
    print(data["age"])
    print(a)
except KeyError:
    print("error:key not found!")
except NameError as e:
    print(e)
else:
    print("dictionary and variable accessed successfully")'''

#code 4
'''try:
    f=open("data.txt","r")
    print(f.read())
    import abcxyz
except Exception as e:
    print(e)
else:
    print("file read and module imported successfully")'''

