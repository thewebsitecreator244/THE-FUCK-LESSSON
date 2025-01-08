book_phones = {

}
contact = input("enter new contact: ")
number = input("enter new number: ")
if contact !="" and number!="":
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