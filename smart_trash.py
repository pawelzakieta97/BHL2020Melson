from pyzbar import pyzbar
import json
import googler
import io
import time
import cv2
import numpy as np
import requests
import psycopg2


class SmartTrash:
    DEFAULT_DESTINATION = 'default'
    TRASH_MAP = {'default': 0, 'glass' : 1, 'plastic': 2, 'metal': 2, 'paper': 3}

    def __init__(self, capture_image=None, database='trash_list.json'):
        if capture_image is not None:
            self.capture = capture_image
        with open(database) as database_file:
            self.trash_types = json.load(database_file)
        self.num = 0
        self.connection = psycopg2.connect(dbname='postgres', user='bhl', password='bhl')
        self.cursor = self.connection.cursor()

    def capture(self):
        URL = "http://192.168.0.17:8080/shot.jpg"
        img_resp = requests.get(URL)
        img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
        img = cv2.imdecode(img_arr, -1)
        height, width, channels = img.shape
        return img

    def get_trash_type(self, code):
        self.cursor.execute(f"SELECT * FROM bhl.trash_types WHERE code={code}")
        result = self.cursor.fetchone()
        if result is not None:
            return result[1]
        else:
            return None

    def add_trash_type(self, code, trash_type):
        self.cursor.execute(f"INSERT INTO bhl.trash_types values ({code}, \'{trash_type}\')")
        self.connection.commit()

    def run(self):
        i = 0
        while 1:
            image = self.capture()
            i += 1
            print('captured')
            barcodes = pyzbar.decode(image)
            if barcodes:
                barcode_data = barcodes[0].data.decode("utf-8")
                print(barcode_data)
                trash_type = self.get_trash_type(int(barcode_data))
                if trash_type is None:
                    trash_type = googler.get_type(f'ean: {barcode_data}')
                    self.add_trash_type(int(barcode_data), trash_type)
                if trash_type is None:
                    trash_type = self.DEFAULT_DESTINATION
                destination = self.TRASH_MAP[trash_type]
                self.eject(destination)

    def eject(self, destination):
        print(f'going to trash car {destination}')
        time.sleep(0.5)

    def save(self, filename='trash_list.json'):
        with open(filename, 'w') as file:
            json.dump(self.trash_types, file)

def capture():
    img = cv2.imread('images/barcode-3.jpg')

    return img


if __name__ == '__main__':
    st = SmartTrash()
    st.get_trash_type(123123123)
    st.run()





