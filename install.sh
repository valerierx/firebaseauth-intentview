#!/bin/bash

sudo cp main.py /bin/intentview
cp Intent.desktop $XDG_DATA_HOME/applications/Intent.desktop
xdg-mime default Intent.desktop x-scheme-handler/intent
