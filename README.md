# Industrial robotics
This repository contains the development of the laboratory practice of the robotics class at the Universidad Nacional de Colombia. This practice consists of using the industrial manipulator ABB IRB 140 to traverse a path on a paper and draw the initials of the name of each [team](#contributors) member (BJC).

#### Materials
* RobotStudio version 5 or higher
* Datasheet ABB IRB 140
* ABB IRB 140 industrial manipulator
* ABB IRC5 controller


### Tool design
In order to write on the paper it is necessary to create a tool that is suitable for the flange of the manipulator and that can hold a marker pen. Consequently, it was necessary to review the manipulator datasheet to know the dimensions of the flange along with the location and type of screws to fix the tool.

<p align="center">
    <img src="https://user-images.githubusercontent.com/30636259/176016691-8cc97696-ada1-4f55-92be-1038c559b90f.png#gh-light-mode-only" width="450px" alt="flange" />
    <img src="https://user-images.githubusercontent.com/30636259/176016671-56aa0b16-6a1d-45ac-b7e1-eebf3c76cdc7.png#gh-dark-mode-only" width="450px" alt="flange" />
</p>


Based on these dimensions we started to design a tool. Initially it was thought to use additive manufacturing to print the structure where the marker goes, but there was a doubt if the piece would be strong enough and not break. Therefore, it was decided to use CPVC pipe for cost and ease of obtaining the components.

<p align="center">
    <img src="https://user-images.githubusercontent.com/30636259/175814613-9f200498-84fc-4494-b909-320eb8ae7de4.gif" alt="tool" width="400" /> <br/>
    <a href="https://cad.onshape.com/documents/f980fe7178465a5e85356d19/w/a751aae7c3f868ba172fc952/e/3687fe216ca7c6a9660936e8?renderMode=0&uiState=62b8723dcd67bc23dc436eb9">
        OnShape CAD Model 
    </a>
</p>


These components allowed us to use more complex geometries as shown in the image above, as the marker is tilted at $45\degree$. CPVC pipe was chosen, as the PVC pipe is a little wider and the markers did not fit properly.

#### Tool creation in RobotStudio
In order to add the tool to the RobotStudio library, the CAD model was exported to .SAT format, which is correctly read in this software as a single part. For this purpose, an empty station is created and with the help of the _import geometry_ option in the _modeling_ tab, the tool is added to the station.

<p align="center">
    <img src="https://user-images.githubusercontent.com/30636259/176235879-7a25f821-b656-4698-b11b-aef3c7ec615c.png" alt="import geometry window" width="450" />
</p>

Once the part is imported, it must be positioned so that the world coordinate frame coincides with that of the manipulator flange. In addition, a frame is added at the location where the TCP (Tool Center Point) is located. To orient the part, it is sufficient to make a rotation in the $z$ axis, while to place the TCP it was necessary to create the frame at the end of the pen housing and then move it to the tip of the pen.

<p align="center">
    <img src="https://user-images.githubusercontent.com/30636259/176238817-671f66dd-b3e8-45dc-a961-e8db909d11c4.png" width="350" />
    <img src="https://user-images.githubusercontent.com/30636259/176240744-c102b506-0439-462d-bce5-2071958232ba.png" width="300" />
</p>

With the TCP created, proceed to create the tool, for this, in the *modeling* tab, select the option to *create tool*. After selecting this option a popup window appears where the mass and moments of inertia of the part (provided by the CAD software) are added, then the TCP is added and click on *Done*.

<p align="center">
    <img src="https://user-images.githubusercontent.com/30636259/176242468-57e4d3de-41e1-40c0-a3eb-424947348880.png" width="300" />
    <img src="https://user-images.githubusercontent.com/30636259/176242519-dea6e20e-0193-42d0-8930-bf42d12cb1a9.png" width="300" />
</p>

In order to use the tool for other applications, it is saved in the personal [library](lib/MarkerPenTool.rslib).

<p align="center">
    <img src="https://user-images.githubusercontent.com/30636259/176242904-4153eb4b-8676-4146-a8b4-3b5e75c37494.png" width="450" /> <br/>
    <img src="https://user-images.githubusercontent.com/30636259/176243349-ffa354ad-5ca2-434e-9a73-4d71c6837768.png" width="300" />
</p>



#### Calibration


### Path planning



### Robotics toolbox

## Contributors
* [Brayan Estupiñan](https://github.com/Brayanleo)
* [Julián Felipe Luna](https://github.com/juflunaca)

## Acknowledgements
* Professor: [Felipe Gonzalez](https://github.com/felipeg17)
* Monitor: [Manuel Lugo](https://github.com/mlugom)


## References
