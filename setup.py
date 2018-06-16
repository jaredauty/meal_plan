import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="meal_plan",
    version="0.0.1",
    author="Jared Auty",
    author_email="jared.auty@gmail.com",
    description="A package for calculating meal plans",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jaredauty/meal_plan",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires=['voluptuous'],
    setup_requires='pytest-runner',
    tests_require=['pytest'],
)