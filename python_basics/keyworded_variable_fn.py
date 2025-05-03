def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)
person('yamini',age=28,phno=8273776)