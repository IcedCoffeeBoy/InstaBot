import csv

class CSVwriter:
    def __init__(self,path):
        self.path = path

    def insert(self, item):
        with open(self.path,'a') as file:
            writer = csv.writer(file, delimiter=",", quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
            writer.writerow(item)

    def many_insert(self,items):
        with open(self.path, 'a') as file:
            writer = csv.writer(file, delimiter=",", quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
            writer.writerows(items)



# Testing
if __name__=="__main__":
    csv_path = 'test_{}.csv'.format('one')
    csvwriter = CSVwriter(csv_path)
    csvwriter.insert(['abc','def'])
