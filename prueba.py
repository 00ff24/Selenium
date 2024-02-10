from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time

# Ruta al controlador del navegador (ajusta según tu ubicación)
chrome_driver_path = "C:/Users/desarrollador/Desktop/chromedriver-win64/chromedriver.exe"

# Configurar las opciones del navegador (Brave)
chrome_options = webdriver.ChromeOptions()
#chrome_options.binary_location = r"C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"  # Ruta al ejecutable de Brave
chrome_options.binary_location = r"C:/Program Files/Google/Chrome/Application/chrome.exe"  # Ruta al ejecutable de Chrome

# Configurar el controlador del navegador
chrome_options.add_argument(f"webdriver.chrome.driver:{chrome_driver_path}")
driver = webdriver.Chrome(options=chrome_options)


# Abrir una página web de ejemplo
driver.maximize_window()
driver.get("https://ppa9vrsatcop.anh.gob.bo:9943/M201O8012V4/Sitio/Persona/wfAutenticacion.aspx")
wait = WebDriverWait(driver, 10)
print("Se cargo la pagina de octano con éxito")

wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div/div/form/table/tbody/tr/td/div[1]/input")))

input_element = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div/form/table/tbody/tr/td/div[1]/input")
input_element.send_keys("refrigas.srl@hotmail.com")

print("Coloco los datos del usuario")

input_element = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div/form/table/tbody/tr/td/div[2]/input")
input_element.send_keys("refrigas")
input_element.send_keys(Keys.ENTER)

print("Le doy enter y espero que cargue la pagina, despues que cargue le dare a detalles")

driver.get("https://ppa9vrsatcop.anh.gob.bo:9943/M201O8012V4/Sitio/Movimientos/WFFlujoOperador.aspx")

print("Aqui ya cargo la pagina de los detalles")


############################################################################ ESTO ES COMUN DESPLIEGO LA LISTA DE LAS SUCURSALES DE LOS DIFERENTES COMBUSTIBLES ##################################################################
print("Despliego el combustible en la barra lateral(LIQUIDO)")

wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/form/div[3]/div[2]/div/div/div/div[1]/table/tbody/tr[2]/td/table/tbody/tr/td[1]/div/table/tbody/tr[8]/td/table[1]/tbody/tr/td/table[1]/tbody/tr[1]/td[1]/img")))
input_element = driver.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/div/div/div/div[1]/table/tbody/tr[2]/td/table/tbody/tr/td[1]/div/table/tbody/tr[8]/td/table[1]/tbody/tr/td/table[1]/tbody/tr[1]/td[1]/img")
input_element.click()


wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/form/div[3]/div[2]/div/div/div/div[1]/table/tbody/tr[2]/td/table/tbody/tr/td[1]/div/table/tbody/tr[8]/td/table[1]/tbody/tr/td/table[1]/tbody/tr[2]/td[2]/img")))
input_element = driver.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/div/div/div/div[1]/table/tbody/tr[2]/td/table/tbody/tr/td[1]/div/table/tbody/tr[8]/td/table[1]/tbody/tr/td/table[1]/tbody/tr[2]/td[2]/img")
input_element.click()

print("Despliego el combustible en la barra lateral(GNV)")

wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/form/div[3]/div[2]/div/div/div/div[1]/table/tbody/tr[2]/td/table/tbody/tr/td[1]/div/table/tbody/tr[8]/td/table[1]/tbody/tr/td/table[1]/tbody/tr[4]/td[1]/img")))
input_element = driver.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/div/div/div/div[1]/table/tbody/tr[2]/td/table/tbody/tr/td[1]/div/table/tbody/tr[8]/td/table[1]/tbody/tr/td/table[1]/tbody/tr[4]/td[1]/img")
input_element.click()


wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/form/div[3]/div[2]/div/div/div/div[1]/table/tbody/tr[2]/td/table/tbody/tr/td[1]/div/table/tbody/tr[8]/td/table[1]/tbody/tr/td/table[1]/tbody/tr[5]/td[2]/img")))
input_element = driver.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/div/div/div/div[1]/table/tbody/tr[2]/td/table/tbody/tr/td[1]/div/table/tbody/tr[8]/td/table[1]/tbody/tr/td/table[1]/tbody/tr[5]/td[2]/img")
input_element.click()
############################################################################ ESTO ES COMUN DESPLIEGO LA LISTA DE LAS SUCURSALES DE LOS DIFERENTES COMBUSTIBLES ###################################################################



