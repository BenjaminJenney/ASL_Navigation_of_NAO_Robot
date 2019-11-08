# ASL_Navigation_of_NAO_Robot

Research project focused on remotely Navigating a NAO Robot using the Kinect V2 

## Getting Started

Simply Download and open the solution in VIsual Studio 2015. You will also need to be able to run the python script which controls the robot and acts as a server socket that listens for commands from Discreet_Gestures_Basics_WPF. You must first run the server (main.py) before you can start streaming data from the Kinect.

Currently the gesture database consists of Sit, Stand, Walk, Turn Left, Turn right.

### Prerequisites

* Visual Studio 2015
* Kinect for Windows SDK 2.0
* .NET Framework 4.5 (may work with later versions)
* Python 2.7
* Naoqi for Python (login required)
* Nao Robot, or Choregraph


```
https://visualstudio.microsoft.com/vs/older-downloads/
https://www.microsoft.com/en-us/download/details.aspx?id=44561
https://www.python.org/download/releases/2.7/
https://community.ald.softbankrobotics.com/en/resources/software/language/en-gb

```

### Installing
Make sure appropriate references are included:
right click project->references->Extensions: 
  check: Microsoft.Kinect
         Microsoft.Kinect.VisualGestureBuilder
         
 If you do not see these references download Kinect sdk 2.0 package using Visual Studios Nuget pkg manager: PM> Install-Package KinectSDK2 -Version 2.0.1410.19000

## Built With

* C# & .NET Framework 4.5
* VS 2015
* Python 2.7
* NaoQi for Python


## Authors

* **Benjamin Jenney** Student at BMCC

## Acknowledgments

* Thank You to BMCC for providing the resources for such a fun opportunity
* Thank You Professor Azhar for being a great mentor
