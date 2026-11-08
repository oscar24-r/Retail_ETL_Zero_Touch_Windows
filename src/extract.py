import pandas as pd
from .config import DATASET
def extraer():
    if not DATASET.exists(): raise FileNotFoundError(DATASET)
    return pd.read_csv(DATASET)
