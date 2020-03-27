<a href="https://gmic.eu">![G'MIC Logo](https://gmic.eu/img/logo4.jpg)</a>
<a href="https://www.blender.org">![Blender3d Logo](https://download.blender.org/branding/blender_logo_socket.png)</a>

#### 
#### Blender 3d Add-on for G'MIC - A Full-Featured Open-Source Framework for Image Processing
##### https://gmic.eu
# gmic-blender


This WIP official G'MIC plugin for [Blender3D 2.8x](https://www.blender.org/) uses the [G'MIC Python binding](https://github.com/dtschump/gmic-py) and will add new Nodes to Blender3d without forking Blender's code. This project is under the CeCILL-A free software license.

Estimated time of arrival of 1 first generic Node: mid-february 2020.

This is being worked on at the [GREYC](https://www.greyc.fr/) Image public research laboratory in Caen, France, with temporary funding by the [INS2I CNRS Information & Interaction Sciences Institute](https://ins2i.cnrs.fr/fr/institut).

## Installing
For now, gmic can be imported from Blender's Python :) The addon should work on Linux and MacOS.
On MacOS you may need to install libomp and fftw first yourself using Homebrew: `brew install libomp fftw`.
1. [Head over to the Releases section an early zip addon archive.](https://github.com/myselfhimself/gmic-blender/releases)
1. [Add the gmic-blender addon .zip to Blender as a 3rd-party addon.](https://docs.blender.org/manual/en/latest/editors/preferences/addons.html#rd-party-add-ons)
1. [Open up a text editor view into Blender](https://docs.blender.org/manual/en/latest/editors/text_editor.html), type "import gmic" and execute it with `Alt+P`.

## Test Driven Development
We are using a Blender Python Pytest framework named [blender-addon-tester](https://github.com/douglaskastle/blender-addon-tester).
