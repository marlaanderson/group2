# Group2
Authors:

Marla Anderson: mfanderson@uchicago.edu
* Wrote initial code for isograms, palindromes, and horizonal symmetry/ music notes program; typed up readme file, and edited Powerpoint

Kevin Ramirez: kevinramirez@uchicago.edu
* Wrote, debugged, and commented on initial anagram function, and edited Powerpoint, wrote code for ASCII interesting find.

Tina Tetrick: ctetrick@uchicago.edu 
* Made the majority of the Powerpoint and also merged the isogram and anagram programs so only iso-anagrams printed.

Date Last Modified: August 8, 2018

Python Version 3.7.0

## Programs:
Anagrams: Finds and groups words longer than 7 characters from a file that share the same letters. Also runs Isogram and ASCII function  based on results of Anagram function. (ASCII function finds numeric value of each word and groups all words that have same numeric value together, orders them in a list from smallest numerical value to greatest). All anagrams greater than 7 characters are saved to file anagramtest.txt, all anagrams filtered through the Isogram function are saved to file isogramtest.txt, and all anagrams filtered through ASCII function are saved to file ascii.txt.
* TO RUN: python anagrams.py

**Stand Alone Versions of Programs**

Isograms: Finds words in a list with no more than one of each letter, and then states a total at the end.
* TO RUN: python isograms.py 

Ascii: Finds numeric value of each word and groups all words that have same numeric value together, orders them in a list from smallest numerical value to greatest.
* TO RUN: python ascii.py

Palindromes: Lists all words spelled the same backwards as forwards from a given file.
        This will list palindromes lest than 8 characters because none above 7 exist in the given file.
* TO RUN: python palindromes.py

Horizontal Symmetry / Music Notes: Lists all word from a given file that contain only certain letters.
        By changing editing the code, you can search for different types of words. 
        For instance, to search for words that can be played on a piano, change the letters in the "horizontals" dictionary to A,B,C,D,E,F, and G
* To Run: python checkbook.py

  




