#!/usr/bin/env python3

import os
import re
import subprocess
import sys
from os import path

SRC = "src"
OUT = "out"
SIZE = 32
BASEDIR = os.path.abspath(os.path.dirname(__file__))

def run(cmd, *, env=None):
    print("   ", " ".join(cmd))
    subprocess.check_call(cmd, env=env)

env = {}

# Developers may have ASAN enabled, avoid non-zero exit codes.
env["ASAN_OPTIONS"] = "exitcode=0:" + os.environ.get("ASAN_OPTIONS", "")

# These NEED to be set on windows for python to initialize properly.
if sys.platform[:3] == "win":
    env["PATHEXT"] = os.environ.get("PATHEXT", "")
    env["SystemDrive"] = os.environ.get("SystemDrive", "")
    env["SystemRoot"] = os.environ.get("SystemRoot", "")

inkscape_bin = os.environ.get("INKSCAPE_BIN", "inkscape")

def export_png(id:str, out:str, size:int, type="png"):
    cmd = (
        inkscape_bin,
        os.path.join(SRC, id+'.svg'),
        "--export-area-page",
        # "--export-width=" + str(size),
        # "--export-height=" + str(size),
        "--export-type=png",
        "--export-filename=" + out+'.'+type
    )
    run(cmd, env=env)

def export_svg(id:str, out:str, size:int):
    cmd = (
        inkscape_bin,
        os.path.join(SRC, id+'.svg'),
        "--export-area-page",
        "--export-type=svg",
        "--export-plain-svg",
        "--export-filename=" + out+'.svg'
    )
    run(cmd, env=env)

if not path.exists(OUT):
    os.mkdir(OUT)
for f in [f for f in os.listdir('src') if re.match(r'[a-z]+.*\.svg', f)]:
    id = f.split('.')[0]
    basepath = os.path.join(OUT, id)
    export_png(id, basepath, SIZE, 'png')
    export_svg(id, basepath, SIZE)

# cmd = (
#     blender_bin, "--background", "--factory-startup", "-noaudio",
#     "--python", datatoc_icon_split_py, "--",
#     "--image=" + os.path.join(BASEDIR, "blender_icons32.png"),
#     "--output=" + os.path.join(BASEDIR, "blender_icons32"),
#     "--output_prefix=icon32_",
#     "--name_style=UI_ICONS",
#     "--parts_x", "26", "--parts_y", "30",
#     "--minx", "6", "--maxx", "106", "--miny", "6", "--maxy", "16",
#     "--minx_icon", "4", "--maxx_icon", "4", "--miny_icon", "4", "--maxy_icon", "4",
#     "--spacex_icon", "2", "--spacey_icon", "2",
# )
# run(cmd, env=env)
