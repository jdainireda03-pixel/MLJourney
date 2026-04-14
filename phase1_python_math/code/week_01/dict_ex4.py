phone_book = {}


while True:
    user_choice = int(input(" 1-search 2-add 3-quit "))
    if user_choice == 1:
        name = input("name : ")
        if name in phone_book:
            print(phone_book[name])
        else:
            print("not found!")

    if user_choice == 2:
        name = input("name : ")
        number = int(input("number : "))
        phone_book[name] = number
        print("ok!")

    if user_choice == 3:
        exit(0)
