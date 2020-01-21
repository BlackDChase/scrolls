read -p "Give dataset folder, (folder name in dataset): " x
data_loc="../dataset/"
PYTHONPATH=src ./train.py --dataset $data_loc$x --memory_saving_gradients --batch_size 2 --save_every 5000 --sample_every 5000 --model_name 345M | tee logs.txt
