import setuptools

version = "0.1.0"

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pypino",
    version=version,
    download_url = 'https://github.com/Brayyy/pypino/tarball/' + version,
    author = 'Bray Almini',
    author_email = 'bray@coreforge.com',
    description = 'A Python JSON logger with output matching Pino.js',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    url = 'https://github.com/Brayyy/pypino',
    packages=setuptools.find_packages(),
    keywords = ['log', 'logging', 'json', 'pino'],
    classifiers=(
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
