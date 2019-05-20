# Що таке дескриптор файлу

with open("Hello", "w") as file:
    #print(file)
    file.writelines("this line will be added to file named Hello \n")
    file.newlines

print("Enf")