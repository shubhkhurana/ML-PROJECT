import logging
import os ##for creating and modifying files
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" ##log is extension
log_path = os.path.join(os.getcwd(),"Logs",LOG_FILE) #defining path 
os.makedirs(log_path,exist_ok=True) ##will create a logs folder where all THe LOG_FILE will be stored

LOG_FILE_PATH = os.path.join(log_path,LOG_FILE) 

##setting format of file
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s %(levelname)s - %(message)s",
    level= logging.INFO, ## can be set to warning
)