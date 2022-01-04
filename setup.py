from setuptools import setup, find_packages


setup(
    name="envsheet",
    version="0.1.0",
    description="Env Sheet For RL",
    author="lipo",
    author_email="lipo8081@gmail.com",
    packages=find_packages("."),
    install_requires=[
        "pynput"
    ]
)