import logging
import os
import sys
#defining the string while returning the logging
logging_str="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"

#defining the directory name
logging_dir="logs"


#creating the directory for logging
log_filepath = os.path.join(logging_dir, "running_logs.log")
os.makedirs(logging_dir, exist_ok=True)

#defining the logging object
logging.basicConfig(level=logging.INFO,format=logging_str,
handlers=[logging.FileHandler(log_filepath),
logging.StreamHandler(sys.stdout)])

#defining the logger
logger=logging.getLogger("gender_reaction_classifier_log")


