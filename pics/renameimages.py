# Pythono3 code to rename multiple
# files in a directory or folder

# importing os module
import os

# Function to rename multiple files
def main():
    i = 0

    for filename in os.listdir("D:/holly/celebration/pics/pics"):
        newName ="holly_celebration_" + str(i) + ".jpg"
        src ='D:/holly/celebration/pics/pics/'+ filename
        dest ='D:/holly/celebration/pics/renamedresult/'+ newName

        # rename all the files
        os.rename(src, dest)
        i += 1
        newLoc = '\'https://github.com/Dgilliams/holly_pics/blob/master/pics/renamedresult/'+ newName +'?raw=true\','
        print(newLoc)

# Driver Code
if __name__ == '__main__':

    # Calling main() function
    main()
