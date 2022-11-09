import setuptools
from typing import List
#reading the read me file
with open("README.md", "r") as fh:
    long_description = fh.read()
#reading all requirements file
def get_requirements_data()->List[str]:
    with open("requirements.txt","r") as f:
        return f.readlines().remove("-e .")

__version__="0.0.4"

#defining the setuptools parameters
REPO_NAME="Gender_and_reaction-Classifier"
AUTHOR_NAME="10tanmay100"
SRC_REPO="gender_reaction_classifier"
AUTHOR_EMAIL="chakrabortytanmay744@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="Gender and reaction Classifier",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": "https://github.com/10tanmay100/Gender_and_reaction-Classifier"
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=get_requirements_data()
)





