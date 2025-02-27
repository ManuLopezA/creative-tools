#  Project Structure Generator  📂

Este script permite crear estructuras de carpetas para proyectos de forma automatizada. A continuación se detallan las **instrucciones** para ejecutarlo.  

## Requisitos:  

### 1️⃣ **Instalar Python**  
Para ejecutar este script, necesitas tener **Python** instalado en tu computadora.  

- **Descargar Python**: Ve a la página oficial de [Python](https://www.python.org/downloads/) y descarga la versión más reciente para tu sistema operativo.  
- **Durante la instalación**, asegúrate de marcar la opción **"Add python.exe to PATH"**.  

### 2️⃣ **Instalar "Project Structure Generator"**  
Copia todo el contenido de esta carpeta **`project-structure-generator/`** en el directorio donde guardarás tus proyectos.  

### 3️⃣ **Ejecutar el script**  
- **Haz doble clic** en el archivo `new_project.py`.  
- Se abrirá una terminal donde deberás ingresar el **nombre del proyecto** y seleccionar el **tipo de estructura** a utilizar.  
- Una vez completado, la terminal se cerrará automáticamente y el proyecto estará listo en la misma carpeta.  


## Modificar o añadir estructuras de carpetas  

En la carpeta **`structures/`** se encuentran los archivos que definen las estructuras de carpetas. Puedes modificarlos o añadir nuevos para personalizar tu flujo de trabajo.  

### 🔹 **Crear o modificar una estructura de carpetas**  

1. Abre la carpeta **`structures/`** donde se encuentran los archivos de las estructuras.  
2. Si deseas **modificar** una estructura de carpetas ya existente:
   - Abre el archivo de la estructura que quieras cambiar (por ejemplo, **`animation.py`**).Dentro del archivo encontrarás un código similar a este:  

   ```python
   # Nombre del tipo de proyecto
   project_type = "animation"

   # Estructura de carpetas del proyecto
   def get_structure():
       return [
           "Designs/PSDs",
           "Designs/Sprites",
           "Animations/Export",
           "Animations/PNGs",
           "Sprites",
       ]
   ```
   
   - Edita la lista de carpetas dentro de la función `get_structure()` según tus necesidades.
     

   > **Nota**: Recuerda que cada `/` simboliza una carpeta anidada dentro de la anterior.  

   Ejemplo de estructura modificada (hemos decidido añadir dos subcarpetas dentro de /PSDs):

   ```python
   def get_structure():
       return [
           "Designs/PSDs/not_valid",
           "Designs/PSDs/final",
           "Designs/Sprites",
           "Animations/Export",
           "Animations/PNGs",
           "Sprites",
       ]
   ```

3. Si deseas **crear una nueva estructura**:
   - Copia uno de los archivos existentes (por ejemplo, **`animation.py`**) y renómbralo con el nombre de la nueva estructura (por ejemplo, **`nuevo_nombre_de_estructura.py`**).
   - Dentro del archivo, cambia el valor de `project_type` por el nombre de tu nueva estructura y edita la lista de carpetas dentro de la función `get_structure()`, como se muestra en el punto anterior.

   Ejemplo:

   ```python
   # Definimos un nuevo nombre para la estructura
   project_type = "nuevo_nombre_de_estructura"

   # Define la estructura de carpetas
   def get_structure():
       return [
           "NuevaCarpeta/Subcarpeta1",
           "NuevaCarpeta/Subcarpeta2",
           "OtroTipo/Subcarpeta/Subsubcarpeta",
       ]
   ```
   **Asegúrate de que el nombre del proyecto (project_type) sea único para evitar confusiones.**

