def Argument(*args,**kwargs):
    for a in args:
        print(f"the args lenght is {type(a)} and {a}")
    print(f"The kwargs type is {type(kwargs)} and {kwargs}")
Argument("Dang","roll","jame")
Argument(key1="Name",key2="Lame")