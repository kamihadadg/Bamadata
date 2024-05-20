import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json
import time

# Path to your downloaded ChromeDriver
driver_path = '/path/to/chromedriver'

# ساخت یک نمونه از تنظیمات Chrome
chrome_options = Options()
chrome_options.add_argument("--webdriver.chrome.driver=" + driver_path)

# ساخت یک نمونه از درایور Chrome با استفاده از تنظیمات سفارشی
chrome_driver = webdriver.Chrome(options=chrome_options)
chrome_driver.maximize_window()

# URL of the webpage
url = "https://bama.ir/car-reviews"

# لیست اطلاعات خودروها در قالب JSON
with open('cars.json', 'r') as file:
    cars_list = json.load(file)

data = []  # لیست برای ذخیره داده‌های جمع‌آوری شده

def get_data(car_name):
    chrome_driver.get(url + '/' + car_name)
    time.sleep(2)  # وقفه 2 ثانیه
    progress_data = chrome_driver.find_elements(By.CLASS_NAME, 'car-reviews-base__progress-holder')
    for div in progress_data:
        elements = div.find_elements(By.CLASS_NAME, 'rounded-progress-wrapper')
        for wrapper in elements:
            percent_div = wrapper.find_elements(By.CLASS_NAME, 'rounded-progress')
            for p in percent_div:
                label = wrapper.text.split('\n')[1]
                percentage = p.find_element(By.CLASS_NAME, 'rounded-progress__text').text.strip()
                # تبدیل رشته درصد به عدد
                percentage_value = float(percentage.rstrip('%'))
                data.append({"Car": car_name, "Label": label, "Percentage": percentage_value})

# برای هر خودرو در لیست، داده‌های مربوطه را بیاورید
for car_info in cars_list:
    car_name = car_info["car_name"]
    get_data(car_name)

# Close the WebDriver
chrome_driver.quit()

# تبدیل لیست داده‌ها به DataFrame
df = pd.DataFrame(data)

# افزودن ستون SumPercentage
df['SumPercentage'] = df.groupby('Car')['Percentage'].transform('sum')

# چاپ اطلاعات DataFrame
print(df)

# ذخیره DataFrame به عنوان یک فایل CSV
df.to_csv('car_reviews.csv', index=False, encoding='utf-8-sig')

# ساخت جدول Pivot بر اساس نام ماشین و برچسب‌ها
pivot_table = df.pivot_table(index='Car', columns='Label', values='Percentage', aggfunc='first')


# چاپ جدول Pivot
print(pivot_table)
