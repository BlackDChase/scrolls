read -p "Give dataset folder, (folder name in dataset): " x
dataset_loc="../dataset/"
PYTHONPATH=src ./train.py --dataset $dataset_loc$x --memory_saving_gradients --batch_size 2 --save_every 5000  --sample_every 2500 --optimizer sgd --learning_rate 0.0006 --model_name 345M | tee log.txt
#log for a backup, if have to kill it in on midway
#later save every 1000 with a diffrent name (maybe time stamp)
