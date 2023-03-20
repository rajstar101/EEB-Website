'''
Team B's API
Because B is for Best
'''
import psycopg2
import psqlConfig as psql

class earlyBooksAPI:
    conn = psycopg2.connect(dbname = psql.database, user = psql.user, password = psql.password, host= 'localhost', )
    cur = conn.cursor()
    def __init__(self):
        '''constructor''' 

    def searchTitleOfBook(self, title):

        '''Returns a list of books published within the specified range (inclusive)'''

        if not(isinstance(title, str)):
            return

        self.cur.execute("SELECT * FROM earlybooks WHERE LOWER(Title) LIKE LOWER('%%%s%%');" % (str(title)))
        return self.cur.fetchall()       
    
    def searchYearInterval(self, start, end):
        '''
        Returns a list of books published within the specified range (inclusive)

        PARAMETERS:
        start - The start of the time frame (inclusive) as an integer.
        end - the end of the time frame (inclusive) as an integer.

        Equivalence classes: Let x be a positive integer. Let y be a be a non-integer. 
        Thus, the equivalence classes are:
        [x,x']-> valid input (provided x<= x')
        [z,x] -> invalid input
        [x,z]-> invalid input
        ''' 
        
        if not(isinstance(start, int)) or not(isinstance(end, int)) or start >= end:
            return []

        self.cur.execute("""SELECT * FROM earlybooks WHERE DateOfPublication 
        BETWEEN %s AND %s;""", (int(start),int(end)))
        return self.cur.fetchall()


    def searchLanguageOfBook(self, language):
        '''
        Returns a list of books published in the desired languge
        
        PARAMETERS:
        language - the language in which books are desired to be filtered by as a string.
        
        Equivalence classes: Let x be a string (represents languages in the database).
        [x] -> valid input
        if x is not in the database then, an empty list would be returned.
        '''
        if not(isinstance(language, str)):
            return

        self.cur.execute("""SELECT * FROM earlybooks WHERE LanguageOfText = '%s'; """ % (str(language)))
        return self.cur.fetchall()      
    

    def searchPublisherOfBook(self, publisher): 
        '''
        Returns a list of books published by the given publisher

        PARAMETERS: 
        publisher - a string that matches the name of a publisher

        Equivalence Classes: Let x be a string that matches a publisher in the dataset.
        '''

        if not(isinstance(publisher, str)):
            return
        
        self.cur.execute("""SELECT * FROM earlybooks WHERE LOWER(PublisherPrinter) LIKE LOWER('%%%s%%')""" %  (str(publisher)))
        return self.cur.fetchall()

    def searchAuthorOfBook(self, author):
        '''
        Returns a list of books written by the given author

        PARAMETERS:
        author - a string that matches the name of an author
        
        Equivalence Classes: Let x be a string (represents author name).
        [x] -> valid input
        '''

        if not(isinstance(author, str)):
            return []
        
        self.cur.execute("""SELECT * FROM earlybooks WHERE LOWER(Author) LIKE LOWER('%%%s%%')""" % (str(author)))
        return self.cur.fetchall()


    def searchTopicOfBook(self, topic):
        '''
        Returns a list of books that classified undere the specified topics

        PARAMETERS:
        topic - the name of the topic of interest (i.e. medicine, funerals, etc.). If not specified, a list of books in alphabetical order by topic will be returned.
        
        Equivalence Classes: Let x be a string that matches a topic in the dataset.
        '''

        if not(isinstance(topic, str)):
            return []

        self.cur.execute("""SELECT * FROM earlybooks WHERE LOWER(USTCClassification) LIKE LOWER('%%%s%%') """ % (str(topic)))
        return self.cur.fetchall()

    def searchNationOfPublication(self, country):
        '''
        Returns a list of books that published in the specified region

        PARAMETERS:
        country - the name of the country of interests. If not specified, a list of books in alphabetical order by country name will be returned.   
        
        Equivalence Classes: Let x be a string that matches a country in the dataset.
        '''
        if not(isinstance(country, str)):
            return []

        self.cur.execute("""SELECT * FROM earlybooks WHERE CountryOfPublication = '%s' """ % (str(country)))
        return self.cur.fetchall()
    
    # returns a list that is the intersection of two given lists
    def intersect(self, list1, list2):
        list3 = []
        for item in list1:
            if list2.count(item) > 0:
                list3.append(item)
        return list3
    #turns a list into a dictionary
    def listToDict(self, list):
        dict = {
            "ID": "",
            "Title": "",
            "Author": "",
            "Year": "",
            "Publisher": "",
            "Nation": "",
            "Language": "",
            "Topic": "",    
        }
        dict["ID"] = list[0]
        dict["Title"] = list[1]
        dict["Author"] = list[2]
        dict["Year"] = list[3]
        dict["Publisher"] = list[4]
        dict["Nation"] = list[5]
        dict["Language"] = list[6]
        dict["Topic"] = list[7]
        return dict

    # searches in the databse for the given parameters and returns a list of sets of books that match the parameters
    def searchInDataBase(self,title, author, publisher, topic, nation, language, startYear, endYear):
        listOfSets = []
        if(title):
            listOfSets.append(self.searchTitleOfBook(title))
        if(author):
            listOfSets.append(self.searchAuthorOfBook(author))
        if(publisher):
            listOfSets.append(self.searchPublisherOfBook(publisher))
        if(topic):
            listOfSets.append(self.searchTopicOfBook(topic))
        if(nation):
            listOfSets.append(self.searchNationOfPublication(nation))
        if(language):
            listOfSets.append(self.searchLanguageOfBook(language))
        if(startYear or endYear):
            if(not startYear):
                startYear = 1481
            if(not endYear):
                endYear = 1753
            listOfSets.append(self.searchYearInterval(int(startYear), int(endYear)))
        while len(listOfSets) > 1:
            listOfSets[0] = self.intersect(listOfSets[0], listOfSets[1])
            listOfSets.pop(1)
        listOfSets = listOfSets[0]
        
        ListOfLists = []
        for item in listOfSets:
            ListOfLists.append(self.listToDict(list(item)))
        

        return ListOfLists

