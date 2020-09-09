import os,random,time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

# ============= Tarea 1 - Criptografía y Seguridad en Redes =============
# Sebastián Ignacio Toro Severino
# Página automatizada: https://contrapunto.cl/
# =======================================================================

def configurar_driver():
    driver_dir = str(os.path.normpath(os.path.join(os.getcwd(),"WebDrivers\\chromedriver.exe")))
    driver = webdriver.Chrome(driver_dir)
    return driver

def autentificacion_login(driver,identificador_usuario,password_usuario,redirect_login=False):

    if redirect_login:
        driver.implicitly_wait(8) 
        # Se redirecciona desde la página principal al formulario de login
        boton_redirect_login = driver.find_element_by_class_name("col-mobile-btn-account").find_element_by_class_name("m-nav-btn")
        driver.execute_script("arguments[0].click();", boton_redirect_login)

    # Elementos HTML
    elemento_identificador_usuario = driver.find_element_by_name("email")
    elemento_identificador_usuario.clear() # Se limpia el input del email
    elemento_identificador_usuario.send_keys(identificador_usuario)

    elemento_password = driver.find_element_by_name("password")
    elemento_password.clear() # Se limpia el input de la password
    elemento_password.send_keys(password_usuario)

    elemento_boton_login = driver.find_element_by_id("submit-login")
    elemento_boton_login.submit()

def iniciar_sesion(password_actual=None):
    url_sitio = "https://contrapunto.cl"
    # Inicio de sesión único o iterado para fuerza bruta
    op_inicio = input("[1] Inicio de sesión único | [2] Inicio de sesión por fuerza bruta: ")

    while op_inicio not in ["1","2"]:
        op_inicio = input("[1] Inicio de sesión único | [2] Inicio de sesión por fuerza bruta: ")
    op_inicio = int(op_inicio)

    # Se solicitan las credenciales
    identificador_usuario = input("[Inicio de sesión] Email: ")
    if op_inicio == 1:
        if password_actual is None:
            password_usuario = input("[Inicio de sesión] Password: ")
        else:
            password_usuario = password_actual

    # Configuración del driver
    driver = configurar_driver()
    driver.get(url_sitio)

    if op_inicio == 1:
        # Interacción con el formulario
        autentificacion_login(driver,identificador_usuario,password_usuario,redirect_login=True)

    else: # Iterativo
        n_iteraciones = input("Cantidad de iteraciones: ")
        while n_iteraciones.isnumeric() is not True:
            n_iteraciones = input("Cantidad de iteraciones: ")

        for i in range(int(n_iteraciones)):
            # Interacción con el formulario
            # Generación de pass aleatoria
            lista_chars = "abcdefghijklmnñopqrstuvwxyz0123456789ABCDEFGHIJKLMNÑOPQRSTUVWXYZ!#$%&/()=?¡[]_:;,´^]"
            largo_pwd = random.randint(5,random.randint(6,255))
            pwd_auth = ""
            for j in range(largo_pwd):
                pwd_auth += lista_chars[random.randint(0,len(lista_chars)-1)]
            
            if i == 0:
                # Se utiliza el redireccionamiento desde la vista principal al login
                autentificacion_login(driver,identificador_usuario,pwd_auth,redirect_login=True)
            else:
                autentificacion_login(driver,identificador_usuario,pwd_auth)
            print("* Num. de intentos: "+str(i+1)+"")
    
    return driver

