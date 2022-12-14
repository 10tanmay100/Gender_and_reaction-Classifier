import logging
import os
from pathlib import Path

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s')
package_name="gender_reaction_classifier"

#mentioned the list of files and folders I want to create for this project
list_of_files=[".github/workflows/.gitkeep",
               "configs/",
               "artifacts/data_ingestion/",
               "test/unit/",
               "test/integration/",
               "params.yaml",
               "setup.py",
               "setup.cfg",
               "pyproject.toml",
               "requirements.txt" ,
               "requirements_dev.txt",
               "tox.ini",
               "init_setup.sh",
               f"src/{package_name}/__init__.py",
               f"src/{package_name}/components/__init__.py",
               f"src/{package_name}/config/__init__.py",
               f"src/{package_name}/entity/__init__.py",
               f"src/{package_name}/pipeline/__init__.py",
               f"src/{package_name}/utils/__init__.py",
               f"src/{package_name}/utils/common.py",
               f"src/{package_name}/constants/"]

#the code to create above mentioned files and folders

from pathlib import Path
import os
for files in list_of_files:
    try:
        path,filename=os.path.split(files)
        if path!="":
            if not os.path.exists(Path(path)):
                os.makedirs(Path(path),exist_ok=True)
                if filename!="":
                    with open(Path(path+"/"+filename),"w") as f:
                        pass
                    logging.info(f"{path}/{filename} has been created successfully!!")

            else:
                logging.info(f"{path}/{filename} already exists!!")
        else:
            if not os.path.exists(filename):
                with open(filename,"w") as f:
                    pass
                logging.info(f"{filename} has been created successfully!!")
            else:
                logging.info(f"{filename} already exists!!")
    except Exception as e:
        logging.info(f"error has happened while creating the fiile and folders  !!!,{e}")