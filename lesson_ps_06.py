import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = "https://www.divan.ru/"

driver.get(url)

time.sleep(3)

lighting_sections = driver.find_elements(By.CLASS_NAME, 'NuViy S5rWI')
print(lighting_sections)

parsed_data = []

for lighting_section in lighting_sections:
      try:
       name = lighting_section.find_element(By.CLASS_NAME, 'div.lsooF ').text
       price = lighting_section.find_element(By.CLASS_NAME, 'div.pY3d2').text
       url = lighting_section.find_element(By.CSS_SELECTOR, 'a.bloko-link').get_attribute('href')

      except:
       print("произошла ошибка при парсинге")
      continue

   # Вносим найденную информацию в список
parsed_data.append([name, price, url])

   # Закрываем подключение браузер
driver.quit()

   # Прописываем открытие нового файла, задаём ему название и форматирование
   # 'w' означает режим доступа, мы разрешаем вносить данные в таблицу
with open("hh.csv", 'w', newline='', encoding='utf-8') as file:

 writer = csv.writer(file)
   # Создаём первый ряд
writer.writerow(['Название вакансии', 'название компании', 'зарплата', 'ссылка на вакансию'])

   # Прописываем использование списка как источника для рядов таблицы
writer.writerows(parsed_data)

