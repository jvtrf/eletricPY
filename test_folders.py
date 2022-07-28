import glob

path_images = ([(p.split('/')[-1].split('_')[0].split('\\')[-1],p.replace('\\','/')) for p in glob.glob("images/icons/*")])

for p in path_images:
    print(p)