# System reqirements:

## Software dependencies and OS

Python 3 with scipy and numpy on Linux, Windows or Mac

## Tested with:

Python 3.11
numpy 1.26.0
scipy 1.11.4
Linux Ubuntu 22.0.4
	
Python 3.11
numpy 1.24.3
scipy 1.10.1
Windows 10 Enterprise

## Non-standard hardware:
None

# Installation guide:

## Instructions

Copy the python script and the json file to the same folder.
Should take less than a minute.

# Demo

Run the python script from the folder where the json file is located.

From a terminal:

``` text
cd folder_with_the_json_and_python_files

python cloacipaperstats.py
```

Alternatively, use an IDE like Spyder. Remember to change directory to the folder where
the python and the json file are located.

## Expected runtime:
A few seconds

## Expected output
(The bootstrapping outputs may vary)

```
1) Reported results, percent reduction:

 a) 90 days experiment, 95% confidence interval by Fieller:

2021-07-14 -- 2021-07-18 :
[92.93956395 94.39113405] 

2021-07-18 -- 2021-07-26 :
[43.20039815 60.89310932] 

2021-07-26-08-00-00 -- 2021-08-02 :
[32.63394164 65.63127108] 

2021-08-01-21-00-00 -- 2021-08-05-16-00-00 :
[19.73157156 44.49047405] 

2021-08-16-09-00-00 -- 2021-08-21 :
[35.06151169 85.57024438] 

2021-10-10 -- 2021-10-16 :
[30.54810186 57.40904325] 

2022-08-01 -- 2022-08-17 :
[ 365.16890526 -125.22287818] 

 b) Four soils experiment, 95% confidence intervals by Fieller:


    calcite [84.19712448 93.1303762 ]
    organic [28.42580865 65.59067044]
    sand [89.65325311 99.26827178]
    unlimed [36.91957086 65.7513522 ]

 c) Field plot experiment, 95% confidence intervals by ttest on ratios:

  [53.82265416 73.56729023]

  [-8.02516283 31.54753303]



2) Simple bootstrap:

 a) 90 days experiment, 95% simple bootstrap confidence interval:
  [93.02341637 94.27449371]
  [44.28041608 59.64516652]
  [35.4976074  63.26092664]
  [21.68881878 42.72271809]
  [42.6770266  82.61390307]
  [32.69593466 55.69753191]
  [-45.16663395 278.76010719]

 b) Four soils experiment, 95% simple bootstrap confidence intervals:
    calcite [85.30411695 92.19389207]
    organic [37.94224482 64.0560954 ]
    sand [90.7630495  98.20986769]
    unlimed [41.30196475 63.56113677]

 c) Field plot experiment, 95% simple bootstrap confidence interval (no blocks):
  [49.89864299 75.00806569]
  [-30.80213005  39.95827787]

``` 
