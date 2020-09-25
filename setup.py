#setup / configuracion
#__author__ = "sn.lionel90"
#print(__author__)

import setuptools

with open ("README.md", "r") as fh:
    long_description = fh.read()
    setuptools.setup(
    name = 'insta-craken.',
    version = '1.0.0',
    author = 'sn.Lionel90 aka Lionel Sanchez',
    description = ("download pic profile from any account"),
    long_description=long_description,
    long_description_content_type="text/markdown", 
    url = ' https://github.com/snLionel90/insta-craken',
    keywords=['instagram', 'snLionel90', 'picture_downloader', 'lel'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Insta-craken :: snLionel90 ",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data=True, 
)
