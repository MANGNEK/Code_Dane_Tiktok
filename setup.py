from setuptools import setup, find_packages

with open("requirements.txt") as requirement_file:
    requirements = requirement_file.read().split()

setup(
    name="TikTokLive-Connect",
    description="TikTokLive-Connect",
    version="1.0.0",
    author="Curly",
    author_email="curly.1747@gmail.com",
    install_requires=requirements,
    packages=find_packages(),
)
