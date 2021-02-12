mydictionary={
       "PRAJJAL":"NANU",
       "ABIJEET":"MINTU",
       "SUBHRA":"ISHAN",
       "ABHRAJEET":"RUDRA",
       "SNEHA":"TUBLI",
       "SURAJEET":"CHANDU"
}
print("options are",mydictionary.keys())
a=input("ENTER THE ORIGINAL NAME TO KNOW THE NICK NAME ASSOCIATED: ")
print("THE NICK NAME ASSOCIATED WITH ORIGINAL NAME IS: ",mydictionary.get(a))