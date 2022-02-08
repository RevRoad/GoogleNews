import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="GoogleNews_WebDriver",
    version="1.0.0",
    author="Jacob Tye",
    author_email="jacob.tye@revroad.com",
    description="Google News search for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RevRoad/GoogleNews",
    packages=setuptools.find_packages(),
    install_requires=[
        "beautifulsoup4",
        "python-dateutil",
        "selenium",
        "webdriver-manager",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
