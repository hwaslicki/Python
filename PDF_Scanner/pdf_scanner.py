# breading season, breeding period, mating season, mating period, reproductive season, reproductive period
import PyPDF2
import os

f = open("out.txt", "a")

for fileName in os.listdir('./Documents'):
    if "._" in fileName:
        print("")
    else:
        cleanedName = fileName.replace("'", "")
        object = open("./Documents/" + fileName, 'rb')
        reader = PyPDF2.PdfFileReader(object)
        pageNums = reader.numPages

        i = 0

        while i < pageNums:
            page = reader.getPage(i)
            text = page.extractText()

            if 'breedingseason' in text or 'BreedingSeason' in text or 'breedingSeason' in text or 'Breedingseason' in text:
                print("yes - " + cleanedName)
                f.write(cleanedName + "\n")
                    
            elif 'breedingperiod' in text or 'BreedingPeriod' in text or 'Breedingperiod' in text or 'breedingPeriod' in text:
                print("yes - " + cleanedName)
                f.write(cleanedName + "\n")
            elif 'matingseason' in text or 'MatingSeason' in text or 'matingSeason' in text or 'Matingseason' in text:
                print("yes - " + cleanedName)
                f.write(cleanedName + "\n")
                
            elif 'matingperiod' in text or 'MatingPeriod' in text or 'matingPeriod' in text or 'Matingperiod' in text:
                print("yes - " + cleanedName)
                f.write(cleanedName + "\n")

            elif 'reproductiveseason' in text or 'ReproductiveSeason' in text or 'reproductiveSeason' in text or 'Reproductiveseason' in text:
                print("yes - " + cleanedName)
                f.write(cleanedName + "\n")

            elif 'reproductiveperiod' in text or 'ReproductivePeriod' in text or 'reproductivePeriod' in text or 'Reproductiveperiod' in text:
                print("yes - " + cleanedName)
                f.write(cleanedName + "\n")

            else:
                print('No - ' + cleanedName)
            
            i = i + 1

print("Scan Complete")