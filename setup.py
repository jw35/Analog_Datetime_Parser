import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="analog_datetime_parser",
    version="1.0.0",
    author="Jon Warbrick",
    author_email="jw35@cam.ac.uk",
    description="A parser for the datetime formats used by 'Analog'",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jw35/analog-datetime-parser",
    packages=["analog_datetime_parser.py"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
