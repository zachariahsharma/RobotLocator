#!/bin/bash
git clone https://github.com/zachariahsharma/RobotLocator.git
cd RobotLocator
pip install -r "requirements.txt"
curl -d '{"finished":"false"}' -H 'localtonet-skip-warning: True' -H 'Content-Type: application/json' 6n90ghq.localto.net
python3 hyperparameter.py
curl -d '{"finished":"true"}' -H 'localtonet-skip-warning: True' -H 'Content-Type: application/json' 6n90ghq.localto.net