unsorted = open("new_01.txt", "r")
sorted = open("new_02.txt", "w")

dataList = unsorted.readlines()
dataList.sort()

for line in dataList:
    #print (line)
    sorted.write(line)

unsorted.close()
sorted.close()