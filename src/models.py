import os
import csv
import codecs
import logging
from datetime import time

def get_csv(path):
    with codecs.open(path, encoding="cp1251") as file:
        reader = csv.reader(file, delimiter=';', dialect='excel')
        data = [x for x in reader]
        return data

class Mock:
    def __init__(self):
        self.id = 1
        self.place = 29
        self.category = "M40+"
        self.last_name = "Константинов"
        self.first_name = "Константин"
        self.club = "Цепная Реакция"
        self.race_number = 55
        self.distance = 57
        self.time = time(hour=3, minute=24)

    @classmethod
    def get(cls, *args, **kwargs):
        return cls()
    
class XCM_osenniy:
    data = get_csv(os.getcwd() + "/src/data/xcm_osenniy_2023/data.csv")
    logging.debug(f"Data loaded: {data}")
    logging.info(f"Results for XCM Osenniy loaded: {len(data)}")

    @classmethod
    def get(cls,id):
        try:
            row = cls.data[id]
            instance = cls()
            instance.id = id
            instance.place = row[0]
            instance.category = row[4]
            instance.last_name = row[1]
            instance.first_name = row[2]
            instance.club = "Цепная Реакция"
            instance.race_number = row[6]
            instance.distance = row[5]
            instance.time = row[7]

            return instance
        except Exception:
            logging.exception(f"Could not load result {id}")

class Triathlon:
    data = get_csv(os.getcwd() + "/src/data/triathlon/data.csv")
    logging.debug(f"Data loaded: {data}")
    logging.info(f"Results for Triathlon loaded: {len(data)}")

    @classmethod
    def get(cls,id):
        try:
            row = cls.data[id-1]
            instance = cls()
            instance.id = id
            instance.event = row[0]
            instance.event_detail = row[1]
            instance.distance = row[2]
            instance.category = row[3]
            instance.place = row[4]
            instance.number = row[5]
            instance.names = row[6].split(",")
            instance.result = row[-1]
            return instance
        except Exception:
            logging.exception(f"Could not load result {id}")