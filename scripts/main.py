from pptx_extract import pptx_extract
from content_list import content_list
import os

path = 'files/ppt_presentations'

folder = os.fsencode(path)
filenames = []

for file in os.listdir(folder):
    
    filename = os.fsdecode(file)
    title, file_extension = os.path.splitext(filename)
    pptx_extract(path, filename)

print("converted all presentations in "+path+" to markdown presentations")

#  update content list
# content_list()

    
    