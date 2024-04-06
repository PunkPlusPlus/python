"""
    Написать программу, которая принимает в качестве аргумента имя организации (или часть имени).
    Программа должа найти в файле все организации с таким именем или с именем,
    которое содержит переданную строку.
"""

import csv
import sys

def search_organizations(keyword):
    NAME_COLUMN = 'Наименование / ФИО'
    
    count = 0
    with open('./csv/organizations.csv', newline='', encoding='utf-8') as csvfile:
        # Пропускаем первую строку с общим заголовком
        next(csvfile)
        next(csvfile)
        reader = csv.DictReader(csvfile)
        for row in reader:
            if keyword.lower() in row[NAME_COLUMN].lower():
                print(row[NAME_COLUMN], "-", row['Категория'])
                count += 1
    return count

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python program.py <organization_name>")
    else:
        keyword = sys.argv[1]
        count = search_organizations(keyword)
        print(f"Total organizations found: {count}")
