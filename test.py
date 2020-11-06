import cv2
from pyzbar import pyzbar

if __name__ == "__main__":
    barcodes = ['images/barcode-3.jpg']
    for barcode_file in barcodes:
        # load the image to opencv
        img = cv2.imread(barcode_file)
        # decode detected barcodes & get the image
        # that is drawn
        img = pyzbar.decode(img)
        # show the image
        cv2.imshow("img", img)
        cv2.waitKey(0)