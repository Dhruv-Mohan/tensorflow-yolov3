from generic_modules.FileIO import *

_config_path = '../project_config/yolov3.config'

cfg= {}
cfg["Data_Path"] = ''

write_json(_config_path, cfg)