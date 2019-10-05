# Android Resources Tools

## Image resources resize tool

It is a simple python script that get as an input the name of the image and the density the the image is currently designed for and outputs resided images for all the lower densities in separate folders.

## Prerequisites

* python 3 installed on your machine

## How to use it

> \user>python [image path] [input density]  

```DOS batch
C:\Users\myuser> python input_image.png 3
```

## Densities maping  

* mdpi -> 1
* hdpi -> 1.5
* xhdpi -> 2
* xxhdpi -> 3
* xxxhdpi -> 4
