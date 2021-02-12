str='''A paragraph is a series of related sentences developing a central idea, called the topic. 
Try to think about paragraphs in terms of thematic unity: a paragraph is a sentence or a group of sentences that supports one central, unified idea.
Paragraphs add one idea at a time to your broader argument'''
print(str)
print(len(str))
print(str.endswith("ment"))
print(str.count("p"))
print(str.upper())
print(str.lower())
print(str.find("sent"))
print(str.replace("paragraph","prajjal"))
letter=''' Dear <|NAME|>,
               You Are Selected to Represent Team <|TEAM|>!!!!
Thanking You
Team <|TEAM|>'''
Name=input("ENTER NAME\n")
Team=input("ENTER TEAM NAME\n")
letter=letter.replace("<|NAME|>",Name)
letter=letter.replace("<|TEAM|>",Team)
print(letter)