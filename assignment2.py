from urllib.request import urlretrieve as retrieve
import datetime
import logging
import csv
import argparse
import sys

url = 'https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv'

def downloadData(url):
    retrieve(url, 'birthday_dict.csv')

x = open('birthday_dict.csv', 'r')
reader = csv.reader(x)

def processData(reader):
    newdict = {}
    data = []
    next(reader)
    
    for row in reader:
        data.append(row)

    ival = 0
    for i in data:
        ident = i[0]
        name = i[1]
        date = i[2]

        try:
          bday = datetime.datetime.strptime(date, '%d/%m/%Y')
        except ValueError:
            logging.error('Error on line' + str(ival) + ' ID #' + str(ident))
            newdict[ident] = (name, date)
        else:
            newdict[ident] = (name, bday)
        ival+=1
    return newdict

    

    def displayPerson(ID, personData):
        ID = str(ID)
        if ID in personData.keys():
            print(ID + ' is ' + personData[ID][0] + ' born on ' + str(personData[ID][1]))
        else:
            print('There is no user with that ID')

    

    def main():
        values = input('Enter employeed ID as an integer from 1 to 100')
        information = downloadData(args.url)
        personData = processData(information)

        while int(values) > 0:
            try:
                displayPerson(values, personData)
                values = input('Enter employeed ID as an integer from 1 to 100')
            except:
                print('Error, please type as integer from 1 to 100')
                sys.exit(1)

    if __name__ == '__main__':
        parser = argparse.ArgumentParser(description="URL needed")
        parser.add_argument("--url", help="The website name", type=str)
        args = parser.parse_args()

        LOG_FILENAME = "C:\\Users\\Eugen\\Desktop\\error.log"
        LOG_FORMAT = "%(message)s"
        logging.basicConfig(filename = LOG_FILENAME,
                        level = logging.ERROR,
                        format = LOG_FORMAT,
                        filemode = 'w'
                        )
        logger = logging.getLogger('assignment2')

        main()


    


    


   


