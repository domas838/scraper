import itertools
from ScraperRequest import ScraperRequest
from ScraperDataExtractor import ScraperDataExtractor
from ScraperDataSaver import ScraperDataSaver


class Scraper:
    def __init__(self, url):
        self.url = url

    def scrap(self) -> object:
        global scraper_data
        for i in itertools.count(start=1):
            init_scraper = ScraperRequest(self.url + str(i))
            scraper_request = init_scraper.request()
            scraper_data = ScraperDataExtractor(scraper_request).extract_data()

            # Stop script if request history array is not empty
            if scraper_request.history:
                break

            ScraperDataSaver(scraper_data).save_to_csv()

        return scraper_data
