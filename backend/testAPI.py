
import unittest 
from api import *

class APITester(unittest.TestCase):
    
    # sets up the database of books
    def setUp(self):
        earlyBook = earlyBooksAPI('EarlyEuropeanBooksCollection1Clean.csv')
        return earlyBook

    #Tests for SearchYearInterval
    def test_SearchYearInterval_valid(self):
        start = 1489
        end = 1493
        self.assertTrue(self.setUp().searchYearInterval(start, end).count('Regule emendate correcteque Hafnye de figuratis constructionibus grammaticis ex diuersis passibus sacre scripture ac poetarum feliciter incipiunt') > 0)
    def test_SearchYearInterval_boundAsString(self):
        start = 'Hello'
        end = 1493
        self.assertTrue(len(self.setUp().searchYearInterval(start, end)) == 0 )

    def test_SearchYearInterval_boundAsFloat(self):
        start = 1930.2
        end = 1493
        self.assertTrue(len(self.setUp().searchYearInterval(start, end)) == 0)


    #Tests for searchLanguage
    def test_SearchLanguage_pass(self):
        language = 'English'
        self.assertTrue(self.setUp().searchLanguageOfBook(language).count('A Postill-- or Exposition of the Gospels that are vsually red in the churches of God-- vpon the Sundayes and Feast dayes of Saincts-- Written by Nicolas Heminge-- and translated into English by Arthur Golding') > 0)

    def test_SearchLanguage_empty(self):
        language = 'elvish'
        self.assertTrue(len(self.setUp().searchLanguageOfBook(language)) == 0)
    
    
    #Tests for SearchPublisher
    def test_searchPublisherOfBook(self):
        publisher = 'Krafft'
        self.assertTrue(self.setUp().searchPublisherOfBook(publisher).count('Isagoge ad libros propheticos et apostolicos') > 0)
        self.assertFalse(self.setUp().searchPublisherOfBook(publisher).count('Hær begyndes en historie aff Flores oc Blantzeflor ...') > 0)

    #tests for SearchAuthor    
    def test_searchAuthorOfBook(self):
        author = 'Frandsen-- Hans'
        self.assertTrue(self.setUp().searchAuthorOfBook(author).count('Johannis Francisci Ripensis Elegiarum liber primus') > 0)
        print(self.setUp().searchAuthorOfBook(author).count('Iohannis Georgii Vibergii Elegidia'))
    
    #tests for searchTopic
    def test_searchTopicOfBook(self):
        topic = 'Religious'
        self.assertFalse(self.setUp().searchTopicOfBook(topic).count('Oratio funebris illustris viri') > 0)
        self.assertTrue(len(self.setUp().searchTopicOfBook(topic)) > 0)

    def test_searchNationOfPublication(self):
        nation = 'Italy'
        self.assertTrue(self.setUp().searchNationOfPublication(nation).count("Assemblea celeste radunata novamente in Parnasso sopra la nova cometa-- Dall'Academico Danico Il Riposato-- descritta in una lettera all'Academico Italico lo Spassionato") > 0)

if __name__ == '__main__':
    unittest.main()
