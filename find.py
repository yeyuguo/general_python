#coding=utf8
import os
def find_file(target_file,path=None):
    '''
    find 'target_file' file  in 'path'
    '''
    paths = os.listdir(path)
    for file in paths:
        path_full = path+'/'+file
        if os.path.isdir(path_full):
            find_file(target_file,path_full)
        elif file == target_file:
            print path
            print path_full
            print type(path_full)
            return path_full
