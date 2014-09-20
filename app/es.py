import MySQLdb
import csv
from pyelasticsearch import ElasticSearch

es = ElasticSearch('http://localhost:9200/')


def importdata():
    db = MySQLdb.connect('localhost', 'root', 'password', 'scout')
    cur = db.cursor()
    with open('data/precinct_data.csv', 'rb') as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            print row
            precinct = row['precinct'].strip().split()[0][:-2]
            print precinct
            s = "INSERT INTO precinct (name, phone, address, latitude, longitude, borough) VALUES ('%s', '%s', '%s', %s, %s, '%s');" %(precinct, row['phone'].strip(), row['address'].strip(), row['lat'].strip(), row['lng'].strip(), row['borough'].strip())
            cur.execute(s)
            db.commit()

    with open('data/monthly.csv', 'rb') as mh:
        reader = csv.DictReader(mh)
        for row in reader:
            precinct = row['Precinct'].strip().split()[0][:-2]
            s = "INSERT INTO PrecinctData (name, crime, total) VALUES ('%s', '%s', %s);" %(precinct, row['Crime'].strip(), row['Total'].strip())
            cur.execute(s)
            db.commit()
    cur.close()
    db.close()

if __name__ == "__main__":
    importdata()