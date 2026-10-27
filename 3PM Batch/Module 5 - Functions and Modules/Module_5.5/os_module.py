import os

print(os.getcwd()) # Print current working folder

print(os.listdir()) # Lists files and folders in a directory

# os.mkdir("KaifPython") # Creates a new folder
# os.makedirs("KaifPython/Kaif/Sanghe") Creates nested folders
# os.rmdir("KaifPython") # Removes an empty directory



# os.rename("5.5", "Module_5.5") 	#Renames a file or directory
# os.remove("Module_5.5/tempCodeRunnerFile.py") # Delete a file

print(os.path.exists("C:/Users/Visual Labs/OneDrive/Desktop/3PM-Python/3PM Batch/Module 5 - Functions and Modules/Module_5.5/kaif.py"))

print(os.path.isfile("C:/Users/Visual Labs/OneDrive/Desktop/3PM-Python/3PM Batch/Module 5 - Functions and Modules/Module_5.5/p1.py"))


print(os.path.isdir("C:/Users/Visual Labs/OneDrive/Desktop/3PM-Python/3PM Batch/Module 5 - Functions and Modules/Module_5.5"))

print(os.name)