############################################################################ TENGO QUE ELEGIR SI QUIERO DAR CLICK Y MOSTRAR LIQUIDO O GNV ####################################################################################
#print("Hago click sobre la primera sucursal (Liquido)")
#wait = WebDriverWait(driver, 10)
#wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/form/div[3]/div[2]/div/div/div/div[1]/table/tbody/tr[2]/td/table/tbody/tr/td[1]/div/table/tbody/tr[8]/td/table[1]/tbody/tr/td/table[1]/tbody/tr[3]/td[4]")))
#input_element = driver.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/div/div/div/div[1]/table/tbody/tr[2]/td/table/tbody/tr/td[1]/div/table/tbody/tr[8]/td/table[1]/tbody/tr/td/table[1]/tbody/tr[3]/td[4]")
#input_element.click()

print("Hago click sobre la primera sucursal (Gnv)")

wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/form/div[3]/div[2]/div/div/div/div[1]/table/tbody/tr[2]/td/table/tbody/tr/td[1]/div/table/tbody/tr[8]/td/table[1]/tbody/tr/td/table[1]/tbody/tr[6]/td[4]")))
input_element = driver.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/div/div/div/div[1]/table/tbody/tr[2]/td/table/tbody/tr/td[1]/div/table/tbody/tr[8]/td/table[1]/tbody/tr/td/table[1]/tbody/tr[6]/td[4]")
input_element.click()
############################################################################ TENGO QUE ELEGIR SI QUIERO DAR CLICK Y MOSTRAR LIQUIDO O GNV ####################################################################################




############################################################################ SELECCIONANDO EL MES ESTO ES COMUN, SOLO DEBO CAMBIAR EL MES SELECCIONADO ####################################################################################
print("Ahora tengo que seleccionar el mes")
print("Click para desplegar la lista de meses")
wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/form/div[3]/div[2]/div/div/div/div[1]/table/tbody/tr[2]/td/table/tbody/tr/td[1]/div/table/tbody/tr[3]/td/div/table/tbody/tr/td/table/tbody/tr/td[2]/img")))
input_element = driver.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/div/div/div/div[1]/table/tbody/tr[2]/td/table/tbody/tr/td[1]/div/table/tbody/tr[3]/td/div/table/tbody/tr/td/table/tbody/tr/td[2]/img")
input_element.click()
time.sleep(1)
print("Seleeciono enero")
#wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/form/div[3]/div[2]/div/div/div/div[1]/table/tbody/tr[2]/td/table/tbody/tr/td[1]/div/table/tbody/tr[3]/td/div/table/tbody/tr/td/div/div/div/div/div/table[2]/tbody/tr[1]/td[1]/a/span")))
input_element = driver.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/div/div/div/div[1]/table/tbody/tr[2]/td/table/tbody/tr/td[1]/div/table/tbody/tr[3]/td/div/table/tbody/tr/td/div/div/div/div/div/table[2]/tbody/tr[1]/td[1]/a/span")
print("click para seleccionar enero")
input_element.click()

input_element = driver.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/div/div/div/div[1]/table/tbody/tr[2]/td/table/tbody/tr/td[1]/div/table/tbody/tr[4]/td/div/div/span")
print("Click para que cargue el mes")
input_element.click()
############################################################################ SELECCIONANDO EL MES ESTO ES COMUN, SOLO DEBO CAMBIAR EL MES SELECCIONADO ####################################################################################




############################################################################ TENGO QUE ELEGIR SI QUIERO DESPLEGAR EL PLIMER COMBUSTIBLE DO GE+ GE SE92 GNV ####################################################################################

#wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/form/div[3]/div[2]/div/div/div/div[1]/table/tbody/tr[2]/td/table/tbody/tr/td[3]/div/div[1]/table/tbody/tr[5]/td/div/div/div[1]/div/table/tbody/tr[2]/td/table/tbody/tr/td/table[1]/tbody/tr[3]/td[1]/img")))
#input_element = driver.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/div/div/div/div[1]/table/tbody/tr[2]/td/table/tbody/tr/td[3]/div/div[1]/table/tbody/tr[5]/td/div/div/div[1]/div/table/tbody/tr[2]/td/table/tbody/tr/td/table[1]/tbody/tr[3]/td[1]/img")
#input_element.click()


print("Hago click sobre COMBUSTIBLE Gnv para desplegar los dias)")
time.sleep(2)
wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/form/div[3]/div[2]/div/div/div/div[1]/table/tbody/tr[2]/td/table/tbody/tr/td[3]/div/div[1]/table/tbody/tr[5]/td/div/div/div[1]/div/table/tbody/tr[2]/td/table/tbody/tr/td/table[1]/tbody/tr[3]/td[1]/img")))
input_element = driver.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/div/div/div/div[1]/table/tbody/tr[2]/td/table/tbody/tr/td[3]/div/div[1]/table/tbody/tr[5]/td/div/div/div[1]/div/table/tbody/tr[2]/td/table/tbody/tr/td/table[1]/tbody/tr[3]/td[1]/img")
input_element.click()
############################################################################ TENGO QUE ELEGIR SI QUIERO DESPLEGAR EL PLIMER COMBUSTIBLE DO GE+ GE SE92 ETC ####################################################################################


