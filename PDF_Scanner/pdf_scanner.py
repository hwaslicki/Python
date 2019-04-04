# breading season, breeding period, mating season, mating period, reproductive season, reproductive period
import PyPDF2
import os

f = open("out.txt", "a")
keywords = ""
keywordsArray = []

print("\n\n\nBefore starting, make sure all the documents you\n" + 
      "want to scan are in Documents directory.")

def gatherWords():
    print("\n\n Please enter the words you would like to search for.\n" +
        "Seperate the words with a pipe character( | ).")

    keywords = raw_input()

    fields = keywords.split('|')

    print("Are these words correct?\n\n")

    for field in fields:
        print(field)

    print("\n\n")

    wordsConfirm = raw_input("y or n\n")

    if wordsConfirm == "y":
        executeScan(fields)
    else:
        keywords = ""
        keywordsArray = []
        gatherWords()

def executeScan(keys):
    for fileName in os.listdir('./Documents'):
        if fileName.lower().endswith(".pdf"):
            print("Scaning " + fileName)
            found = False
            object = open("./Documents/" + fileName, 'rb')
            reader = PyPDF2.PdfFileReader(object)
            pageNums = reader.numPages

            currentPage = 0

            while currentPage < pageNums:
                page = reader.getPage(currentPage)
                text = page.extractText()

                for word in keys:
                    if word in text:
                        found = True
                
                currentPage = currentPage + 1

            if found == True:
                print("\nKeyword Found -- " + fileName)
                f.write(fileName)
        else:
            print("Non-PDF file found, ignoring...")
    
    print("\n\nScan Complete\n\n")


gatherWords()