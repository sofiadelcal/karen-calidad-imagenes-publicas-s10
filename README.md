# Redes Neuronales V · Karen Sofía Delgado Calderon

La práctica de la actividad 73148 compara una red siamesa con una línea base de píxeles usando las fotografías públicas de Labeled Faces in the Wild (LFW). Las identidades de ajuste, calibración y prueba forman grupos disjuntos.

El informe de entrega es Karen_Redes_V_LFW_APA.pdf. Incluye las tablas de la corrida local y la captura de la ejecución en Colab.

## Repetir el experimento

Abre Karen_Siamesa_LFW.ipynb en Google Colab y elige **Entorno de ejecución → Ejecutar todo**. La primera ejecución descarga LFW mediante scikit-learn. También puedes instalar las dependencias de requirements_lfw.txt y ejecutar siamesa_lfw.py en Python.

El script genera resumen_lfw.json y resultados_lfw.png dentro de resultados_lfw. El informe explica cómo se seleccionaron las tomas, cómo se eligieron los umbrales y cómo se calcula cada métrica.

## Resultados de referencia

| Método | Referencias | Aciertos | AUC |
|---|---:|---:|---:|
| Píxeles | 1 | 501 / 2.400 | 0,604 |
| Píxeles | 5 | 805 / 2.400 | 0,679 |
| Siamesa | 1 | 699 / 2.400 | 0,753 |
| Siamesa | 5 | 1.039 / 2.400 | 0,841 |

La galería de cinco tomas mejoró la exactitud en este protocolo. Cada consulta se compara con prototipos de 12 identidades reservadas. Una imagen puede aparecer en más de un episodio. El informe incluye las tasas de falsa aceptación y falso rechazo y detalla cómo interpretarlas.

Huang, Ramesh, Berg y Learned-Miller publicaron LFW como conjunto académico. Los recortes proceden de la variante alineada de scikit-learn. [Informe técnico de LFW](https://people.cs.umass.edu/~elm/papers/lfw.pdf) · [Documentación del cargador](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_lfw_people.html)
