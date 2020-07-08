# handy
A hand gesture controlled script/application to execute other applications/actions.

A collaborative college project has an user interface to select actions that can be performed or executed when a hand gesture is detected.

## Tech used
- PyQt5
- OpenCV

## Files
`handy.py` - The main file to start the GUI.
`handycam.py` - The file used to start the camera, and perform the functions.
`rscfile_rc.py` - Resource file compiled for PyQt5.
`icon.png` - Icon file.
`setup.py` - Script to generate executable file.

## Execution 
Just install the required python modules and run `handy.py` using `python3 handy.py`.

## Procedure
Clicking on the fingers will open a window asking to choose application.
Clicking on the eye once will allow user to show gestures, for which the application linked will execute. In order to re-run, click on the eye again.

## Create executable file
Install 	idna and cx_freeze using `pip3 install cx-Freeze idna`, and run `setup.py`.
Run this only when `handy.py` runs without any problem.

## References
1. lzane/Fingers-Detection-using-OpenCV-and-Python. https://github.com/lzane/Fingers-Detection-using-OpenCV-and-Python
2. amarlearning/Finger-Detection-and-Tracking. https://github.com/amarlearning/Finger-Detection-and-Tracking
