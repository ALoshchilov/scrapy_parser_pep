import csv
from collections import defaultdict
from datetime import datetime as dt

from scrapy.exceptions import DropItem

from pep_parse.messages import KEY_NOT_FOUND
from pep_parse.settings import BASE_DIR, RESULTS_REL_PATH


class PepParsePipeline:

    def open_spider(self, spider):
        self.statuses = defaultdict(int)

    def process_item(self, item, spider):
        if 'status' not in item:
            raise DropItem(KEY_NOT_FOUND.format(key='status'))
        self.statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        results_dir = BASE_DIR / RESULTS_REL_PATH
        results_dir.mkdir(exist_ok=True)
        with open(
            results_dir / (
                'status_summary_'
                f'{dt.utcnow().strftime("%Y-%m-%d_%H-%M-%S")}.csv'
            ),
            'w',
            encoding='utf-8'
        ) as f:
            csv.writer(
                f, dialect=csv.unix_dialect
            ).writerows((
                ('Статус', 'Количество'),
                *self.statuses.items(),
                ('Total', sum(self.statuses.values()))
            ))
