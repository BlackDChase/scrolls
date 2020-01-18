#!/usr/bin/env bash

git clone 'https://github.com/nshepperd/gpt-2.git'
cd gpt-2
pip3 install -r requirements.txt # install required modules
python3 download_model.sh 345M # download original OA model, medium
mv ../finetune.sh ./
./finetune.sh
../dataset/clean_fantasy/
