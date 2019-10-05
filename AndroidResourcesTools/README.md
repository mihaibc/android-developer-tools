# Android Resources Tools

## Image resources resize tool

It is a simple python script that helps Android developers to resize image resources for all screen densities.

## Prerequisites

* [Python 3](https://www.python.org/downloads/) installed on your machine
* [Pillow](https://github.com/python-pillow/Pillow) library installed 

    -  You can install the libray with the follwoing command: 
        ```DOS batch
        pip install pillow
        ```
   
## How to use it

Open a terminal (*command prompt/powershell/shell terminal*) and go to the folder in which you have downloaded/cloned the python script and run it as described bellow. 

Syntax:
> \user> python image_resources_resize_tool.py [image path] [input density] [destination folder path]
    
- [destination path]  is an optional parameter - if it is not given the output folder will be the root folder of the image_resources_resize_tool.py file 

Usage example:
```DOS batch
C:\Users\myuser> python image_resources_resize_tool.py input_image.png 3 C:\Users\mysuer\Desktop\outputFolder
```
You cand give the resource folder of your Android project as an output folder and the images will be placed into drawables folder for each screen density.
## Densities maping  

* mdpi -> 1
* hdpi -> 1.5
* xhdpi -> 2
* xxhdpi -> 3
* xxxhdpi -> 4
