# PDF Scanner

This script will have you enter in some keywords you need to search for delimited with a Pipe. Make sure to put any PDFs you want scanned inside the ***Documents*** directory. I wrote this code in a few hours, so I have listed the known bugs that I don't really want to fix.

### Needs:
- You will need to run this through some form of terminal app
- [PyPDF2](https://pypi.org/project/PyPDF2/) is used, you can install with PIP


### Known Issues:
- If you enter in a single word, you must have a pipe following, otherwise it will break
- I implemented a check on file type so the logic only runs on PDFs, but I am sure this could go wrong
- Again, this uses PyPDF2, so this could break. The logging is pretty good so feel free to change the code and fix it