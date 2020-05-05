!pip install tensorflow==1.15.2 	tflearn==0.3.2 	
!pip install -q gpt-2-simple
import gpt_2_simple as gpt2
from datetime import datetime
from google.colab import files

!nvidia-smi
#Checks GPU

gpt2.download_gpt2(model_name="124M")
#Loads a lighter varient of the model todemonstrate fine tuning

fantasy = "filter_clean_fantasy.txt"
# Or any other text file to be trained

sess = gpt2.start_tf_sess()
gpt2.finetune(sess,
              dataset=fantasy,
              model_name='124M',
              steps=100,
              restore_from='fresh',
              run_name='fantasy3',
              print_every=2,
              sample_every=5,
              save_every=10
              )
#Stop to see if it's trained enough

gpt2.copy_checkpoint_to_gdrive(run_name='fantasy3')
input_text="I was riding a cycle when"
#this is where we enter the text to get suggestions
#Other hyperparameters
length=20
top_p=0.5
temperature=0.9
top_k=0.8
#To be used while running

gpt2.generate(sess,
              prefix=input_text,
              length=length,
              temperature=temperature,
              top_p=top_p,
              top_k=top_k,
              nsamples=5,
              batch_size=5,
              include_prefix=False,
              return_as_list=True
              )
# Loads suggestions

gpt2.copy_checkpoint_to_gdrive()
