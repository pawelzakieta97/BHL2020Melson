from pyzbar import pyzbar

class SmartTrash:
    def __init__(self, capture_image):
        self.capture_image = capture_image

    def run(self):
        while 1:
            img = self.capture_image()
            detected_barcodes = pyzbar.decode(img)
            if detected_barcodes:
                barcodeData = detected_barcodes[0].data.decode("utf-8")
                
