#!/bin/bash
pip uninstall scalecodec cyscale -y
pip install cyscale --force-reinstall
python3 bagbot.py --nocheck
