import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
img = cv2.imread("./img/Lap_trinh_python.png")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
boxes = pytesseract.image_to_data(img)
print(boxes)

for x, b in enumerate(boxes.splitlines()):
    if(x!=0):
        print(b)
        b = b.split()
        if(len(b) == 12):
            print(b)
            x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_PLAIN,3,(0,0,255),2)

cv2.imshow("NHAN DANG CHU VIET",img)
cv2.waitKey()
cv2.destroyAllWindows()



