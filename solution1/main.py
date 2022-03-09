import csv
import re

def handle_csv():
    file = open('output.csv', "w")
    writer = csv.writer(file, delimiter='|',quoting=csv.QUOTE_NONE, quotechar='')
    with open('../sample_addresses.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            string = remover(row[0]) + ' '
            for i in row[1:-3]:
                if "/" in i:
                    string = string[0:-1] + i
                elif "-" in i:
                    string = string[0:-1] + i
                elif string.endswith("/") or string.endswith("-") or string.endswith(" "):
                    string += remover(i)
                else:
                    string = string + " " + remover(i) 
            for i in row[-3:]:
                string += ',' + remover(i)
            writer.writerow([string])
    file.close()
def remover(string):
    return re.sub(r"[\,\"]", '', string)

if __name__ == "__main__":
    handle_csv()
