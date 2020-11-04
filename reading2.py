#open the file
text_file = open("files/myfile.txt")
#treat the file
for line in text_file:
    print(line + "Great !")
    #ligne vide à la fin du .txt
#close the file
text_file.close()
