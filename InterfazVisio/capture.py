import cv2

# Cargar vídeo
cap = cv2.VideoCapture(0)

# Trabajamos frame a frame
while(cap.isOpened()):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # ret será verdadero mientras haya frames a trabajar y no estén corruptos.
    # (Esto es sobretodo útil cuando trabajamos vídeos)
    if ret==True:
        # Mostramos la imagen por pantalla
        cv2.imshow('frame',gray)

        # Si se pulsa una tecla guardamos su valor en 'key'
        key = cv2.waitKey(1)
        if key == 27:
            # Si queremos interrumpir el video y salir apretamos la tecla 'esc'
            # (ascii = 27)
            break
        elif key == 32:
            # Si queremos guardar frame actual apretamos tecla 'espacio' (ascii=32)
            print('Hacemos foto')
            cv2.imwrite('C:/Users/6hs8de/Desktop/imgCap.png', gray)

    else:
        break

# Liberamos el sistema
cap.release()
cv2.destroyAllWindows()