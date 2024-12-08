#!/bin/bash

# Upgrade pip, setuptools, and wheel to the latest versions
python -m pip install --upgrade pip setuptools wheel

# Install dependencies from requirements.txt (no cache to avoid issues)
pip install --no-cache-dir -r requirements.txt
