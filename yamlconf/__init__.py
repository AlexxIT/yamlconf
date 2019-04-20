import logging
import logging.config

import yaml

__version__ = '0.1.3'


def load(filename='config.yml') -> dict:
    try:
        config: dict = yaml.safe_load(open(filename, encoding='utf-8'))

        logconf: dict = config.pop('logging', None)
        if logconf:
            if logconf.get('level'):
                logging.basicConfig(**logconf)
            else:
                logconf.setdefault('version', 1)
                logconf.setdefault('disable_existing_loggers', False)
                logging.config.dictConfig(logconf)

        return config

    except:
        logging.getLogger(__name__).exception(f"Error load yaml config")

        return {}
