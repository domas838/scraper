import csv


class ScraperDataSaver:
    def __init__(self, extracted_data):
        self.extracted_data = extracted_data

    def save_to_csv(self) -> None:
        print(self.extracted_data)
        with open('../../ipads.csv', mode='a') as csv_file:
            fieldnames = ['title', 'price', 'condition', 'review', 'city', 'date', 'href']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.extracted_data)
