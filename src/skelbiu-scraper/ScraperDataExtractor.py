from bs4 import BeautifulSoup
from ScraperRequest import ScraperRequest


class ScraperDataExtractor:
    def __init__(self, request: ScraperRequest):
        self.request = request

    def extract_data(self) -> object:
        soup = BeautifulSoup(self.request.content, 'html.parser')
        products = soup.find_all('li', class_='simpleAds')
        list_of_products = []

        for product in products:
            title = product.find('h3').text.strip()  # Title
            price = product.find('div', class_='adsPrice').findNext('span').text  # price
            condition = product.find('div', class_='adsTextMoreDetails').text.strip()  # condition
            review = product.find('div', class_='adsTextReview').text.strip()  # Review
            city = product.find('div', class_='adsCity').text.strip()  # City
            date = product.find('div', class_='adsDate').text.strip()  # Date
            href = 'https://skelbiu.lt/' + product.find('a', href=True)['href'] # Href

            scraper_data = {'title': title, 'price': price, 'condition': condition,
                            'review': review, 'city': city, 'date': date, 'href': href}

            list_of_products.append(scraper_data)

        return list_of_products
