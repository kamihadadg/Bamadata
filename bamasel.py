from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json
import time  # برای استفاده از تابع sleep()

# Path to your downloaded ChromeDriver
driver_path = ''
# ساخت یک نمونه از تنظیمات Chrome
chrome_options = Options()
chrome_options.add_argument("--webdriver.chrome.driver=" + driver_path)

# ساخت یک نمونه از درایور Chrome با استفاده از تنظیمات سفارشی
chrome_driver = webdriver.Chrome(options=chrome_options)
chrome_driver.maximize_window()

# URL of the webpage
url = "https://bama.ir/car-reviews"

# لیست اطلاعات خودروها در قالب JSON
cars_list = [
    {"car_name": "bac/x3pro-specs-1456-1.5liter"},
    {"car_name": "peugeot/207sd-specs-1168-at"},
    {"car_name": "peugeot/207-specs-1167-381-at"},
    {"car_name": "jac/s5-specs-1036-464-at1500"},
    {"car_name": "jac/j4-specs-1231"},
    tara/manual-specs-1371
    {"car_name": "alfaromeo/4c-specs-1177"}
    
    
    # اطلاعات خودروهای دیگر اینجا اضافه شود
]

def get_data(car_name, file):
    chrome_driver.get(url + '/' + car_name)
    time.sleep(3)  # وقفه 3 ثانیه
    progress_data = chrome_driver.find_elements(By.CLASS_NAME, 'car-reviews-base__progress-holder')
    for div in progress_data:
        elements = div.find_elements(By.CLASS_NAME, 'rounded-progress-wrapper') 
        for wrapper in elements:
            percent_div = wrapper.find_elements(By.CLASS_NAME, 'rounded-progress')
            for p in percent_div:
                percentage = p.find_element(By.CLASS_NAME, 'rounded-progress__text').text.strip()
                file.write(f'{wrapper.text}: {percentage}\n')

# نام فایل متنی برای ذخیره خروجی
output_file = 'output.txt'

# باز کردن فایل برای نوشتن
with open(output_file, 'w', encoding='utf-8') as file:
    # برای هر خودرو در لیست، داده‌های مربوطه را بیاورید
    for car_info in cars_list:
        car_name = car_info["car_name"]
        file.write(f"Fetching data for {car_name}\n")
        get_data(car_name, file)

# Close the WebDriver
chrome_driver.quit()
