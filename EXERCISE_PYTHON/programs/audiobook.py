import pyttsx3
speaker=pyttsx3.init()
import PyPDF2
speaker.say("I'm Ready to read your book")
voices=speaker.getProperty("voices")
speaker.setProperty("voice",voices[2].id)
speaker.runAndWait()
book=open(r"C:\Users\Prj Rock's\Documents\books abroad authors\EDC\Neamen solid state device gate.pdf","rb")
pdfReader=PyPDF2.PdfFileReader(book)
page=pdfReader.numPages
print(page)
for num in range(page):
    singlepage=pdfReader.getPage(num)
    text=singlepage.extractText()
    speaker.say(text)
    speaker.runAndWait()
