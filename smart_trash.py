from pyzbar import pyzbar
import json
import googler
import time
import cv2
import numpy as np
import requests
import psycopg2
import threading


def get_button_cycle():
    return False

def get_button_paper():
    return False

def get_button_plastic():
    return False

def get_button_glass():
    return False

def input_type():
    while 1:
        if get_button_glass():
            return 'glass'
        if get_button_paper():
            return 'paper'
        if get_button_plastic():
            return 'plastic'

def diode_assign(state):
    if state:
        print('ASSIGN MODE')

def diode_db(state):
    if state:
        print('DB MODE')

def diode_exp(state):
    if state:
        print('EXPERIMENTAL MODE')

class SmartTrash:
    DEFAULT_TYPE = 'default'
    TRASH_MAP = {'default': 0, 'glass': 1, 'plastic': 2, 'metal': 2, 'paper': 3}
    mode = 'assign'
    def __init__(self, mode='db_only', capture_image=None, database='trash_list.json'):
        if capture_image is not None:
            self.capture = capture_image
        with open(database) as database_file:
            self.trash_types = json.load(database_file)
        self.num = 0
        self.mode = mode
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
        if self.get_trash_type(code) is None:
            self.cursor.execute(f"INSERT INTO bhl.trash_types values ({code}, \'{trash_type}\')")
        else:
            self.cursor.execute(f"UPDATE bhl.trash_types SET type=\'{trash_type}\' WHERE code={code}")
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
                print(f'current trash type: {self.get_trash_type(barcode_data)}')
                if self.mode == 'assign':
                    trash_type = self.input_type()
                    self.add_trash_type(int(barcode_data), trash_type)
                else:
                    trash_type = self.get_trash_type(int(barcode_data))
                if trash_type is None:
                    if self.mode == 'db_only':
                        trash_type = self.input_type()
                        self.add_trash_type(int(barcode_data), trash_type)
                    else:
                        trash_type = googler.get_type(f'ean: {barcode_data}')
                        self.add_trash_type(int(barcode_data), trash_type)
                if trash_type is None:
                    trash_type = self.DEFAULT_TYPE
                destination = self.TRASH_MAP[trash_type]
                self.eject(destination)

    def input_type(self):
        print('podaj typ smiecia smieciu')
        trash_type = input()
        return trash_type

    def eject(self, destination):
        print(f'going to trash car {destination}')
        time.sleep(0.5)

    def save(self, filename='trash_list.json'):
        with open(filename, 'w') as file:
            json.dump(self.trash_types, file)

def run_UI():
    while 1:
        time.sleep(0.05)
        if SmartTrash.mode == 'assign':
            diode_assign(True)
            diode_db(False)
            diode_exp(False)
        elif SmartTrash.mode == 'db_only':
            diode_assign(False)
            diode_db(True)
            diode_exp(False)
        else:
            diode_assign(False)
            diode_db(False)
            diode_exp(True)
        if get_button_cycle():
            if SmartTrash.mode == 'assign':
                SmartTrash.mode = 'db_only'
            elif SmartTrash.mode == 'db_only':
                SmartTrash.mode = 'exp'
            else:
                SmartTrash.mode = 'assign'


if __name__ == '__main__':
    mode = 'db_only'
    mode = 'assign'
    st = SmartTrash(mode)
    runner = threading.Thread(target=run_UI)
    runner.start()
    st.run()





