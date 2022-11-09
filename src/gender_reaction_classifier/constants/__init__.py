from pathlib import Path
import datetime

#define config yaml file Path
CONFIG_FILE_PATH=Path('configs\config.yaml')
#define the current time
CURRENT_TIME=str(datetime.datetime.now()).replace(" ","-").replace(":","-").replace(".","-")