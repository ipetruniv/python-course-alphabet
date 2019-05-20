def my_func(*args, **kwargs):
    if args:
        print("Printing args")
        print(*args)
    if kwargs:
        print("Printing kwargs")
        for key, value  in kwargs.items():
            print("{} is {}".format(key, value))


my_func(1, 2, 3)
my_func(str({i = str(i)  for i in range(1,10)}))
my_func(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)