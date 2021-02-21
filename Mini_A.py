import csv
"""
def load_CSV():
    with open('CO2Emissions_filtered.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        next(reader, None)
        people_dict = {row[1].lower():row[3:] for row in reader}
        print (people_dict)
    return(people_dict)
if __name__ == '__main__':
    load_CSV()
"""
def load_CSV():
    with open('CO2Emissions_filtered.csv', 'r') as csvFile:
            reader = csv.reader(csvFile)
            next(reader, None)
            people_dict = {row[1].lower(): [float(j) for j in row[3:]] for row in reader}
            #for i in people_dict.keys(): 
            #    people_dict[i]=[float(j) for j in people_dict[i]]
            # print(people_dict)
    return (people_dict) 
load_CSV()

