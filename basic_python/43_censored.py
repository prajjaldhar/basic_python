words=["kutta","kamina","ghadha","suar","randi","motherfucker","bitch","pisser","pervert"]
content=True
i=1
with open("vulgar.txt") as f:
    while content:
        content=f.readline()
        content=content.lower()
        for slang in words:
            if slang in content:
                content=content.replace(slang,"%$@%@$@%*")
                print(f"Slag is present at {i}th line")
                i+=1
        with open("vulgar.txt","w")as f:
            f.write(content)