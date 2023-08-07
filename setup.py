from setuptools import setup, find_packages

setup(
    name='stock-insights',
    version='0.1.0',
    description='',
    author='Mathias Noerskov',
    author_email='mathiasnoerskov@gmail.com',
    url='https://github.com/mathiasDK/stock_insights',
    packages=find_packages(),
    install_requires=[
        "bs4",
        "pandas==2.0.3",
        "lxml",
        "plotly==5.15.0",
        "streamlit==1.25.0",
    ],
    classifiers=[
        'Programming Language :: Python :: 3.11',
    ],
)
