import csv

def handle_csv():
    file = open('output.csv', 'w')
    writer = csv.writer(file, delimiter='|', quoting=csv.QUOTE_NONE,  quotechar='')
    with open('../sample_addresses.csv') as csvfile:
        spamreader = csv.reader(csvfile,  quotechar='|') 
        for row in spamreader:
            if len(row) > 1:
                print("The data has extra column: ", ','.join(row))
                continue
            string = row[0]
            if '"' in string:
                print("The string contain the double double quotation marks: " + string)
            elif ',' in string:
                print("The string contain the illegal comma: " + string)
            else:
                words = string.split(" ")
                line = [' '.join(words[:-3]) + ',' + ','.join(words[-3:])]
                writer.writerow(line)
    file.close()
if __name__ == "__main__":
    handle_csv()   
