from setuptools import setup, find_packages

setup(
    name='clustering',
    version='0.1.0',
    author='',
    author_email='',
    packages=find_packages(),
    url='',
    description='Clustering (Data Mining) implementation in Python',
    long_description=open('README.md').read(),
    install_requires=[
        "enum >= 0.4.4",
    ],
    include_package_data=True,
    zip_safe=False,
    license='MIT',
    platforms=['any'],
)