# Project Overview:
This repository contains all necessary code to take an uncleaned .csv document from Zooniverse's citizen science project Microplants and output a cleaned datasheet with necessary calculations that can be used for further analysis of classification data. 
Uncleaned data can be obtained via the Zooniverse API. 
project website: https://www.zooniverse.org/projects/fieldmuseumexhibits/microplants


### plant_and_segment_classes.py:
This file contains classes with methods to:
- determine if two line segments intersect
- return the intersection point of two lines
- calculate the angle between two lines

### cleaning_script.py:
This file takes an uncleaned .csv file as input returns a cleaned dataframe with the desired structure.

### visualizations.py:
This file uses a cleaned dataframe to produce desired visualizations of classification data. 

