import cv2  
import tkinter as tk 
from pyzbar import pyzbar 



 
root = tk.Tk()
root.title('TSH Project')
root.geometry('800x600')
root.configure(background="#000066")

frame1 = tk.Frame(root, bg = "#000099", bd = 10)
frame1.place( relx = 0.5 , rely = 0.08 , relwidth =0.92 , relheight = 0.9 ,  anchor = "n" )



def Read_barcodes(frame): 
    barcodes = pyzbar.decode(frame) 
    for barcode in barcodes: 
        x, y, w, h = barcode.rect  
        barcode_info = barcode.data.decode('utf-8')     
         
        font = cv2.FONT_HERSHEY_SIMPLEX 
        cv2.putText(frame, barcode_info, (x+6, y-6), font, 0.9, (255,255,255),2) 
         
    return frame 

 
cap = cv2.VideoCapture(0) 
while True: 
    ret, frame = cap.read() 
    frame = Read_barcodes(frame) 
    cv2.imshow('The QR code reader', frame) 
    if cv2.waitKey(1) & 0xff == ord("q"): 
        break 

cap.release() 
cv2.destroyAllWindows()












button1 = tk.Button(frame1 , text = "Search" , bg = "red" , font = 15, width = 11 , height =3)
button1.place(x = 290 ,y =230)
button1.config(command=click)


root.mainloop()