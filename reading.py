#open the file
text_file = open("files\myfile.txt")
#read the file
content = text_file.read()
#treat the file
for line in text_file:
    print(line + "Great !")

#close the file
text_file.close()
#print the result
print(content)