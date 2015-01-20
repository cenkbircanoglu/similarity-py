from distutils.core import setup

from setuptools import find_packages


setup(
    name='similarityPy',
    version='0.1.2',
    packages=find_packages(exclude=['tests', 'settings', 'requirements']),
    description='Similarity Algorithm (Data Mining) implementation in Python',
    long_description=open('README.md').read(),
    install_requires=[
        "enum >= 0.4.4",
    ],
    author='Cenk Bircanoglu',
    author_email='cenk.bircanoglu@gmail.com',
    url='https://github.com/cenkbircanoglu/similarityPy',  # use the URL to the github repo
    download_url='https://github.com/cenkbircanoglu/similarityPy/tarball/v0.1.2',  # I'll explain this in a second
    keywords=['data mining', 'distance', 'similarity', 'measure', 'python', 'statistic'],  # arbitrary keywords
    classifiers=[],
    include_package_data=True,
    zip_safe=False,
    license='MIT',
    platforms=['any'],
)