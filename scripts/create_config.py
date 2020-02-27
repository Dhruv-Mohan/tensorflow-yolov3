from generic_modules.FileIO import *

_config_path = '../project_config/yolov3.config'

cfg= {}
cfg["Data_Path"] = 'C:\\Users\\Dhruv\\Documents\\Dataset\\yolo_test\\2\\2\\'
cfg["Base_Dir"] = 'C:\\Users\\Dhruv\\Documents\\Dataset\\yolo_test\\'
cfg['Dataset_file'] = 'C:\\Users\\Dhruv\\Documents\\Dataset\\yolo_test\\input\\dataset.txt'
cfg['Classes'] = 'C:\\Users\\Dhruv\\Documents\\Dataset\\yolo_test\\input\\classes.names'
write_json(_config_path, cfg)