import os

files=os.listdir()
files.remove("cleaning_clutters.py")
# print(files)

#this def will create folder if folder is previously not existed
def create_if_not_exits(folder):
    if not os.path.exists(folder):
        os.makedirs(folder) 

#this defination will move all the files to respective folders
def move_files(foldername,files):
    for file in files:#iterate and find each and every media files and tried to replace it with media folder
        os.replace(file,f"{foldername}/{pdf}")#this will reallocate media files inside media folder 


#function calling of all folders
create_if_not_exits("Images") 
create_if_not_exits("Docs") 
create_if_not_exits("Pdf") 
create_if_not_exits("Media")
create_if_not_exits("programs")  
create_if_not_exits("Other_folders")  

imgExtns=[".png",".jpg",".jpeg"]
images=[file for file in files if os.path.splitext(file)[1].lower() in imgExtns]

docExtns=[".txt",".docx",".doc"]
docs=[file for file in files if os.path.splitext(file)[1].lower() in docExtns]
print(docs)

pdfExtns=[".pdf"]
pdfs=[file for file in files if os.path.splitext(file)[1].lower() in pdfExtns]
print(pdfs)

MediaExtns=[".mp4",".mp3",".flv"]
medias=[file for file in files if os.path.splitext(file)[1].lower() in MediaExtns]
print(medias)

prgmExtns=[".py",".c",".cpp"]
prgms=[file for file in files if os.path.splitext(file)[1].lower() in prgmExtns]
print(prgms)

other_etxn=[]
for file in files:
    extn=os.path.splitext(file)[1].lower()
    if (extn not in MediaExtns) and (extn not in imgExtns) and (extn not in pdfExtns) and (extn not in docExtns) and os.path.isfile(file):
        other_etxn.append(file)

#move_files is a function where we will provide two arguments as functions folder name  and filenames
move_files("Images",images) 
move_files("Docs",docs) 
move_files("Pdf",pdfs) 
move_files("Media",medias)
move_files("programs",prgms)  
move_files("Other_folders",other_etxn)  

