from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

chromedriver_path = '/home/bennet/.wdm/drivers/chromedriver/linux64/114.0.5735.90/chromedriver' 
# Initialisiere den Webdriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# URL der Webseite
url = 'https://auktionen.restlos.com/auktionen/-/1134/Betriebsaufgabe-Villa-Borgnis-/lose/348030/Edelstahlhangeregal-ohne-Inhalt'

# Lade die Seite
driver.get(url)

# Warte 3 Sekunden, damit alle Inhalte geladen werden können
time.sleep(3)

# Extrahiere den gesamten Seiteninhalt
page_content = driver.page_source

# Verarbeite den Inhalt weiter
print('page wurde geladen')

# Definiere den Inhalt, den du speichern möchtest

text_content = page_content

with open('example_file.txt', 'w') as file:
    file.write(text_content)

# Schließe den Webdriver
driver.quit()
