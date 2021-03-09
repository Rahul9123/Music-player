import sys
from cx_Freeze import *
includefiles = ['music.ico','browsing.png','play.png','pause.png','stop.png','resume.png','mute.png','unmute.png','volume-up.png','volume-down.png']
excludes =[]
packages =[]
base = None

if sys.platform =="win64":
    base = "Win64GUI"

shortcut_table =[
    ( "DesktopShortcut", # shortcut
      "DesktopFolder", #Directory
      "Simple Music Player", #Name
      "TARGETDIR", #Component
      "TARGETDIR\simplemusicplayer.exe", #Target
      None, # Arguments
      None, #Description
      None, #Hotkey
      None, #Icon
      None, #ShowCmd
      "TARGETDIR", #WkDir
    )
]

msi_data = {"Shortcut":shortcut_table}

bdist_msi_option = {'data':msi_data}
setup(
    version = "0.1",
    description = "Simple Music Player Developed By Rahul Kumar",
    author = "Rahul Kumar",
    name = "Simple Music Player",
    options = {'build_exe': {'include_files':includefiles},"bdist_msi":bdist_msi_option},
    executables=[
        Executable(
            script='simplemusicplayer.py',
            base=base,
            icon='music.ico'
        )
    ]
)