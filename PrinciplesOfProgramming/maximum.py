import os

folder ="E:\\Archives\\AdobeProducts\\PSD Files\\PSD_tools\\Brushes\\ Oil-Brush-Pack-1.0\\_ard_brsh\\ardd"
file_formats = ['.jpg', '.JPG', '.psd']
for filename in os.listdir(folder):
    infilename = os.path.join(folder,filename)
    if not os.path.isfile(infilename): continue
    oldbase = os.path.splitext(filename)
    #newname = infilename.replace('.JPG', '.jpgjpg')
    #newname = infilename.replace('.jpg', '.jpgjpg')
    #newname = infilename.replace('.psdsd', '.psd')
    #newname = infilename.replace('.psd', '.psdsd')
    newname = infilename.replace('.JPGjpg', '.JPG')
    output = os.rename(infilename, newname)