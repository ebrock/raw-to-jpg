raw-to-jpg is a Python script which converts CR2 images to JPG. 

## SETUP
A `requirements.txt` file is included, however, additional setup is required because the PIP version of `rawkit` requires libraw 0.19.0 to work. As a workaround, clone the latest version of `rawkit` from github (https://github.com/photoshell/rawkit) and copy/paste the `libraw` directory into the virtual env. 

## USAGE:
`python raw-to-jpg.py <file>`

