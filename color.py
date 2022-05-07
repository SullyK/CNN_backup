import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from copy import deepcopy
import uuid
import os

from pathlib import Path
import os


# assign directory
directory = os.getcwd()

ROOT_DIR = os.getcwd()
 
files = Path(directory).glob('ara2012_plant???_label*')
for file in files:
    print(file)
    os.getcwd()
    print(os.getcwd())
    
    uniq_plant = str(file)[44:-4]
    working_dir = os.getcwd() + '/' +  uniq_plant
    print("Working Dir ", working_dir)

    if not os.path.exists(working_dir):
        re = os.makedirs(working_dir)
        print("Error: ", re)

    os.chdir(working_dir)

    fpath = str(file)  
    IMG = cv.cvtColor(cv.imread(fpath), cv.COLOR_BGR2RGB)

    H, W, C = IMG.shape
    IMG_FLATTENED = np.vstack([IMG[:, w, :] for w in range(W)])

    colors, counts = np.unique(IMG_FLATTENED, axis=0, return_counts = True)

    for color, count in zip(colors, counts):

        print("COLOR: {}, COUNT: {}".format(color, count))
        if(color == [0,0,0]).all():
            SINGLE_COLOR = (1 * np.ones(IMG.shape)).astype(np.uint8)  
            random_name = uuid.uuid4().hex
            image_gray = cv.cvtColor(SINGLE_COLOR, cv.COLOR_BGR2GRAY)            
            
            cv.imwrite(f'{working_dir}/{random_name}.png', image_gray)

            os.chdir(ROOT_DIR)
            continue
        else:
            SINGLE_COLOR = (0 * np.ones(IMG.shape)).astype(np.uint8)
            color_idx = np.all(IMG[..., :] == color, axis=-1)
            SINGLE_COLOR[color_idx, :] = (255,255,255)

            random_name = uuid.uuid4().hex            
            image_gray = cv.cvtColor(SINGLE_COLOR, cv.COLOR_BGR2GRAY)

            cv.imwrite(f'{working_dir}/{random_name}.png' , image_gray)



            os.chdir(ROOT_DIR)