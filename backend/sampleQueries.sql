/* List all of the books published in 1619. */

SELECT * FROM earlybooks WHERE DateOfPublication BETWEEN 1619 AND 1669 AND USTCClassification LIKE '%Religious%'; 
/* List books written in Italian */

SELECT *  FROM earlybooks WHERE LanguageOfText = 'Italian' AND CountryOfPublication = 'Germany';

/* List books written by Niels Hemmingsen (Note: the double dash used to be a comma,
we had to change it becuase the csv wasdelimited by semicolons intstead of commas; 
thus, we had to change commas in the entries for '--', and then semicolons to commas). */

SELECT * FROM earlybooks WHERE Author LIKE '%Hemmingsen-- Niels%' AND LanguageOfText = 'Latin';
