from generic_modules.FileIO import *

_config_path = '../project_config/yolov3.config'

cfg= {}
cfg["Data_Path"] = '/media/dhruv/Blue22/Blue2/downloads/yolov3/total'
cfg["Base_Dir"] = '/media/dhruv/Blue22/Blue2/downloads/yolov3/'
cfg['Dataset_file']
write_json(_config_path, cfg)