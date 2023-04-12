sourcePath = input("Please enter the full path of the source file: ")
print("The source path is: " + sourcePath)
strSource = input("Please enter the string to search for: ")
print("This value will be replaced: " + strSource)
destinationPath = input("Please enter the full path of the destination file: ")
print("The destination path is: " + destinationPath)
strDestination = input("Please enter the string to replace the old value with: ")
print("The value is replaced with: " + strDestination)

with open(sourcePath, 'r') as f:
    data = f.read()
    f.close()
    print(sourcePath + " dizinindeki okunan dosyanın içeriği: \n" +  data)

    newData = data.replace(strSource, strDestination)

    print("Creating file...")

with open(destinationPath, 'w') as file:
    file.write(newData)
    file.close()
    print(destinationPath + " dizinindeki oluşturulan dosyanın içeriği: \n" +  newData)

    input("Press any key...")
