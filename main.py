import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# Функция для парсинга цен
def parse_divans(url):
    prices = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Цены в данный моментнаходятся в элементах с классом 'ui-LD-ZU'
    for item in soup.find_all(class_='ui-LD-ZU'):
        price_text = item.get_text(strip=True)
        # Убираем лишние символы и преобразуем в число
        price = int(''.join(filter(str.isdigit, price_text)))
        prices.append(price)

    return prices

# URL страницы с диванами
url = 'https://divan.ru/'  # Укажите правильный URL
prices = parse_divans(url)

# Сохранение цен в CSV файл
prices_df = pd.DataFrame(prices, columns=['Price'])
prices_df.to_csv('divan_prices.csv', index=False)

# Вычисление средней цены
average_price = prices_df['Price'].mean()
print(f'Средняя цена на диваны: {average_price:.2f} руб.')

# Построение гистограммы
plt.hist(prices, bins=20, color='blue', alpha=0.7)
plt.title('Гистограмма цен на диваны')
plt.xlabel('Цена (руб.)')
plt.ylabel('Количество')
plt.grid(axis='y', alpha=0.75)
plt.show()