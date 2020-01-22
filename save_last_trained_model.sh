# Script to separately save the last saved checkpoint of the model
# For 345M, edit for othre ones
# Reference:https://medium.com/@ngwaifoong92/beginners-guide-to-retrain-gpt-2-117m-to-generate-custom-text-content-8bb5363d8b7f 

read -p "Model name:" x
mkdir $x
cp src/checkpoint/run1/ gpt-2/models/$x
cp src/345M/encoder.json gpt-2/models/$x
cp src/345M/hparams.json gpt-2/models/$x
cp src/345M/vocab.bpe gpt-2/models/$x
