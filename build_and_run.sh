#!/bin/bash
mkdir build

clear

if [ ! -d "app-venv" ]; then
    python3 -m venv app-venv
fi

if [ ! -d "build-venv" ]; then
    python3 -m venv build-venv
fi

source app-venv/bin/activate
pip freeze > app-requirements.txt

source build-venv/bin/activate
pip freeze > build-requirements.txt

python flatpak-pip-generator --requirements-file=app-requirements.txt --runtime='org.freedesktop.Sdk//22.08'
flatpak-builder --user --install --force-clean build/ org.flatpak.Worktimer.yml
# flatpak run --command=sh org.flatpak.Worktimer
flatpak run org.flatpak.Worktimer