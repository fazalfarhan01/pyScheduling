import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyScheduling",  # Replace with your own username
    version="0.0.1",
    author="Mohamed Farhan Fazal",
    author_email="fazal.farhan@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fazalfarhan01/pyScheduling",
    project_urls={
        "Bug Tracker": "https://github.com/fazalfarhan01/pyScheduling/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    python_requires=">=3.6",
    install_requires=[
        "altgraph==0.17",
        "future==0.18.2",
        "pefile==2019.4.18",
        "pywin32-ctypes==0.2.0",
        "terminaltables==3.1.0",
    ],
)
