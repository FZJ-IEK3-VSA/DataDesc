source config.sh

# CREATE CONFIG FILES
printf 'from setuptools import setup, find_packages
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(dir_path, "README.md"), "r") as fh:
    long_description = fh.read()

setup(
    name="'"${TITLE}"'",
    version="'"${VERSION}"'",
    license="'"${LICENSE_NAME}"'",
    author="'"${CONTACT_NAME}"'",
    author_email="'"${CONTACT_EMAIL}"'",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages("src"),
    package_dir={"": "src"},
    url="'"${REPOSITORY}"'",
    keywords="'"${KEYWORDS}"'",
)' > setup.py

printf "[metadata]
description-file=README.md" > setup.cfg

# CREATE SOURCE DISTRIBUTION
python3 setup.py sdist bdist_wheel
pip install twine 

# UPLOAD TO PYPI
twine upload -u ${PYPI_USER} -p ${PYPI_PASS} dist/*