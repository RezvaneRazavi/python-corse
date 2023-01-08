import os
import imageio

file_list = sorted(os.listdir("Assignment-8/pic/"))
IMAGES = []

for file_name in file_list:
  file_path = "Assignment-8/pic/" + file_name
  image = imageio.imread(file_path)
  IMAGES.append(image)

imageio.mimsave('patterns.gif', IMAGES, format = 'GIF-PIL', fps = 100)