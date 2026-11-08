import logging
from logging.handlers import RotatingFileHandler
from .config import LOGS
def get_logger():
    LOGS.mkdir(parents=True,exist_ok=True)
    log=logging.getLogger("retail_etl"); log.setLevel(logging.INFO)
    if not log.handlers:
        h=RotatingFileHandler(LOGS/"pipeline.log",maxBytes=1000000,backupCount=5,encoding="utf-8")
        h.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")); log.addHandler(h)
        c=logging.StreamHandler(); c.setFormatter(logging.Formatter("%(levelname)s: %(message)s")); log.addHandler(c)
    return log
