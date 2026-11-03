# Local and global scope

count = 10

def readit():
    print("Global value of count: ", count)

def writeit():
    global count
    count = count + 1
    print("Value inside local scope: ",count)

readit()
writeit()