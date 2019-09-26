import project_configuration as conf
from imutils import paths
import random
import shutil
import os

# Acquire all the image file paths from the orig data
imagepaths = list(paths.list_images(conf.ORIGINAL_INPUT_DATASET))
random.shuffle(imagepaths)

split = int(len(imagepaths) * 0.8)
trainpaths = imagepaths[:split]
testpaths = imagepaths[split:]

split = int(len(imagepaths) * 0.1)
valpaths = trainpaths[:split]
trainpaths = trainpaths[split:]

datasets = [('training',trainpaths, conf.TRAIN_PATH),
            ('validation',valpaths , conf.VAL_PATH),
            ('testing',testpaths , conf.TEST_PATH)]

for (datatype, paths_to_images , output_path) in datasets:
    print('Building {} split'.format(datatype))

    if not os.path.exists(output_path):
        print('Creating Directory {}'.format(output_path))
        os.makedirs(output_path)
    
    for path in paths_to_images:
        filename = path.split(os.path.sep)[-1]
        label = filename[-5]
        
#        Building output path based on label
        labelpath = os.path.sep.join([output_path,label])
        
        if not os.path.exists(labelpath):
            print('Creating Directory {}'.format(labelpath))
            os.makedirs(labelpath)
            
#            Lets copy each file to its respective directory
        target_file_path = os.path.sep.join([labelpath,filename])
        shutil.copy2(path,target_file_path)