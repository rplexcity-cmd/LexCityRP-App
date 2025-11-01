
#!/bin/bash
pkg update -y && pkg upgrade -y
pkg install python git zip unzip wget clang openjdk-17 -y
pip install buildozer cython virtualenv kivy
buildozer -v android debug
