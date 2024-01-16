import os
#from openxlab.dataset import get
#import openxlab
#OPENXLAB_AK = os.environ.get('OPENXLAB_AK')
#OPENXLAB_SK = os.environ.get('OPENXLAB_SK')
#openxlab.login(ak=OPENXLAB_AK, sk=OPENXLAB_SK)
#get(dataset_repo='seifer08ms/ass-4bit', target_path='./') 
os.system('git clone https://www.modelscope.cn/seifer08ms/assistant-seifer-4bit.git') 
os.system('./start.sh')
