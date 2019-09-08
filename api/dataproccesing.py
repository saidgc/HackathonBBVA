import csv

if __name__ == "__main__":
    contador = 0
    contador2 = 0
    tags = []
    with open("dataset.csv", 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            if row[1] != -1:
                if float(row[18]) >= 50000:
                    if row[20] == '0':
                        print(row[1], row[2], row[4], row[18])    
                        contador += 1
                        tag = [1]
                        with open('tags.csv', 'a') as tags:
                            writer = csv.writer(tags)
                            writer.writerow(tag)
                        tags.close()
                    else:
                        contador2 += 1
                        tag = [0]
                        with open('tags.csv', 'a') as tags:
                            writer = csv.writer(tags)
                            writer.writerow(tag)
                        tags.close()
                else:
                    if row[15] != '0':
                        print(row[1], row[2], row[4], row[18])    
                        contador += 1
                        tag = [1]
                        with open('tags.csv', 'a') as tags:
                            writer = csv.writer(tags)
                            writer.writerow(tag)
                        tags.close()
                    else:
                        contador2 += 1
                        tag = [0]
                        with open('tags.csv', 'a') as tags:
                            writer = csv.writer(tags)
                            writer.writerow(tag)
                        tags.close()
            else:
                contador2 += 1
                tag = [0]
                with open('tags.csv', 'a') as tags:
                    writer = csv.writer(tags)
                    writer.writerow(tag)
                tags.close()
        print(contador)
        print(contador2)
        csvFile .close()
