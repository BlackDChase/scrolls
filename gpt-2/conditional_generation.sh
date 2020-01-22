read -p "Give dataset folder, folder in dataset: " x
dataset_loc="../dataset/"
python3 src/interactive_conditional_samples --temperature 0.8 --top_k 40 --model_name $dataset_loc$x
