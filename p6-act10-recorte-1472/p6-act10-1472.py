import numpy as np
import cv2

# vision artificial act10 nc 1472

# Posición de la ventana en pantalla (x: más a la derecha, y: distancia desde arriba)
pos_x = 600
pos_y = 100

# 1. PEONIA
img_peonia = cv2.imread("peoniia.jpg", cv2.IMREAD_GRAYSCALE)

if img_peonia is not None:
    img_peonia = cv2.resize(img_peonia, (300, 300))
else:
    img_peonia = np.zeros((300, 300), np.uint8)

print("+-+-+-+-+Peonia+-+-+-+-")
cv2.imshow("peonia 1472", img_peonia)
cv2.moveWindow("peonia 1472", pos_x, pos_y)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 2. CIRCULO
print("el circulo 1472")
img = np.zeros((300, 300, 3), np.uint8)
img = cv2.circle(img, (150, 150), 60, (255, 255, 255), 3)

cv2.imshow("circulo 1472", img)
cv2.moveWindow("circulo 1472", pos_x, pos_y)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 3. LINEA
print("la linea 1472")
img = np.zeros((300, 300, 3), np.uint8)
img = cv2.line(img, (0, 0), (299, 299), (255, 255, 255), 3)

cv2.imshow("linea 1472", img)
cv2.moveWindow("linea 1472", pos_x, pos_y)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 4. NOMBRE
print("el nombre 1472")
img = np.zeros((300, 300, 3), np.uint8)
img = cv2.putText(img, "jose alberto solis porras", (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

cv2.imshow("nombre 1472", img)
cv2.moveWindow("nombre 1472", pos_x, pos_y)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 5. TEXTO
print("el texto 1472")
img = np.zeros((300, 300, 3), np.uint8)
img = cv2.putText(img, "Vision Artificial 1472", (20, 150), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

cv2.imshow("texto 1472", img)
cv2.moveWindow("texto 1472", pos_x, pos_y)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 6. THRESHOLDING
print("el thresholding 1472")
_, img_thresh = cv2.threshold(img_peonia, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("thresholding 1472", img_thresh)
cv2.moveWindow("thresholding 1472", pos_x, pos_y)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 7. TRACKBAR
print("el trackbar 1472")

def nada(x):
    pass

cv2.namedWindow("trackbar 1472")
cv2.moveWindow("trackbar 1472", pos_x, pos_y)
cv2.createTrackbar("Umbral", "trackbar 1472", 127, 255, nada)

while True:
    val = cv2.getTrackbarPos("Umbral", "trackbar 1472")
    _, img_tb = cv2.threshold(img_peonia, val, 255, cv2.THRESH_BINARY)
    cv2.imshow("trackbar 1472", img_tb)
    
    if cv2.waitKey(1) != -1:
        break

cv2.destroyAllWindows()

print("jose solis nc 1472")