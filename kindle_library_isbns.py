# Usage: Name the Text File "Raw_Book_List.txt"
#
# For instructions see readme.md
#
# Requires ISBN Tools : https://pypi.org/project/isbntools/
# pip install isbntools
#
# May need to be broken up into batches, as the remote service is rate limited.  I got temporarily blocked after around 500 requests.
# Runs off of the outut file from kindle_library.py

from mailbox import linesep
from isbntools.app import *

file = "output.txt"

file_read = open(file, "r")
file_write = open("isbns.txt", "a")
line_count = 0

while True:
    line_count += 1
    
    # Get next line from file
    books = file_read.readline()
    isbn = isbn_from_words(books)
    file_write.write(isbn+"\n")
  
    # if line is empty end of file is reached
    if not books:
        break

file_read.close()


