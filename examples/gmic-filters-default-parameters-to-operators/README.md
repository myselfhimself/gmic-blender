Those scripts are not production quality, but I wanted them to be stored in
some safe place in order to reuse their good parts some day when needed.
The latest script in the list below (`bpy_operators_scripts.py`) was showcased at the LGM 2020 within the G'MIC+Blender presentation in the last Blender demo chapter.

`default_parameters_gmic_py.py` was created from https://gmic.eu/filters290.json
in some obscure way, maybe using this bash command: `cat /tmp/fff | cut -d' ' -f5,6 | sed "s/[^ ][^ ]*/'&'/g" | sed 's/ /: /g' | paste -s --delimiters="," > default_parameters_gmic_py.py`

`make_operators.py` is a blender python script generator create 1 Operator class per G'MIC filters calling the latter's default parameters (tentatively..)

`bpy_operators_scripts.py` is the resulting file, a generated python script for Blender 2.8x that can be run within Blender's Text editor with `Alt+P`
