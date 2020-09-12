import pytesseract
from PIL import Image


class ImgConverter(object):
    def extract_text(self, img_path, txt_file):
        img = Image.open(img_path)
        print(img)
        pytesseract.pytesseract.tesseract_cmd = r'C:\Users\YEONSSSS\AppData\Local\Tesseract-OCR\tesseract.exe'
        result = pytesseract.image_to_string(img)

        with open(txt_file, mode='w') as file:
            file.write(result)
            print(result)

        # extract_text('text15.png')

        return txt_file


