import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

def get_data(page_index):
    url = f"https://bama.ir/cad/api/Price/hierarchy?pageIndex={page_index}"
    driver = webdriver.Chrome()
    driver.get(url)
    data_element = driver.find_element(By.TAG_NAME, 'pre')
    data_text = data_element.get_attribute('innerHTML')
    driver.quit()
    return data_text

def scrape_car_price_list():
    result = []
    for i in range(1, 16):  # تغییر صفحه اینجا انجام می‌شود
        data = get_data(i)
        if data:
            # تبدیل متن به شیء JSON
            data_json = json.loads(data)
            # اضافه کردن داده به لیست نتیجه
            result.append(data_json)

    items_list = []
    for data in result:
        for brand in data["data"]:
            for item in brand["items"]:
                item["brand"] = brand["brand"]
                item["brand_fa"] = brand["brand_fa"]
                items_list.append(item)

    df = pd.DataFrame(items_list)
    df.to_csv('car_PriceList.csv', index=False, encoding='utf-8-sig')

    return df
