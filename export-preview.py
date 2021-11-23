#!/usr/bin/env python3

import os
import subprocess
import sys

inkscape_bin = os.environ.get("INKSCAPE_BIN", "inkscape")
size=400

cmd = (
    inkscape_bin,
    'blender',
    "--export-area-page",
    "--export-width=" + str(size),
    "--export-height=" + str(size),
    "--export-type=" + type,
    "--export-id=" + id,
    "--export-id-only",
    "--export-filename=" + out+'.'+type
)
run(cmd, env=env)


inkscape blender_icons.svg --export-area-page --export-width=32 --export-height=32 --export-type=png --export-id=nodes --export-id-only --export-filename=src/nodes.png
