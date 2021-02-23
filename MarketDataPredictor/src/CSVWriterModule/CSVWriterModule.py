import csv
import os


class CsvWriter:
    def __init__(self, data_dir, file_name):
        self.file = open(
            os.path.join(data_dir, file_name),
            'w',
           encoding='utf8'
        )

        self.csv_writer = csv.writer(
            self.file,
            delimiter=',',
            quotechar='|', quoting=csv.QUOTE_MINIMAL
        )

    def add_row(self, data):
        self.csv_writer.writerow(data)

    def add_rows(self, data):
        self.csv_writer.writerows(data)