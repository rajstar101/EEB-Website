'''
Command line code that calls Team B's API
'''
from api import *

def main():
    choice  = 'null'

    print('Welcome to Ancient Euro Text!')

    while choice != 'q':
        
        print('Please select from the following options')
        print('(a) : Find books by year.')
        print('(b) : Find books by language.')
        print('(c) : Find books by publisher.')
        print('(d) : Find books by author.')
        print('(e) : Find books by topic.')
        print('(f) : Find books by nation.')
        print('(q) : Quit this program')

        data = earlyBooksAPI()

        choice = input('Make your selection: ')
        
        if choice == 'a': # by year
            start = int(input('Start year: '))
            end = int(input('End year: '))
            booksByYear = data.searchYearInterval(start, end)
            print('\nThe following books were published between ' + str(start)  + ' and ' + str(end) + ' : ')
            for book in booksByYear:
                print(book)

        elif choice == 'b': # by language
            language = input('Select a language: ')
            booksByLanguage = data.searchLanguageOfBook(language)
            print('\nThe following books were published in ' +  language + ' : ')
            for book in booksByLanguage:
                print(book)
            
        elif choice == 'c': # by publisher
            publisher = input('Select a publisher: ')
            booksByPublisher = data.searchPublisherOfBook(publisher)
            print('\nThe following books were published by ' + publisher + ' : ')
            for book in booksByPublisher:
                print(book)
                
        elif choice == 'd': # by author
            author = input('Select an author: ')
            booksByAuthor = data.searchAuthorOfBook(author)
            print('\nThe following books were published by' + author + ' : ')
            for book in booksByAuthor:
                print(book)

        elif choice == 'e': # by topic
            topic = input('Select a topic: ')
            booksByTopic = data.searchTopicOfBook(topic)
            print('Books from about ' + topic + ' :')
            for book in booksByTopic:
                print(book)

        elif choice == 'f': # by nation
            nation = input('Nation: ')
            booksByNation = data.searchNationOfPublication(nation)
            print('Books from ' + nation + ' : ')
            for book in booksByNation:
                print(book)
        
        elif choice == 'q': # QUIT
            print('Goodbye!')

        else:
            print('I don\'t recognize that choice. Please select again.')

    print('Thank you for visitng Ancient-EuroBooks')


if __name__ == '__main__':
    main()
