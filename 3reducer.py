s = open("02.txt","r")
r = open("03.txt", "w")

thisKey = ""
thisValue = 0.0

for line in s:
  data = line.strip().split('\t')
  paymentType, count = data

  if paymentType != thisKey:
    if thisKey:
      # output the last key value pair result
      r.write(str(thisKey) + '\t' + str(thisValue)+'\n')

    # start over when changing keys
    thisKey = paymentType
    thisValue = 0.0

  # apply the aggregation function
  #thisValue += float(amount)
  thisValue += float(count)

# output the final entry when done
r.write(str(thisKey) + '\t' + str(thisValue)+'\n')

s.close()
r.close()
