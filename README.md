# Distance-Finder-Script

IR sensor was being to find distance as described in the following project : http://devpost.com/software/distance-sensor

This script was created as Microsoft Excel was giving accurate results when
trying to curve fit a polynomial function of order four and above.

The values of IR sensor were providing one number and had some jitter values.
To remove these jitter values, we took mode as the jitter values were very off
from the actual value.

However, if there is an error, the script takes mean of the readings.

The final values were then graphed.