def crear_cuenta():
    # Datos para creación de cuenta
    genero = input("[Creación de cuenta] [1] Masculino | [2] Femenino: ")
    while genero not in ["1","2"]:
       genero = input("[Creación de cuenta] [1] Masculino | [2] Femenino: ")

    nombres = input("[Creación de cuenta] Nombres: ")
    apellidos = input("[Creación de cuenta] Apellidos: ")
    email = input("[Creación de cuenta] Email: ")
    password = input("[Creación de cuenta] Password: ")
    birthday = input("[Creación de cuenta] Fecha de cumpleaños (dd/mm/aaaa): ")

    url_sitio = "https://contrapunto.cl"
    # Configuración del driver
    driver = configurar_driver()
    driver.get(url_sitio)

    driver.implicitly_wait(10) 
    # Se redirecciona desde la página principal de login y registro
    boton_redirect_login = driver.find_element_by_class_name("col-mobile-btn-account").find_element_by_class_name("m-nav-btn")
    driver.execute_script("arguments[0].click();", boton_redirect_login)

    # Se redirecciona nuevamente al formulario de registro de cuenta
    driver.implicitly_wait(10) 
    driver.find_element_by_xpath("//a[@class='btn btn-secondary']").click()

    # Input radio masculino / femenino
    # Ambos elementos html son 'id_gender', por lo tanto marcará el masculino por default (primero en el archivo html)
    elemento_genero = driver.find_element(By.XPATH, '//input[@name="id_gender" and @value='+genero+']')
    elemento_genero.click()

    elemento_nombre = driver.find_element_by_name("firstname")
    elemento_nombre.send_keys(nombres)

    elemento_apellido = driver.find_element_by_name("lastname")
    elemento_apellido.send_keys(apellidos)

    elemento_email = driver.find_element_by_name("email")
    elemento_email.send_keys(email)

    elemento_password = driver.find_element_by_name("password")
    elemento_password.send_keys(password)

    elemento_birthday = driver.find_element_by_name("birthday")
    elemento_birthday.send_keys(birthday)

    elemento_boton_registrar = driver.find_element_by_class_name("form-control-submit")
    elemento_boton_registrar.submit()

def recuperacion_password():

    email_usuario = input("[Recuperación de password] Email: ")

    url_sitio = "https://contrapunto.cl"
    # Configuración del driver
    driver = configurar_driver()
    driver.get(url_sitio)

    driver.implicitly_wait(10) 
    # Se redirecciona desde la página principal de login y registro
    boton_redirect_login = driver.find_element_by_class_name("col-mobile-btn-account").find_element_by_class_name("m-nav-btn")
    driver.execute_script("arguments[0].click();", boton_redirect_login)

    # Se redirecciona a la sección del formulario de recuperar contraseña
    # click en '¿Olvidó su contraseña?'
    driver.find_element_by_class_name("forgot-password").find_element_by_tag_name("a").click()

    elemento_email = driver.find_element_by_id("email")
    elemento_email.send_keys(email_usuario)

    # Se envía el formulario
    driver.find_element(By.XPATH, '//button[@type="submit" and @class="form-control-submit btn btn-primary"]').click()

def modificar_password():
    # Input para contraseña actual
    password_actual = input("[Modificación de password] Password actual: ")
    # Input para nueva contraseña
    password_nueva = input("[Modificación de password] Password nueva: ")

    # Modificación de password desde el interior de la cuenta
    driver = iniciar_sesion(password_actual)

    # Al cargar el menú luego de iniciar sesión, se ingresa a la sección
    # de 'Mis datos personales y claves'
    driver.find_element_by_id("identity-link").click()

    # Una vez cargado el formulario de datos personales, se modifica.
    # Se modifica sólo la password, los demás datos se dejan intactos
    elemento_password_actual = driver.find_element_by_name("password")
    elemento_password_actual.send_keys(password_actual)

    elemento_password_nueva = driver.find_element_by_name("new_password")
    elemento_password_nueva.send_keys(password_nueva)

    elemento_boton_guardar = driver.find_element_by_class_name("form-control-submit")
    elemento_boton_guardar.submit()

def menu():
    print("** Al terminar una de las operaciones cerrar el navegador")
    print("-------------------------------------")
    print("[1] Registrar nueva cuenta")
    print("[2] Iniciar sesión")
    print("[3] Recuperar password")
    print("[4] Modificar password")
    print("[5] Salir")
    print("-------------------------------------")

if __name__ == "__main__":
    while True:
        menu()
        op = input("Selecciona una opción: ")
        while op not in ["1","2","3","4","5"]:
            op = input("Selecciona una opción [1,2,3,4]: ")
        op = int(op)

        if op == 1:
            crear_cuenta()
        elif op == 2:
            iniciar_sesion()
        elif op == 3:
            recuperacion_password()
        elif op == 4:
            modificar_password()
        else:
            break