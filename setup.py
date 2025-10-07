import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "End-to-end-ML-Project-with-MLflow"
AUTHOR_USER_NAME = "SAMEERMISHRA"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "sameermishra280202@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author="SAMEER MISHRA",
    author_email="sameermishra280202@gmail.com",
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content="text/markdown",
    url="https://github.com/Sameermishra123/END-TO-END-MLPROJECT",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)