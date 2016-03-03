import csv

datafile = open('ship-nmpg.data','rb')
outfile = open('ship-nmpg.csv','w')
out = csv.writer(outfile)

# write out the csv headers
out.writerow(['nmpg', 'cyl', 'disp', 'hp', 'wt', 'accel', 'yr', 'origin','name'])

for line in datafile:
  line = line.strip()
  # add code to split the numeric data from the string name
  numbers, name = line.split('\t')
  # add code to split the numbers into a list
  numbers =  numbers.split()
  newline = numbers + [name]
  # add code to writerow each newline of data as csv
  out.writerow(newline)

datafile.close()
outfile.close()
