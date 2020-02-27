from generic_modules.config import *

_config_path_ = '../project_config/yolov3.config'
cfg = config()
cfg.load_data(_config_path_)

with open(cfg.data["Dataset_file"], "w") as file:
  pass

def process_lines(image_path, lines):
  final_line = image_path[:-4] + '.jpg '
  for line in lines:
    c, x, y, w, h = line.split()
    w1 = float(w)/2 + float(x)
    h1 = float(h)/2 + float(y)
    print(x, y, w1 ,h1)
    x = float(x) * 1920
    y = float(y) * 1080
    w = float(w) * 1920
    h = float(h) * 1080
    x = x - w/2
    y = y - h/2

    w = x + w
    h = y + h

    final_line += str(x) + ',' + str(y) + ',' + str(w) + ',' + str(h) + ',' + c + ' '
    #final_line += c + ' '
    #input(final_line)

  final_line += '\n'

  with open(cfg.data["Dataset_file"], "a+") as file:
    file.write(final_line)

def get_file_path(file_name):
  file_path = os.path.join(cfg.data["Data_Path"], file_name)
  return file_path

def read_file(file_name):
  file_path = get_file_path(file_name)
  with open(file_path, 'r') as file:
    lines = file.readlines()
    process_lines(file_path, lines)
    #input(lines)
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