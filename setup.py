from setuptools import find_packages, setup

setup(
    name='src',
    install_requires=[
        "pandas", 
        "ipykernel", 
        "numpy",
        "sodapy",
        "python-dotenv>=0.5.1"
    ],
    version='0.1.0',
    description='classification of public procurement through UNSPSC codes',
    author="""
    Laura Navarro

    Julian Vargas

    Daniel Perdomo

    Julian Chacon

    Victor Rivera

    Jose Dager

    Jose Cardenas
    """,
    license='',
)
