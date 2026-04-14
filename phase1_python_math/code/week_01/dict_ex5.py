phone_book = {}


while True:
    user_choice = int(input(" 1-search 2-add 3-quit "))
    if user_choice == 1:
        name = input("name : ")
        if name not in phone_book:
            print("not found")
        else:
            print(phone_book[name])

    if user_choice == 2:
        name = input("name : ")
        number = int(input("number : "))
        if name not in phone_book:
            phone_book[name] = []
        phone_book[name].append(number)
        print("ok!")

    if user_choice == 3:
        exit(0)
