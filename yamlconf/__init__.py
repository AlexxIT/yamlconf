import logging
import logging.config

import yaml


def load(filename='config.yml') -> dict:
    try:
        config: dict = yaml.load(open(filename, encoding='utf-8'))

        logconf: dict = config.pop('logging')
        if logconf:
            logconf.setdefault('version', 1)
            logconf.setdefault('disable_existing_loggers', False)
            logging.config.dictConfig(logconf)

        return config

    except Exception as e:
        logging.getLogger(__name__).warning(f"Error reading config: {e}")

        return {}
