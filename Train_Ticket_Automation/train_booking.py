from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from config import USERNAME, PASSWORD, FROM_STATION, TO_STATION, DATE, PASSENGER_NAME, PASSENGER_AGE
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.irctc.co.in")
driver.maximize_window()

wait = WebDriverWait(driver, 15)
wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'LOGIN')]"))).click()
time.sleep(2)

driver.find_element(By.XPATH, "//input[@formcontrolname='userid']").send_keys(USERNAME)
driver.find_element(By.XPATH, "//input[@formcontrolname='password']").send_keys(PASSWORD)
driver.find_element(By.XPATH, "//button[text()='SIGN IN']").click()

time.sleep(5)

from_field = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@aria-label='Enter From station. Input is Mandatory.']")))
from_field.click()
from_field.send_keys(Keys.CONTROL + "a")
from_field.send_keys(Keys.DELETE)
for char in FROM_STATION:
    from_field.send_keys(char)
    time.sleep(0.2)
wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@role='option'][1]"))).click()

time.sleep(1)

to_field = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@aria-label='Enter To station. Input is Mandatory.']")))
to_field.click()
to_field.send_keys(Keys.CONTROL + "a")
to_field.send_keys(Keys.DELETE)
for char in TO_STATION:
    to_field.send_keys(char)
    time.sleep(0.2)
wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@role='option'][1]"))).click()

time.sleep(1)

date_field = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[contains(@class,'ui-inputtext') and @autocomplete='off'])[3]")))
date_field.click()
date_field.send_keys(Keys.CONTROL + "a")
date_field.send_keys(Keys.DELETE)
date_field.send_keys(DATE)

time.sleep(1)

driver.find_element(By.TAG_NAME, "body").click()
time.sleep(1)

search_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Search Trains')]")))
driver.execute_script("arguments[0].click();", search_button)

time.sleep(5)

train = wait.until(EC.visibility_of_element_located((By.XPATH, "//strong[contains(text(),'12658')]")))
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", train)

time.sleep(2)

train_card = wait.until(EC.presence_of_element_located((By.XPATH, "//strong[contains(text(),'12658')]/ancestor::app-train-avl-enq")))
ac_2a_refresh = train_card.find_element(By.XPATH, ".//strong[contains(text(),'AC 2 Tier')]/parent::div/following-sibling::div")

driver.execute_script("arguments[0].click();", ac_2a_refresh)
print("Clicked AC 2 Tier refresh")

time.sleep(2)

train_card = wait.until(EC.presence_of_element_located((By.XPATH, "//strong[contains(text(),'12658')]/ancestor::app-train-avl-enq")))
availability = train_card.find_element(By.XPATH, ".//*[contains(text(),'AVAILABLE')]")
driver.execute_script("arguments[0].click();", availability)
print("Clicked availability")

time.sleep(2)

train_card = wait.until(EC.presence_of_element_located((By.XPATH, "//strong[contains(text(),'12658')]/ancestor::app-train-avl-enq")))
book_now = train_card.find_element(By.XPATH, ".//button[contains(text(),'Book Now')]")
driver.execute_script("arguments[0].click();", book_now)
print("Clicked Book Now")

wait.until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@placeholder,'Name')]")))
driver.find_element(By.XPATH, "//input[contains(@placeholder,'Name')]").send_keys(PASSENGER_NAME)
driver.find_element(By.XPATH, "//input[contains(@placeholder,'Age')]").send_keys(PASSENGER_AGE)
gender = Select(driver.find_element(By.XPATH, "//select[contains(@formcontrolname,'passengerGender')]"))
gender.select_by_visible_text("Female")

continue_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Continue')]")))
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", continue_button)

time.sleep(300)

driver.quit()