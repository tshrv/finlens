from setuptools import find_packages, setup


def parse_requirements(filename: str) -> list[str]:
    """Load requirements form a pip requirements file"""
    with open(filename, "r") as f:
        return [
            line.strip()
            for line in f
            if line.strip() and not line.strip().startswith("#")
        ]


setup(
    name="finlens_core",  # Replace with your package name
    version="0.1.0",  # Initial version
    description="Core library for finlens backend services",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Tushar Srivastava",
    author_email="tusharsrivastava162@gmail.com",
    url="https://github.com/tshrv/finlens",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires="==3.9.20",
    install_requires=parse_requirements("requirements.txt"),
)
