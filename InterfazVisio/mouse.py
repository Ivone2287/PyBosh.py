

import cv2
import numpy as np

#variables para almacenar los puntos
top_left_corner=[]
bottom_right_corner=[]

#funcion para crear rectangulo
def drawRectangle(action, x,y, flags, params):
    #variables globales
    global top_left_corner, bottom_right_corner
    #Marca el punto arriba-izquierda cuando se presiona el boton izq del mouse
    if action==cv2.EVENT_LBUTTONDOWN:
        top_left_corner= [(x,y)]
    elif action==cv2.EVENT_LBUTTONUP:
        bottom_right_corner=[(x,y)]
        cv2.rectangle(image, top_left_corner[0], bottom_right_corner[0], (0,255,0),2,8)
        cv2.imshow("Ventana-Crop", image)
    pointA = top_left_corner
    pointB = bottom_right_corner
    print(pointA)
    print(pointB)


#llamar al mouse v2.setMouseCallback(winname, onMouse, userdata)


##leer imagen para segmentar
image= cv2.imread("C:/Users/6hs8de/Desktop/DataAumentada/SpotT1.jpg")
##crear una imagen temporal
temp=image.copy()
#crear una ventana
cv2.namedWindow("Ventana-Crop")
#llamar la ventana cuando ocurra el evento
cv2.setMouseCallback("Ventana-Crop", drawRectangle)




#Display Loop antes de presionar la letra 'q' del codigo asciii
k=0
while k!=113:
    cv2.imshow("Ventana-Crop", image)
    k=cv2.waitKey(0)
    if (k==99):
        image=temp.copy()
        cv2.imshow("Ventana-Crop", image)
cv2.destroyAllWindows()









