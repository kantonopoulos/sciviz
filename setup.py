from setuptools import find_packages, setup

with open("app/README.md", "r") as f:
    long_description = f.read()

setup(
    name="sciviz",
    version="0.1.0",
    description="A package to simplify scientific visualization",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kantonopoulos/SciViz",
    author="Konstantinos Antonopoulos",
    author_email="k.antono@outlook.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering",
    ],
    intall_requires=["matplotlib>=3.9.0", "numpy>=1.26.0", "pandas>=2.2.0", "seaborn>=0.13.0", "matplotlib-venn>=0.11.10"],
    extras_require={
        "dev": ["unittest"]
    },
    python_requires=">=3.10",
)