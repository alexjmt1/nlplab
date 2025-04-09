from setuptools import setup, find_packages

setup(
    name="nlplab",
    version="0.1.0",
    author="MATHAPAN",
    author_email="miniprojectmlmaiml@gmail.com",
    description="NLP Lab Experiments Package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/nlplab",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "nltk>=3.5",
        "scikit-learn>=0.24.0",
        "pandas>=1.0.0",
        "numpy>=1.0.0"
    ],
)