s = open("new_02.txt","r")
r = open("new_03.txt", "w")

thisKey = ""
thisValue = 0.0

for line in s:
  data = line.strip().split('\t')
  paymentType, count = data

  if paymentType != thisKey:
    if thisKey:
      # output the last key value pair result
      r.write(thisKey + '\t' + str(thisValue)+'\n')

    # start over when changing keys
    thisKey = data
    thisValue = 0.0

  # apply the aggregation function
  thisValue += float(count)


# output the final entry when done
r.write(thisKey + '\t' + str(thisValue)+'\n')

s.close()
r.close()
