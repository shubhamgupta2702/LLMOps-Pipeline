from setuptools import find_packages, setup

setup(
    name="LLMOps Pipeline",
    version="0.0.1",
    author="Shubham Gupta",
    author_email="shubhamgupta43567@gmail.com",
    packages=find_packages(),
    install_requires=[
        "langchain",
        "fastapi",
        "uvicorn",
        "python-dotenv"
    ]
)