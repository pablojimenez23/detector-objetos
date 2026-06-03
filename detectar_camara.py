import cv2
import csv
import os
from datetime import datetime
from ultralytics import YOLO
from collections import Counter

# Carga el modelo preentrenado YOLOv8
modelo = YOLO('yolov8n.pt')

# Archivo donde se guarda el historial de detecciones
ARCHIVO_HISTORIAL = 'historial_detecciones.csv'

def inicializar_historial():
    # Crea el archivo CSV con encabezados si no existe
    if not os.path.exists(ARCHIVO_HISTORIAL):
        with open(ARCHIVO_HISTORIAL, 'w', newline='', encoding='utf-8') as f:
            escritor = csv.writer(f)
            escritor.writerow(['fecha', 'hora', 'objeto', 'confianza', 'total_en_fotograma'])

def guardar_detecciones(detecciones):
    # Guarda cada deteccion del fotograma en el CSV
    ahora = datetime.now()
    fecha = ahora.strftime('%Y-%m-%d')
    hora  = ahora.strftime('%H:%M:%S')
    conteo = Counter([d['clase'] for d in detecciones])

    with open(ARCHIVO_HISTORIAL, 'a', newline='', encoding='utf-8') as f:
        escritor = csv.writer(f)
        for deteccion in detecciones:
            escritor.writerow([
                fecha,
                hora,
                deteccion['clase'],
                f"{deteccion['confianza']:.1f}%",
                conteo[deteccion['clase']]
            ])

def dibujar_conteo(fotograma, conteo):
    # Dibuja el conteo de objetos en la esquina superior derecha
    alto, ancho = fotograma.shape[:2]
    x_inicio = ancho - 220
    y_inicio = 20

    cv2.rectangle(fotograma, (x_inicio - 10, y_inicio - 15),
                  (ancho - 5, y_inicio + len(conteo) * 25 + 5),
                  (0, 0, 0), -1)

    cv2.putText(fotograma, 'Conteo:', (x_inicio, y_inicio),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    for i, (clase, cantidad) in enumerate(conteo.items()):
        texto = f'{clase}: {cantidad}'
        cv2.putText(fotograma, texto, (x_inicio, y_inicio + (i + 1) * 25),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 0), 2)

    return fotograma

# Inicializa el historial CSV
inicializar_historial()

# Inicializa la camara
camara = cv2.VideoCapture(0)

print('Detector iniciado')
print(f'Historial guardado en: {ARCHIVO_HISTORIAL}')
print('Presiona Q para salir')

intervalo_guardado = 30
fotograma_actual   = 0

while True:
    ret, fotograma = camara.read()
    if not ret:
        break

    # Deteccion de objetos en el fotograma actual
    resultados = modelo(fotograma, verbose=False)
    fotograma_anotado = resultados[0].plot()

    # Extrae las detecciones del fotograma
    detecciones = []
    for caja in resultados[0].boxes:
        clase     = modelo.names[int(caja.cls)]
        confianza = float(caja.conf) * 100
        detecciones.append({'clase': clase, 'confianza': confianza})

    # Calcula el conteo por clase
    conteo = Counter([d['clase'] for d in detecciones])

    # Dibuja el conteo en pantalla
    fotograma_anotado = dibujar_conteo(fotograma_anotado, conteo)

    # Guarda en CSV cada cierto numero de fotogramas
    if fotograma_actual % intervalo_guardado == 0 and detecciones:
        guardar_detecciones(detecciones)

    fotograma_actual += 1
    cv2.imshow('Detector de Objetos en Tiempo Real', fotograma_anotado)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camara.release()
cv2.destroyAllWindows()
print(f'\nSesion finalizada. Historial guardado en: {ARCHIVO_HISTORIAL}')