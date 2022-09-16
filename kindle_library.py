# Usage: Name the Text File "Raw_Book_List.txt"
#
# For instructions see readme.md

from mailbox import linesep


file = "Raw_Book_List.txt"

file_read = open(file, "r",encoding='utf-8')
file_write = open("output.txt", "a",encoding='utf-8')
line_count = 0
counter = 0
write_string = ""

while True:
    line_count += 1
    
    # Get next line from file
    books = file_read.readline()
    if books[:-1] == "Prime Reading":
        books = file_read.readline()
    
    if counter == 0:
        write_string += books[:-1] + " - "
    elif counter == 3: 
        write_string += books
    elif counter == 4:
        file_write.write(write_string)
        write_string = ""
        counter = -1
    
    counter +=1
  
    # if line is empty end of file is reached
    if not books:
        break

file_read.close()


