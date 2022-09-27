## Exercise 34 - Working with os

# Create a directory structure by using os
# Create one parent directory with at least five child directories
# Create a file in each directory simply by using os and by changing directories beforehand

import os

os.mkdir("Using_OS")
os.chdir("Using_OS")

for i in range(5):
    os.mkdir(f"Dir{i+1}")
    os.chdir(f"Dir{i+1}")
    os.system(f"touch touch_file{i+1}.txt")
    open(f"open_file{i+1}.txt", "w")
    os.chdir("..")

os.chdir("..")
print(os.getcwd())
