# ASL-alphabet
CNN to recognize ASL alphabets.
## Dataset
The training data set was taken from [kaggle](https://www.kaggle.com/grassknoted/asl-alphabet). It contains 87,000 images which are 200x200 pixels. There are 29 classes, of which 26 are for the letters A-Z and 3 classes for SPACE, DELETE and NOTHING. These 3 classes are very helpful in real time applications, and classification. I used a resnet34 architecture to achieve an accuracy of 99.98% on the validation set.

![ASL-alphabet](https://raw.githubusercontent.com/utkarshchawla/ASL-alphabet/master/resources/asl-alphabet.jpg "Logo Title Text 1")

## Demo

<img src="https://github.com/utkarshchawla/ASL-alphabet/blob/master/resources/A-E.gif?raw=true" width="285" height="320"> <img src="https://github.com/utkarshchawla/ASL-alphabet/blob/master/resources/F-J.gif?raw=true" width="285" height="320"> <img src="https://github.com/utkarshchawla/ASL-alphabet/blob/master/resources/K-O.gif?raw=true" width="285" height="320"> <img src="https://github.com/utkarshchawla/ASL-alphabet/blob/master/resources/P-T.gif?raw=true" width="285" height="320"> <img src="https://github.com/utkarshchawla/ASL-alphabet/blob/master/resources/U-Z.gif?raw=true" width="285" height="320">
