#!/bin/bash
PWD=`pwd`
python3.11 -m venv venv

activate() {
    . $PWD/venv/bin/activate
}

activate

pip install -r requirements.txt
pip install --upgrade pip