print("Hago click sobre COMBUSTIBLE Gnv 1 dia)")
time.sleep(2)
wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/form/div[3]/div[2]/div/div/div/div[1]/table/tbody/tr[2]/td/table/tbody/tr/td[3]/div/div[1]/table/tbody/tr[5]/td/div/div/div[1]/div/table/tbody/tr[2]/td/table/tbody/tr/td/table[1]/tbody/tr[4]")))
input_element = driver.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/div/div/div/div[1]/table/tbody/tr[2]/td/table/tbody/tr/td[3]/div/div[1]/table/tbody/tr[5]/td/div/div/div[1]/div/table/tbody/tr[2]/td/table/tbody/tr/td/table[1]/tbody/tr[4]/td[1]")
input_element.click()

print("Hago doble click sobre COMBUSTIBLE Gnv 1 dia)")
time.sleep(2)
wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/form/div[3]/div[2]/div/div/div/div[1]/table/tbody/tr[2]/td/table/tbody/tr/td[3]/div/div[1]/table/tbody/tr[5]/td/div/div/div[1]/div/table/tbody/tr[2]/td/table/tbody/tr/td/table[1]/tbody/tr[4]/td[3]")))
input_element = driver.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/div/div/div/div[1]/table/tbody/tr[2]/td/table/tbody/tr/td[3]/div/div[1]/table/tbody/tr[5]/td/div/div/div[1]/div/table/tbody/tr[2]/td/table/tbody/tr/td/table[1]/tbody/tr[4]/td[3]")
actions = ActionChains(driver)
actions.double_click(input_element).perform()




time.sleep(2)
print("espero que cargue la pagina donde me muestra el detalle")
wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/form/div[3]/div[2]/div/div/div/div[2]/div[2]/div/div[1]/table/tbody/tr[2]/td[1]/table/tbody/tr/td/div[2]/table/tbody/tr/td[4]")))
input_element = driver.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/div/div/div/div[2]/div[2]/div/div[1]/table/tbody/tr[2]/td[1]/table/tbody/tr/td/div[2]/table/tbody/tr/td[4]")
input_element.click()


print("Muevo el elemento fecha hacia la lista de titulos")
# Localizar el elemento de origen (puedes ajustar según tus necesidades)
elemento_origen = driver.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/div/div/div/div[2]/div[2]/div/div[1]/table/tbody/tr[2]/td[1]/table/tbody/tr/td/div[2]/table/tbody/tr/td[1]")

# Localizar el elemento de destino (puedes ajustar según tus necesidades)
elemento_destino = driver.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/div/div/div/div[2]/div[2]/div/div[1]/table/tbody/tr[2]/td[1]/table/tbody/tr/td/table[1]/tbody/tr[1]/td[4]")

# Crear una instancia de ActionChains y realizar el "drag and drop"
acciones = ActionChains(driver)
acciones.drag_and_drop(elemento_origen, elemento_destino).perform()

time.sleep(2)
print("Muevo el elemento placa hacia la lista de titulos")
# Localizar el elemento de origen (puedes ajustar según tus necesidades)
elemento_origen = driver.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/div/div/div/div[2]/div[2]/div/div[1]/table/tbody/tr[2]/td[1]/table/tbody/tr/td/div[2]/table/tbody/tr/td[1]")

# Localizar el elemento de destino (puedes ajustar según tus necesidades)
elemento_destino = driver.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/div/div/div/div[2]/div[2]/div/div[1]/table/tbody/tr[2]/td[1]/table/tbody/tr/td/table[1]/tbody/tr[1]/td[9]")
# Crear una instancia de ActionChains y realizar el "drag and drop"
acciones = ActionChains(driver)
acciones.drag_and_drop(elemento_origen, elemento_destino).perform()






####################################################################DESCARGAR EXCEL####################################################################
print("click en descargar excel")
wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/form/div[3]/div[2]/div/div/div/div[2]/div[2]/div/div[1]/table/tbody/tr[1]/td[5]/div")))
input_element = driver.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/div/div/div/div[2]/div[2]/div/div[1]/table/tbody/tr[1]/td[5]/div")
input_element.click()

alert = driver.switch_to.alert
print("Texto del cuadro de diálogo:", alert.text)
alert.accept()

####################################################################DESCARGAR EXCEL####################################################################



#click cerrar ventana de detalles
#/html/body/form/div[3]/div[2]/div/div/div/div[2]/div[1]/div[1]/img

print("Espero 5 segundos")

########Cierro ventana detalles###########
print("cierro la ventana detalles de ese dia")
wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/form/div[3]/div[2]/div/div/div/div[2]/div[1]/div[1]/img")))
input_element = driver.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/div/div/div/div[2]/div[1]/div[1]/img")
input_element.click()




print("Ahora estoy en la ventana principal")

time.sleep(5)
print("Cerrar el navegador al finalizar")
driver.quit()