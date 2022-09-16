## Kindle Library Parser

* Using the list on this page https://read.amazon.com/kindle-library?itemView=row
* Scroll all the way to the bottom, repeatedly
* Once you have everything loaded, click and hold on the side near but not on "Notes and Highlights"
* Drag over into the library to the last entry.  This should select everything.
* Open Raw_Book_List.txt in Notepad
* Paste the copied into Notepad replacing the sample list to get a clean format free file.
* Scroll to the top and delete any extra text and be sure the first two lines are a repeated title.
* This script is a simple dumb loop so the formatting is important!

### It will look something like this, over and over.

Alice's Adventures in Wonderland  
Alice's Adventures in Wonderland

Carroll, Lewis; Carroll, Lewis

The Autobiography of Benjamin Franklin  
The Autobiography of Benjamin Franklin

Franklin, Benjamin; Franklin, Benjamin

The Scarlet Letter  
The Scarlet Letter

Hawthorne, Nathaniel; Hawthorne, Nathaniel

### This script will parse through a file in this format and leave a format like this

Alice's Adventures in Wonderland - Carroll, Lewis; Carroll, Lewis  
The Autobiography of Benjamin Franklin - Franklin, Benjamin; Franklin, Benjamin  
The Scarlet Letter - Hawthorne, Nathaniel; Hawthorne, Nathaniel  
