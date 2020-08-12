import cv2
import pytesseract
from PIL import Image
import sys
from pdf2image import convert_from_path




pytesseract.pytesseract.tesseract_cmd= r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# reading from image file
#img = cv2.imread("photo.png")
#text = pytesseract.image_to_string(img)
#cv2.waitKey(0);

#reading from pdf file

pdf_file = sys.argv[1]
print('PDF PATH IS: '+ pdf_file)

pages = convert_from_path(pdf_file, poppler_path=r'C:\Program Files\poppler-0.68.0_x86\poppler-0.68.0\bin')

img_counter=1

for page in pages:
    filename = "page_"+str(img_counter)+".jpg"
    page.save(filename,'JPEG')
    img_counter+=1

file_limit = img_counter-1

output = "out_text.txt"

f = open(output,"w")

for i in range(1,file_limit+1):
    filename = "page_"+str(i)+".jpg"
    text = str(((pytesseract.image_to_string(Image.open(filename)))))
    f.write(text)
f.close()

log = open("out_text.txt")

for line in log:
    print(line)