
import book_packs.book_class



print()
print('---------------------------------')
print('       NEXTBOOK MAIN MENU        ')
print('---------------------------------')
print()

if __name__ == '__main__':
    while True:

        print ('What would you like to do?')
        print ('1. Add a new book')
        print ('2. Get a reading suggestion')
        menu_choice = input('Choose 1 or 2: ')
        selection = int(menu_choice)


        if selection == 1:

            print("\nAdd a new book to the library:")
            print()

            nbt = input("Title: ").title()
            author = input("Author: ").title()
            newbook = '{} by {}'.format(nbt, author)


            print()
            print(book_class.add_book(nbt, author))
            print('\nLibrary updated')

        elif selection == 2:

    
            print(book_class.what_book())

        elif selection == 3:
            break

        else:
            print('Please choose 1 or 2')
            print()

'''
NewBook = Book()

if __name__ == '__main__':
  while True:
    print("\nAdd a new book to the library:")
    print()

    nbt = input("Title: ").title()
    author = input("Author: ").title()
    newbook = '{} by {}'.format(nbt, author)


    print()
    print(NewBook.add_book(nbt, author))
    #print("Added {}".format(newbook))
    break


NextBook = Book()

if __name__ == '__main__':
  while True:
    user_input = input("\nDo you need a book suggestion? Yes or no: ").lower()
    if user_input == 'yes':
        print()
        print(NextBook.what_book())


    elif user_input == 'end'.lower():
        break

    else:
      print()
      print("Let's try something else, shall we?")
      print()
      break
      #Return to menu
'''
