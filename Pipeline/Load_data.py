if __name__ == "__main__" and __package__ is None:
    __package__ = "Pipeline"

import os
import logging
import zipfile
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import shutil
from utils.help import *
# Set up logging
log_file_path = os.path.join("log", "data_loading_log.txt")
logging.basicConfig(filename=log_file_path, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
ColoredOutput.log_message("Data Loading Started....",'BLUE',True)

# data_file = os.path.join('Data','Evaluation-dataset (1).csv')
df = pd.read_csv('Data\Evaluation-dataset.csv')


df = df.iloc[:, :4]
df.columns = ['Text', 'subtheme1', 'subtheme2','subtheme3']
print(df.head())
path=os.path.join('Data', 'Data_load.csv')
df.to_csv(path,index=False)
ColoredOutput.log_message(f"Data saved in {path}",'GREEN',True)
