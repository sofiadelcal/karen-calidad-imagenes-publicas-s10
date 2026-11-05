# Aprendizaje métrico y calidad de imágenes
Práctica de Karen Sofía Delgado Calderon para Redes Neuronales V.

## Reproducción
Abre Karen_Calidad_Publicas.ipynb en Google Colab y elige Entorno de ejecución > Ejecutar todo. El cuaderno descarga tres imágenes públicas, registra las fuentes y genera resultados_publicos/. Para ejecución local instala requirements.txt, ejecuta descargar_publicas.py y después calidad_publicas.py.

## Método
Se corrige EXIF, se convierte a RGB y se limita el tamaño a 320×320 con proporción conservada y Lanczos. Las medidas se calculan sobre grises. Brillo es la media, contraste la desviación estándar, oscuros corresponde a intensidad <=10 y claros a intensidad >=245. Se registran además entropía y varianza del Laplaciano.

## Alcance
El análisis describe escenas fotográficas completas de condiciones diferentes. Las estadísticas dependen también de fondos, instrumentos y luces. Esta práctica de preprocesamiento constituye un avance parcial respecto de la consigna de reconocimiento facial.

## Fuentes y licencias
- **publica01**. Shakira. Autoría Marcello Casal Jr/Agência Brasil. Fecha 2014-07-12. [Shakira 2014.jpg](https://commons.wikimedia.org/wiki/File:Shakira_2014.jpg). [CC BY 3.0 BR](https://creativecommons.org/licenses/by/3.0/br/). Reducción proporcional y conversión a grises. 

- **publica02**. Juanes. Autoría Jörgens.Mi/Wikipedia. Fecha 2015-07-18. [Juanes ZMF 2015 jm49211.jpg](https://commons.wikimedia.org/wiki/File:Juanes_ZMF_2015_jm49211.jpg). [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/). Reducción proporcional y conversión a grises. 

- **publica03**. Carlos Vives. Autoría b r e n t; retoque de Resize. Fecha 2005-09-16. [Carlos Vives.jpg](https://commons.wikimedia.org/wiki/File:Carlos_Vives.jpg). [CC BY 2.0](https://creativecommons.org/licenses/by/2.0/). Reducción proporcional y conversión a grises. 

El manifiesto fuentes_publicas.json contiene URLs de origen y descarga. Las ilustraciones aplican reducción y conversión a grises. La adaptación correspondiente a publica02 conserva CC BY-SA 3.0. Las otras imágenes conservan sus licencias de atribución. El cuaderno incluye salidas de una ejecución local.

## Adaptación con dígitos
Karen_Siamesa_Digitos.ipynb entrena un codificador compartido con Triplet Loss y compara píxeles normalizados frente a representaciones aprendidas. Ajuste con clases 0–4, calibración con 5–6 y prueba con 7–9, usando 20 episodios de una y cinco referencias. Las consultas pueden repetirse entre episodios. La red logra 60,58 % y 74,33 % de exactitud media; píxeles logra 75,08 % y 91,33 %. resumen_metrica.json conserva recuentos y parámetros. El informe explica los errores y límites. La aceptación de la adaptación respecto al requisito facial depende de la profesora.


## Evidencias y lectura del informe
El PDF Karen_Redes_V_Adaptacion_APA.pdf contiene la arquitectura, la partición de clases, las condiciones de evaluación, las tablas y el código completo. evidencia_colab_metrica.png documenta una ejecución en Google Colab que reproduce las cifras locales.

La exactitud elige el prototipo más cercano en clasificación cerrada. FAR y FRR usan los umbrales elegidos en calibración; son medidas distintas. La caída de Triplet Loss no implica mejor generalización. Los 20 episodios reutilizan imágenes y no sustituyen repeticiones independientes del entrenamiento.
