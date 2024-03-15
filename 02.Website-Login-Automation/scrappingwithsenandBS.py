from bs4 import BeautifulSoup
import requests

def get_currency(input_currency, output_currency):
    url = f'https://www.x-rates.com/calculator/?from={input_currency}&to={output_currency}&amount=1'
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    soup.find('span', class_="ccOutputRslt")
    currency = soup.find('span', class_="ccOutputRslt").get_text()
    print(currency)
get_currency('INR', 'USD')
