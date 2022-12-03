from pathlib import Path

BOT_NAME = 'pep_parse'

PEP_SPIDERS = 'pep_parse.spiders'
PEP_FQDN = 'peps.python.org'

SPIDER_MODULES = [PEP_SPIDERS]
NEWSPIDER_MODULE = PEP_SPIDERS

ROBOTSTXT_OBEY = True

BASE_DIR = Path(__file__).parent.parent
RESULTS_REL_PATH = 'results'
(BASE_DIR / RESULTS_REL_PATH).mkdir(exist_ok=True)

FEEDS = {
    f'{RESULTS_REL_PATH}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    }
}
ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300
}
