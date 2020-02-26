from generic_modules.config import *

_config_path_ = '../project_config/yolov3.config'
cfg = config()
cfg.load_data(_config_path_)

def process_lines(image_path, lines):
  final_line = image_path[:-4] + '.jpg '
  for line in lines:
    data = line.split()
    for i in range(1,len(data)):
      final_line += data[i] +','
    final_line += data[0] + ' '
    print(final_line)
    input(data)

def get_file_path(file_name):
  file_path = os.path.join(cfg.data["Data_Path"], file_name)
  return file_path

def read_file(file_name):
  file_path = get_file_path(file_name)
  with open(file_path, 'r') as file:
    lines = file.readlines()
    process_lines(file_path, lines)
    input(lines)
  pass

def is_file(name):
  if name[-1] == 't':
    return True
  else:
    return False

def start():
  total_files = os.listdir(cfg.data["Data_Path"])
  for file in total_files:
    if is_file(file):
      read_file(file)

if __name__ == '__main__':
  start()