import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fastapi_and_vue",
    version="0.0.1",
    author="cybergrind",
    author_email="cybergrind@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cybergrind/fastapi_and_vue",
    project_urls={"Bug Tracker": "https://github.com/pypa/sampleproject/issues"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "backend"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=[
        'aiofiles==0.7.0',
        'fastapi==0.65.2',
        'orjson==3.5.3',
        'uvicorn==0.14.0',
        'uvloop==0.15.2',
        'httptools==0.2.0',
    ],
    extras_require={
        'test': ['pytest-asyncio==0.15.1', 'pytest==6.2.4', 'httpx==0.18.2', 'factory-boy==3.2.0']
    },
)
