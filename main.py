
import webbrowser
# اجرای توابع برای گرفتن داده‌ها
from Bama import scrape_car_reviews
from CarPriceList import scrape_car_price_list

# Path to your downloaded ChromeDriver
driver_path = '/path/to/chromedriver'
# Path to cars.json
cars_json_path = 'cars.json'

# گرفتن داده‌ها از توابع
df_reviews, pivot_table_reviews = scrape_car_reviews(driver_path, cars_json_path)
df_prices = scrape_car_price_list()

# تبدیل داده‌ها به فرمت HTML
html_reviews = df_reviews.to_html()
html_pivot_reviews = pivot_table_reviews.to_html()
html_prices = df_prices.to_html()

# ادغام کدهای HTML و Python
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>نتایج</title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
    <h1>Car Reviews</h1>
    {html_reviews}
    <h1>Car Reviews Pivot Table</h1>
    {html_pivot_reviews}
    <h1>Car Prices</h1>
    {html_prices}
</body>
</html>
"""

# ذخیره فایل HTML
with open('results.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Results saved to 'results.html'")


webbrowser.open('results.html')