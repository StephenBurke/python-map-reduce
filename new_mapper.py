input = open("purchases.txt", "r")
output = open("new_01.txt", "w")

for line in input:
    datalist = line.strip().split("    ")
    date, time, city, item, cost, paymentType = datalist
    output.write(paymentType +  '\t' + '1' + "\n")

input.close()
output.close()