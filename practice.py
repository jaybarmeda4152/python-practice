def countLines(fileName):
    file = open(fileName,'r+')
    count = 0
    for line in file:
        # print(count , line,end="")
        count += 1
    
    file.write("\n\n Total line in this file is "+str(count)+".")
    file.close()
    return count

print("Total lines in your files is",countLines("D:/Jay/Basic_constiction_site_template.txt"),end=".")
