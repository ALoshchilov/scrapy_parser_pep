import csv
from collections import defaultdict
from datetime import datetime as dt

from pep_parse.settings import BASE_DIR, RESULTS_REL_PATH


class PepParsePipeline:

    def open_spider(self, spider):
        self.statuses = defaultdict(int)

    def process_item(self, item, spider):
        self.statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        with open(
            BASE_DIR / RESULTS_REL_PATH / (
                'status_summary_'
                f'{dt.utcnow().strftime("%Y-%m-%d_%H-%M-%S")}.csv'
            ),
            'w',
            encoding='utf-8'
        ) as f:
            csv.writer(
                f, dialect=csv.unix_dialect, quoting=csv.QUOTE_MINIMAL
            ).writerows((
                ('Статус', 'Количество'),
                *self.statuses.items(),
                ('Total', sum(self.statuses.values()))
            ))
