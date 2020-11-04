#open the file
text_file = open("files/names.txt")
#treat the file
for line in text_file:
    print(line)
    #ligne vide à la fin du .txt
#close the file
text_file.close()
