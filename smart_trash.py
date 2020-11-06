from pyzbar import pyzbar
import json
import googler
import cv2
import time

class SmartTrash:
    DEFAULT_DESTINATION = 'default'
    TRASH_MAP = {'default': 0, 'glass' : 1, 'plastic': 2, 'metal': 2, 'paper': 3}

    def __init__(self, capture_image, database='trash_list.json'):
        self.capture_image = capture_image
        with open(database) as database_file:
            self.trash_types = json.load(database_file)

    def run(self):
        while 1:
            img = self.capture_image()
            barcodes = pyzbar.decode(img)
            if barcodes:
                barcode_data = barcodes[0].data.decode("utf-8")
                if barcode_data in self.trash_types.keys():
                    trash_type = self.trash_types[barcode_data]
                else:
                    trash_type = googler.get_type(f'ean: {barcode_data}')
                    self.trash_types[barcode_data] = trash_type
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
    st = SmartTrash(capture)
    st.run()





