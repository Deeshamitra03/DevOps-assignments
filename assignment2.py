
file = open("text.txt", "w")
file.write("Hello tutedude!.\n")
file.write("this is my assignment 2 related to python.\n")
file.close()
print("Content written to 'text.txt' successfully.")



file = open("text.txt", "r")
text = file.read()
print("File text:\n")
print(text)
file.close()
