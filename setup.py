from pathlib import Path
from setuptools import setup, find_packages


with open('requirements.txt') as f:
    requirements = f.read().splitlines()

parent = Path(__file__).resolve().parent
setup(
    name="runx",
    version="0.0.4",
    author="Andrew Tao",
    author_email="atao@nvidia.com",
    description="runx - experiment manager for machine learning research",
    url="https://github.com/NVIDIA/runx",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements,
    python_requires='>=3.6',
)
