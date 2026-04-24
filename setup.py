from setuptools import setup, find_packages

setup(
    name="ORM_IXC",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
       'requests>=2.0.0'
    ],
    author="Caio Lima, Bruno Carvalho",
    description="Uma ORM para simplificar ações na API IXCSoft",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)