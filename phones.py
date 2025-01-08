
book_phones = {
 }
while True:
    choice=input("enter what you want to do: 1 see 2 add 3 change 4 delete: ")
    if choice == "1":
        numbersee=input("enter the number that you want to see: ")
        if numbersee in book_phones:
            print(book_phones[numbersee])
        else:
            print("number not found")
    elif choice == "2":
        contact = input("enter new contact: ")
        number = input("enter new number: ")
        if contact != "" and number != "":
            book_phones[contact] = number
            for key in book_phones:
                print(f'{key}: {book_phones[key]}')
        elif contact != "":
            if contact in book_phones:
                print(book_phones[contact])
            else:
                print("not found")
        else:
            print("cannot add or find")
    elif choice == "3":
        change_choice = input("enter the phone you want to change:  ")
        if change_choice in (book_phones):
            number_choice = input("enter the new number:    ")
            book_phones[change_choice]=number_choice
        else:
            print("not found")
    else:
        del_c = input("enter the contact you want to delete: ")
        if del_c in book_phones:
            book_phones.pop(del_c)
            print(f" {del_c} was successfully deleted")
        else:
            print(f"{del_c} is not a contact")
    print(book_phones)

