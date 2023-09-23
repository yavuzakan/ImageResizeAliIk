from PIL import Image
import os
import csv


try: 
    os.mkdir("son") 
except OSError as error: 
    i=0

with open('son\\liste.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["Filename"]
    
    writer.writerow(field)



def resize(name):
    try:
        image = Image.open(name)
        image.thumbnail((180, 240))
        Tr2Eng = str.maketrans("çğıöşü ", "cgiosu_")
        name = name.translate(Tr2Eng)
        image.save("son\\"+name)
        print(name)
        with open('son\\liste.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name])

    except:
        i=0

  



obj = os.scandir(os.getcwd())
for entry in obj:
    if entry.is_file():
        #print(entry.name)  
        resize(entry.name)   

