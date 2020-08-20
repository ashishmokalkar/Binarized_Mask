# Binarized Mask Generation using OpenCV

This code converts the target image into binarized mask. It distinguishes between foreground object and the background.

# Installations

### Install Python 3 
```
sudo apt-get install python3.6
```
### Install pip 
```
sudo apt-get install python3-pip
```
### Then install virtualenv using pip3
```
sudo pip3 install virtualenv 
```
### Now create a virtual environment
```
virtualenv venv 
```
### Active your virtual environment
```
source venv/bin/activate
```
# Setup dependencies
Install dependent python packages
```
pip install requirements.txt
```
# Run Code
### Python
```
python binarization.py -input <path to input file>
```
For example, on my system:
```
python binarization.py -input /home/ashish/Pictures/125356504.jpg
```
Type `-h` for `help`
```
python binarization.py -h
```

# Architecture
![](images/flowchart2.jpg)

# Procedure
Original Image:
<img src="images/denoised.png" width=400>


# Architecture
![](images/flowchart2.jpg)

# Procedure
### Read original image
Original Image:
![](images/orig.png)

### Denoised image
Non-local Means Denoising algorithm to remove noise in the image:
![](images/denoised.png)
