from Bama import scrape_car_reviews
from CarPriceList import scrape_car_price_list

# Path to your downloaded ChromeDriver
driver_path = '/path/to/chromedriver'
# Path to cars.json
cars_json_path = 'cars.json'

df, pivot_table = scrape_car_reviews(driver_path, cars_json_path)

# چاپ اطلاعات DataFrame
print(df)

# چاپ جدول Pivot
print(pivot_table)


df = scrape_car_price_list()

# چاپ نتیجه
print(df)