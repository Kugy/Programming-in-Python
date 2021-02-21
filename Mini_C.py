from Mini_A import load_CSV
import csv

valDict = load_CSV()
countries = list(dict.keys(valDict))

print(len(countries))

updatedCountries = []

with open('population.csv', 'r') as _file:
    reader = csv.reader(_file)
    data = [row[1] for row in reader]    

def intersection(countries, data):
    for elements in countries:
        if elements in data:
            updatedCountries.append(elements)
    print(len(updatedCountries))

# if __name__ == '__main__':
intersection(countries, data)