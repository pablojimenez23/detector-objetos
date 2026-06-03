import cv2
from ultralytics import YOLO

# Carga el modelo preentrenado YOLOv8
modelo = YOLO('yolov8n.pt')

# Inicializa la camara
camara = cv2.VideoCapture(0)

print('Presiona Q para salir')

while True:
    ret, fotograma = camara.read()
    if not ret:
        break

    # Deteccion de objetos en el fotograma actual
    resultados = modelo(fotograma, verbose=False)

    # Dibuja los recuadros y etiquetas en el fotograma
    fotograma_anotado = resultados[0].plot()

    cv2.imshow('Detector de Objetos en Tiempo Real', fotograma_anotado)

    # Presiona Q para salir
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camara.release()
cv2.destroyAllWindows()