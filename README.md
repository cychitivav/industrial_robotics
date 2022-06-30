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
For tool calibration we used a method with 4 points to define TCP and 1 elongator point to define $z$ axis. The first is to position robot at home, later we assembly own tool in the robot flange and last we put the reference tip on the floor inside of workspace robot, The idea is that the tip remains still, so we glue it to the floor.

<div align="center">
    <img src="https://user-images.githubusercontent.com/30636259/176493668-00edbee5-f5d0-44e6-aa2b-c0c6fb13b46d.png" width="250" /> <br/>
    Reference Tip
</div>

Now we can use the flexpendant to control robot joints manually and in this way make the TCP reach the reference tip as we can see it in the following image:

<div align="center">
    <img src="https://user-images.githubusercontent.com/30636259/176547056-50fe7d83-07be-4afa-9407-bdaa1263cfd4.jpg" width="350" />
</div>

Once the reference tip is reached, the information of the current position of the TCP must be saved, then we look for another orientation for  TCP  and we repeat the previous procedure until we have saved the four required points. Finally, to define the elongator point we must leave the tool in a vertical position to bring it closer to reference tip,as shown in the following image:

<div align="center">
    <img src="https://user-images.githubusercontent.com/30636259/176547094-c9d71ed0-92ee-44d3-af6e-3f3721760d2c.jpg" width="350" />
</div>

When the 4 points and $z$ are defined, tool data is created, also in this moment we can observe the error between the measurements. Finally, with this position the controller compute the tool transformation matriz.



<div align="center">
    <img src="https://user-images.githubusercontent.com/30636259/176549014-ceb92387-03b3-4f06-80bc-4530023ff5bc.jpg" width="350" />
    <img src="https://user-images.githubusercontent.com/30636259/176549184-9096a6a3-650c-4fc3-97ad-7d138425335f.jpg" width="350" />
</div>

$$
\text{Mean error} = 0.353\ mm
$$

### Path planning

<div align="center">
    <img src="https://user-images.githubusercontent.com/30636259/176568637-34abc6d3-b387-4574-a0e7-6cd6a467ef83.png#gh-dark-mode-only" width="700" />
    <img src="https://user-images.githubusercontent.com/30636259/176568709-5a4846fb-183c-4c45-9e0e-750b4b6ce175.png#gh-light-mode-only" width="700" />
</div>

<div align="center">

|   Point  | $x(mm)$ | $y(mm)$ | $z(mm)$ |
|:--------:|:-------:|:-------:|:-------:|
|   $P_1$  |   $35$  |  $135$  |   $0$   |
|   $P_2$  |   $35$  |  $85$   |   $0$   |
|   $P_3$  |   $35$  |  $25$   |   $0$   |
|   $P_4$  |   $60$  |  $25$   |   $0$   |
|   $P_5$  |   $55$  |  $85$   |   $0$   |
|   $P_6$  |   $75$  |  $115$  |   $0$   |
|   $P_7$  |   $85$  |  $60$   |   $0$   |
| $P_{7u}$ |   $85$  |  $60$   |   $30$  |
|   $P_8$  |   $100$ |  $135$  |   $0$   |
|   $P_9$  |   $145$ |  $135$  |   $0$   |
| $P_{10}$ |   $145$ |  $50$   |   $0$   |
| $P_{11}$ |   $125$ |  $25$   |   $0$   |
| $P_{12}$ |   $100$ |  $50$   |   $0$   |
| $P_{12u}$|   $100$ |  $50$   |   $30$  |
| $P_{13}$ |   $220$ |  $110$  |   $0$   |
| $P_{14}$ |   $225$ |  $125$  |   $0$   |
| $P_{15}$ |   $210$ |  $133$  |   $0$   |
| $P_{16}$ |   $180$ |  $120$  |   $0$   |
| $P_{17}$ |   $162$ |  $40$   |   $0$   |
| $P_{18}$ |   $190$ |  $25$   |   $0$   |
| $P_{19}$ |   $210$ |  $50$   |   $0$   |


</div>


### Robotics toolbox

## Contributors
* [Brayan Estupiñan](https://github.com/Brayanleo)
* [Julián Felipe Luna](https://github.com/juflunaca)

## Acknowledgements
* Professor: [Felipe Gonzalez](https://github.com/felipeg17)
* Monitor: [Manuel Lugo](https://github.com/mlugom)


## References
