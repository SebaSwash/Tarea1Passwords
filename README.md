## Tarea 1 - Criptografía y Seguridad en Redes (CIT-2105)
--- 

Automatización de registro de cuenta, inicio de sesión, recuperación de cuenta y modificación de contraseña.

### Herramientas utilizadas
1. Python 3.8
2. Selenium

### Consideraciones importantes
---
1. Todas las funcionalidades fueron probadas y deberían funcionar sin problema. A veces se detecta que el navegador no logra cargar en el tiempo establecido en el código y el proceso comienza a buscar elementos que aún no cargan, tirando error. Para solucionarlo, intentar nuevamente la ejecución o modificar los segundos en los implicit wait o time.sleep.
   
2. Se utilizan las siguientes librerías de Python:
   1. Selenium (pip install selenium)
   2. os (pip install os)
   3. time (pip install time)
   4. random (pip install random)

3. El código está configurado para trabajar con el driver de Chrome v85. La ruta de la ubicación del archivo se encuentra en la función **configurar_driver()**, en la **línea 13** de cada código.

4. Los códigos están separados por sitio, para el caso del **sitio nacional**, el archivo corresponde a **sitio_cl.py**. Para el **sistema europeo**, el archivo es **sitio_uk.py**

5. Cada uno de los códigos funciona con un menú e interacción con el usuario para poder visualizar de buena forma la automatización en cada uno de los formularios.



