# LS-SVM-Abnormality-Detector
This script is a sample script of a larger, more optimized, and automatic script I designed for a limit switch outlier machine developed for a company. The full script is confidential however rights were given for me to publish this sample.
This sample uses SVM from the Scikit-Learn library

The machine essentially allowed input of a tape roll of manufactured limit switches and tested multiple dimensions (four shown here) including that of a general x, y, z, and operating position dimension of tens of thousands of switches.

Ex: 

![data](https://github.com/Mich8952/LS-SVM-Abnormality-Detector/blob/c672aead13473b6c5d14d42aecb12ab96b20940f/SVM%20Abnormality%20Detector/ls%20image.jpeg)

Some graphs of interest are num_outliers vs gamma values which was used to help the model reduce the number of outliers such that devices that were not outliers were not labelled as outliers.

![data](https://github.com/Mich8952/LS-SVM-Abnormality-Detector/blob/c672aead13473b6c5d14d42aecb12ab96b20940f/SVM%20Abnormality%20Detector/outliers%20vs%20gamma.png)

This can be graphically shown in a 4D plot as such:

![data](https://github.com/Mich8952/LS-SVM-Abnormality-Detector/blob/c672aead13473b6c5d14d42aecb12ab96b20940f/SVM%20Abnormality%20Detector/outlier%20plot.png)

Where X resemble outliers.

Note that the power in the model is not the plot but the output that lists potential outliers and their dimensions. A user will then verify the dimensions and discard/keep them depending on how far off their dimensions are. Note again, the actual full solution has many more than 4 dimensions so a plot is not viable.

Ex: The model may produce the following output:

![data](https://github.com/Mich8952/LS-SVM-Abnormality-Detector/blob/c1e41629efdeae371d2bc2e5c924713c6ff2b6c8/SVM%20Abnormality%20Detector/output.PNG)

Depending on the application of the limit switches, all of these may be viable. However, if it needs to fit a specific spec/bound, then certain ones that violate that spec can be discarded while others can be kept.
