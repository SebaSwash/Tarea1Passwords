import os,time,random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

# ============= Tarea 1 - Criptografía y Seguridad en Redes =============
# Sebastián Ignacio Toro Severino
# Página automatizada: https://www.whsmith.co.uk/
# =======================================================================

def configurar_driver():
    driver_dir = str(os.path.normpath(os.path.join(os.getcwd(),"WebDrivers\\chromedriver.exe")))
    driver = webdriver.Chrome(driver_dir)
    return driver

def autentificacion_login(driver,identificador_usuario,password_usuario,redirect_login=False):

    if redirect_login:
        driver.implicitly_wait(10) 
        # Se redirecciona desde la página principal al formulario de login
        boton_redirect_login = driver.find_element_by_class_name("user-panel").find_element_by_class_name("user-login")
        driver.execute_script("arguments[0].click();", boton_redirect_login)

    driver.implicitly_wait(5) 
    
    # Elementos HTML
    elemento_email = driver.find_element_by_xpath("//input[@type='email']")
    elemento_email.clear() # Se limpia el input del email
    elemento_email.send_keys(identificador_usuario)

    elemento_password = driver.find_element_by_xpath("//input[@type='password']")
    elemento_password.clear() # Se limpia el input de la password
    elemento_password.send_keys(password_usuario)

    elemento_submit = driver.find_element_by_name("dwfrm_login_login")
    driver.execute_script("arguments[0].click();", elemento_submit)

def iniciar_sesion(password_actual=None):
    url_sitio = "https://www.whsmith.co.uk/"
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

    # Se consultan los campos antes de obtenerlos con Selenium
    nombres = input("[Creación de cuenta] Nombres: ")
    apellidos = input("[Creación de cuenta] Apellidos: ")
    email = input("[Creación de cuenta] Email: ")
    password = input("[Creación de cuenta] Password: ")

    url_sitio = "https://www.whsmith.co.uk/"
    # Configuración del driver
    driver = configurar_driver()
    driver.get(url_sitio)

    driver.implicitly_wait(10) 
    # Se redirecciona desde la página principal al formulario de login
    boton_redirect_login = driver.find_element_by_class_name("user-panel").find_elements_by_class_name("user-login")[1]
    driver.execute_script("arguments[0].click();", boton_redirect_login)

    driver.implicitly_wait(5)

    # Se rellena el formulario de creación de cuenta
    # Title aleatorio
    posibilidades_title = ["Mr","Mrs","Miss","Ms","Mx","Ind","Misc","Dr","Prof","Prefer not to say"]

    title_seleccionado = posibilidades_title[random.randint(0,len(posibilidades_title)-1)]

    elemento_li_title = driver.find_element_by_xpath("//div[@class='selectric-scroll']/ul/li[text() = '"+title_seleccionado+"']")
    driver.execute_script("arguments[0].click();",elemento_li_title)
    #//*[@id="btn"]/ul/li[2]/a/span

    # Nombres del usuario
    elemento_nombres = driver.find_element_by_id("dwfrm_profile_customer_firstname")
    elemento_nombres.send_keys(nombres)

    # Apellidos del usuario
    elemento_apellidos = driver.find_element_by_id("dwfrm_profile_customer_lastname")
    elemento_apellidos.send_keys(apellidos)

    # Correo electrónico
    elemento_email = driver.find_element_by_id("dwfrm_profile_customer_email")
    elemento_email.send_keys(email)

    # Contraseñas (contraseña y confirmación)
    elementos_passwords = driver.find_elements_by_xpath("//input[@type='password']")
    for elemento in elementos_passwords:
        elemento.send_keys(password)
    
    # Botón de confirmación de registro
    elemento_boton_submit = driver.find_element_by_name("dwfrm_profile_confirm")
    driver.execute_script("arguments[0].click();", elemento_boton_submit)

def recuperacion_password():

    email_usuario = input("[Recuperación de password] Ingresa tu email: ")

    url_sitio = "https://www.whsmith.co.uk/"
    # Configuración del driver
    driver = configurar_driver()
    driver.get(url_sitio)

    driver.implicitly_wait(10) 
    # Se redirecciona desde la página principal al formulario de login
    boton_redirect_login = driver.find_element_by_class_name("user-panel").find_element_by_class_name("user-login")
    driver.execute_script("arguments[0].click();", boton_redirect_login)

    # Se redirecciona desde el login a la sección de recuperación de contraseña
    boton_redirect_forgot_pass = driver.find_element_by_id("password-reset")
    driver.execute_script("arguments[0].click();", boton_redirect_forgot_pass)

    # Se obtiene el input de email del modal
    elemento_email_recuperacion = driver.find_element_by_id("dwfrm_requestpassword_email")
    elemento_email_recuperacion.send_keys(email_usuario)

    elemento_submit_recuperacion = driver.find_element_by_name("dwfrm_requestpassword_send")
    driver.execute_script("arguments[0].click();", elemento_submit_recuperacion)

def modificar_password():
    # Input para contraseña actual
    password_actual = input("[Modificación de password] Password actual: ")
    # Input para nueva contraseña
    password_nueva = input("[Modificación de password] Password nueva: ")

    # Modificación de password desde el interior de la cuenta
    driver = iniciar_sesion(password_actual)

    # Se navega por el perfil hasta la sección de modificación de contraseñas
    elemento_redirect_mod_pass = driver.find_element_by_xpath("//a[contains(@href,'https://www.whsmith.co.uk/on/demandware.store/Sites-whsmith-Site/en_GB/Account-EditPassword')]")
    driver.execute_script("arguments[0].click();", elemento_redirect_mod_pass)

    # Se obtienen los elementos de contraseña (contraseña actual, nueva y confirmación de la nueva)
    elementos_password = driver.find_elements_by_xpath("//input[@type='password']")
    for index_loop,elemento in enumerate(elementos_password):
        if index_loop == 0:
            # Password actual (índice 0)
            elemento.send_keys(password_actual)
        else:
            # Password nueva y confirmación (índices 1 y 2)
            elemento.send_keys(password_nueva)
        # Se esperan 2 segs para no producir problemas al llenar los datos
        time.sleep(2)
    
    elemento_submit_form = driver.find_element_by_name("dwfrm_profile_changepassword")
    driver.execute_script("arguments[0].click();", elemento_submit_form)

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