#!/bin/bash

x-terminal-emulator --title="SilentTrinity server" -e "./server_start.sh ; $SHELL"
sleep 2
x-terminal-emulator --title="SilentTrinity client" -e "./client_start.sh ; $SHELL"
x-terminal-emulator --title="SilentTrinity loggueur" -e "./loggueur_start.sh ; $SHELL"
