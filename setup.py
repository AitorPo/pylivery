from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'A package to integrate your business with delivery companies'
LONG_DESCRIPTION = 'A package that makes it easy integrate your deliveries with companies like Glovo, Uber or Catcher'

setup(
    name="pylivery",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author="Aitor Poquet",
    author_email="aitorpoquetgin@gmail.com",
    license='MIT',
    packages=find_packages(),
    install_requires=[],
    keywords='delivery',
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
    ]
)
