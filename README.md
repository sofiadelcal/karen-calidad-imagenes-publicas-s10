# Calidad de fotografías públicas
Práctica de Karen Sofía Delgado Calderon para Redes Neuronales V.

## Reproducción
Abre Karen_Calidad_Publicas.ipynb en Google Colab y elige Entorno de ejecución > Ejecutar todo. El cuaderno descarga tres imágenes públicas, registra las fuentes y genera resultados_publicos/. Para ejecución local instala requirements.txt, ejecuta descargar_publicas.py y después calidad_publicas.py.

## Método
Se corrige EXIF, se convierte a RGB y se limita el tamaño a 320×320 con proporción conservada y Lanczos. Las medidas se calculan sobre grises. Brillo es la media, contraste la desviación estándar, oscuros corresponde a intensidad <=10 y claros a intensidad >=245. Se registran además entropía y varianza del Laplaciano.

## Alcance
El análisis describe escenas fotográficas completas de condiciones diferentes. Las estadísticas dependen también de fondos, instrumentos y luces. Esta práctica de preprocesamiento constituye un avance parcial respecto de la consigna de reconocimiento facial.

## Fuentes y licencias
- **publica01**. Shakira. Autoría Marcello Casal Jr/Agência Brasil. Fecha 2014-07-12. [Shakira 2014.jpg](https://commons.wikimedia.org/wiki/File:Shakira_2014.jpg). [CC BY 3.0 BR](https://creativecommons.org/licenses/by/3.0/br/). Reducción proporcional y conversión a grises. La adaptación de publica02 conserva CC BY-SA 3.0.

- **publica02**. Juanes. Autoría Jörgens.Mi/Wikipedia. Fecha 2015-07-18. [Juanes ZMF 2015 jm49211.jpg](https://commons.wikimedia.org/wiki/File:Juanes_ZMF_2015_jm49211.jpg). [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/). Reducción proporcional y conversión a grises. La adaptación de publica02 conserva CC BY-SA 3.0.

- **publica03**. Carlos Vives. Autoría b r e n t; retoque de Resize. Fecha 2005-09-16. [Carlos Vives.jpg](https://commons.wikimedia.org/wiki/File:Carlos_Vives.jpg). [CC BY 2.0](https://creativecommons.org/licenses/by/2.0/). Reducción proporcional y conversión a grises. La adaptación de publica02 conserva CC BY-SA 3.0.

El manifiesto fuentes_publicas.json contiene URLs de origen y descarga. Las ilustraciones aplican reducción y conversión a grises. La adaptación correspondiente a publica02 conserva CC BY-SA 3.0. Las otras imágenes conservan sus licencias de atribución. El cuaderno incluye salidas de una ejecución local.
