from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="recipe_manager_montwh1te",
    version="0.0.1",
    author="montwh1te",
    author_email="eduardomatuella@gmail.com",
    description="a package that can improve your recipe and baking management",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/montwh1te/recipe-package-template.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>= 3.8'
)