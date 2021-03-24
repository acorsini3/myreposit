#create a note
def write_note(text):
    file = open("mynoteapp.txt", "a") #a is for append
    file.write("------\n") #\ for a new line
    file.write(text + "\n")
    file.close()

#search through notes
def search(text):
    file = open("mynoteapp.txt")
    content = file.read()
    file.close()
    result = ""
    notes = content.split("------")
    for note in notes:
        if note.find(text) != -1:
            result += "\n------" + note
    if result == "":
        print ("no result")
    else :
        print (result)

#menu
print ("input a command")
print ("press 1 to add a note")
print ("press 2 to search a note")
answer = input (": ")

#execution
if answer == "1":
    print ("enter a note")  
    note = input().strip()
    write_note(note)
elif answer == "2":
    print ("enter your search")
    text= input().strip()
    search(text)
else :
    print("please chosse between 1 and 2")
