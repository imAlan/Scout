from elasticsearch import Elasticsearch
import MySQLdb
import logging

logging.basicConfig(level=logging.INFO)
def index_crime():
    es = Elasticsearch('http://localhost:9200/')
    db = MySQLdb.connect('localhost', 'root', 'password', 'scout')
    cur = db.cursor()
    cur.execute("SELECT * FROM precinct")
    data = cur.fetchall()
    for precinct in data:
        es.index(
                "locations",
                "point",
                {
                    "pin": {
                        "location": {
                            "lat": precinct[3],
                            "lng": precinct[4]
                        },
                        "tag": "crime",
                        "info": {"pid": precinct[0], "address": precinct[2], "borough": precinct[5]}
                    }
                }
        )

if __name__ == "__main__":
    index_crime()