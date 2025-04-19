# *** Shutil Module ***
import shutil
# The shutil module in Python is used for file and directory operations
#  It is especially useful for copying, moving, and deleting files and folders

# 1 copy file
# shutil.copy(src, dst)

# copies a file from src to dst (destination)
# it keeps the file contents but does NOT copy metadata (like permissions, timestamps)


shutil.copy("source.txt", "destination.txt")  # Copies the file


# we also have shutil.copy2() 

# same as copy but copy permissions metadata also
shutil.copy2("source.txt", "destination.txt")  

# 2 Copy Directories

# Copies an entire folder including all files and subfolders of that files 

shutil.copytree("my_folder", "backup_folder")  # Copies all files & subfolders

# 3 Moving Files & Directories

# shutil.move(src, dst)
#  Moves a file or folder to a new location
shutil.move("old_folder", "new_folder")  # Moves a folder
shutil.move("file.txt", "new_folder/")   # Moves a file


# 4 Deleting Files & Directories

# shutil.rmtree(path)
# Deletes a folder and all its contents files & subfolders
shutil.rmtree("backup_folder")  # Deletes the entire folder

# 5 Disk Usage Information
shutil.disk_usage(path)
# gets disk usage (total, used, free space)


usage = shutil.disk_usage("/")
print(f"Total: {usage.total / (1024**3)} GB")   # Total space
print(f"Used: {usage.used / (1024**3)} GB")     # Used space
print(f"Free: {usage.free / (1024**3)} GB")     # Free space

# 6 Making Archives (ZIP, TAR)
shutil.make_archive(base_name, format, root_dir)
# creates a ZIP or TAR archive from a folder

shutil.make_archive("backup", "zip", "my_folder")  # Creates backup.zip from my_folder
#  Formats supported: "zip", "tar", "gztar", "bztar", "xztar"




