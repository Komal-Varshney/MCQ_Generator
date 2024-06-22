# for installing local package in virtual environment
from setuptools import find_packages,setup

setup(
    name = 'mcq_generator',
    version='0.0.1',
    author='Komal Varshney',
    author_email='varshneyk578@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)
#find_package is responsible for inding out the local packages whereever it will be able to find out init file it will consider that folder as local package