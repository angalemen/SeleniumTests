
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def HERPmes():
    driver = webdriver.Chrome()
    driver.get("https://aarricgra.github.io/")
    driver.maximize_window()
    time.sleep(1)

    Element1 = driver.find_element(By.LINK_TEXT, "CONTÁCTANOS")
    Element1.click()
    time.sleep(1)

    Element1 = driver.find_element(By.NAME, "Name")
    Element1.send_keys("Carles Vidret Gafas")
    Element1.click()
    time.sleep(1)

    Element1 = driver.find_element(By.NAME, "Email")
    Element1.send_keys("gafasylentes@gmail.com")
    Element1.click()
    time.sleep(1)

    Element1 = driver.find_element(By.NAME, "Telf")
    Element1.send_keys("634599188")
    Element1.click()
    time.sleep(1)

    Element1 = driver.find_element(By.NAME, "Subject")
    Element1.send_keys("Gru")
    Element1.click()
    time.sleep(1)

    Element1 = driver.find_element(By.NAME, "Reason")
    Element1.send_keys("Me fa mal la chufa")
    Element1.click()
    time.sleep(1)

    Element1 = driver.find_element(By.XPATH, "//button[@style='font-size: 20px;']")
    Element1.click()
    time.sleep(1)

    driver.close()

def Movistar():
    driver = webdriver.Chrome()
    driver.get('https://www.movistar.es/')
    driver.maximize_window()

    time.sleep(1)
    Element1 = driver.find_element(By.XPATH, "//button[@style='background-color:#0079bb;color:#fff;border-color:#0079bb']")
    Element1.click()
    time.sleep(1)

    Element1 = driver.find_element(By.NAME, "searcher")
    Element1.send_keys("autonomos")
    Element1.click()
    Element1.send_keys(Keys.ENTER)
    time.sleep(5)
    driver.close()

def Game():
    driver = webdriver.Chrome()
    driver.get("https://www.game.es/")
    driver.maximize_window()
    time.sleep(2)
    Element1 = driver.find_element(By.ID, "btnCookiesAcceptAll")
    Element1.click()
    time.sleep(2)
    Element1 = driver.find_element(By.ID, "searchinput")
    Element1.send_keys("Switch")
    time.sleep(5)
    Element1 = driver.find_element(By.ID, "submitsearch")
    Element1.click()
    time.sleep(4)
    Element1 = driver.find_element(By.LINK_TEXT, "Más información")
    Element1.click()
    time.sleep(2)
    Element1 = driver.find_element(By.CLASS_NAME, "product-thumbnail-anchor")
    Element1.click()
    time.sleep(2)
    Element1 = driver.find_element(By.ID, "txtRegisterNewsletter")
    Element1.send_keys("angalemen@alu.edu.gva.es")
    time.sleep(2)
    Element1 = driver.find_element(By.ID, "btnSendNewsletter")
    Element1.click()
    time.sleep(2)
    driver.close()

def MediaMark():
    driver = webdriver.Chrome()
    driver.get("https://www.mediamarkt.es/?ad-machina=79MN-10yX:4beG-10yY:8N3t~e&gad_source=1&gclid=CjwKCAiAibeuBhAAEiwAiXBoJJ1oCPjAnZ1oJ56z3LMu09vOn-JyFQMwIymTBmkuPVgtcU6huXznfxoCSoMQAvD_BwE&gclsrc=aw.ds")
    driver.maximize_window()
    time.sleep(2)

    element = driver.find_element(By.ID, "pwa-consent-layer-accept-all-button")
    element.click()
    time.sleep(2)

    element = driver.find_element(By.XPATH, "//span[text()='¿Te ayudamos?']")
    element.click()
    time.sleep(2)

    element = driver.find_element(By.ID, "rn_KeywordTextExtended_2_Text")
    element.send_keys("Proceso de Cobro")
    time.sleep(2)

    element = driver.find_element(By.ID, "rn_SearchButton_3_SubmitButton")
    element.click()
    time.sleep(2)

    element = driver.find_element(By.LINK_TEXT, "¿Cómo puedo descargar mi factura?")
    element.click()
    time.sleep(2)

    element = driver.find_element(By.CLASS_NAME, "ThumbsDown-P")
    element.click()
    time.sleep(2)

    try:
        element_present = EC.presence_of_element_located((By.LINK_TEXT, "Añadir al carrito"))
        WebDriverWait(driver, 80).until(element_present)
    except TimeoutException:
        print("No carrega la página")

    time.sleep(2)

    Element2 = driver.find_element(By.ID, '1125')
    Element2.click()
    time.sleep(1)

    Element2 = driver.find_element(By.XPATH, "//a[@target='_self']")
    Element2.click()
    time.sleep(1)

    Element2 = driver.find_element(By.XPATH, "//input[@type='text']")
    Element2.send_keys("Madrid")
    Element2.click()
    Element2.send_keys(Keys.ENTER)
    time.sleep(2)
    driver.close()

def main():
    while True:
        print("------ Menú ------")
        print("1. Formulario de contacto")
        print("2. Buscar en Movistar")
        print("3. Buscar en Game")
        print("4. Buscar en MediaMarkt")
        print("0. Salir")

        opcion = input("Selecciona una opción: ")

        opciones = {
            '1': HERPmes,
            '2': Movistar,
            '3': Game,
            '4': MediaMark,
            '0': exit
        }

        if opcion in opciones:
            opciones[opcion]()
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()







