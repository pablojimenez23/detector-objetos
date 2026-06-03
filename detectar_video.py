import cv2
import sys
import os
from ultralytics import YOLO

# Carga el modelo preentrenado YOLOv8
modelo = YOLO('yolov8n.pt')

def detectar(ruta_imagen):
    if not os.path.exists(ruta_imagen):
        print(f'No se encontro la imagen: {ruta_imagen}')
        return

    # Carga la imagen y ejecuta la deteccion
    imagen = cv2.imread(ruta_imagen)
    resultados = modelo(imagen, verbose=False)

    # Muestra los objetos detectados
    print(f'\nImagen: {ruta_imagen}')
    print(f'Objetos detectados: {len(resultados[0].boxes)}')
    for caja in resultados[0].boxes:
        clase = modelo.names[int(caja.cls)]
        confianza = float(caja.conf) * 100
        print(f'  {clase}: {confianza:.1f}%')

    # Guarda la imagen con las detecciones
    nombre_salida = f'resultado_{os.path.basename(ruta_imagen)}'
    fotograma_anotado = resultados[0].plot()
    cv2.imwrite(nombre_salida, fotograma_anotado)
    print(f'\nResultado guardado en: {nombre_salida}')

    # Muestra la imagen con las detecciones
    cv2.imshow('Detecciones', fotograma_anotado)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Uso: python detectar_imagen.py ruta/imagen.jpg')
    else:
        detectar(sys.argv[1])