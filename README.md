# Industrial robotics
This repository contains the development of the laboratory practice of the robotics class at the Universidad Nacional de Colombia. This practice consists of using the industrial manipulator ABB IRB 140 to traverse a path on a paper and draw the initials of the name of each [team](#contributors) member.

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
