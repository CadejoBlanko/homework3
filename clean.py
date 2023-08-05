import os
import sys
import shutil
from pathlib import Path
from threading import Thread

list_images = [".jpeg", ".png", ".jpg", ".svg"]
list_documents = [".doc", ".docx", ".txt", ".pdf", ".xlsx", ".pptx"]
list_audio = [".mp3", ".ogg", ".wav", ".amr"]
list_video = [".avi", ".mp4", ".mov", ".mkv"]
list_archives = [".zip", ".gz", ".tar"]

def folder_creation(path_f):

        path_f = Path(path_f)

        Path(f'{str(path_f)}/' + 'images').mkdir(parents=True, exist_ok=True)
        Path(f'{str(path_f)}/' + 'documents').mkdir(parents=True, exist_ok=True)
        Path(f'{str(path_f)}/' + 'audio').mkdir(parents=True, exist_ok=True)
        Path(f'{str(path_f)}/' + 'video').mkdir(parents=True, exist_ok=True)
        Path(f'{str(path_f)}/' + 'archives').mkdir(parents=True, exist_ok=True)

        sorter(path_f, path_f)


def sorter(folder, path_f):
    
    for el in folder.iterdir():

        if el.is_file() and el.suffix in list_images:
            shutil.move(os.path.join(folder, el.name), os.path.join(f'{str(path_f)}\\' + 'images', el.name))

        elif el.is_file() and el.suffix in list_documents: 
            shutil.move(os.path.join(folder, el.name), os.path.join(f'{str(path_f)}\\' + 'documents', el.name))

        elif el.is_file() and el.suffix in list_audio:
            shutil.move(os.path.join(folder, el.name), os.path.join(f'{str(path_f)}\\' + 'audio', el.name))

        elif el.is_file() and el.suffix in list_video:
            shutil.move(os.path.join(folder, el.name), os.path.join(f'{str(path_f)}\\' + 'video', el.name))

        elif el.is_file() and el.suffix in list_archives:
   
            name_archive = (el.name).split(".")
            Path(f'{str(path_f)}/' + 'archives/' + name_archive[0]).mkdir(parents=True, exist_ok=True)
            shutil.unpack_archive(el, f'{str(path_f)}/' + 'archives/' + name_archive[0])

        elif el.is_dir():

            if el.name == 'images' or el.name == 'documents' or el.name == 'audio' or el.name == 'video' or el.name == 'archives':
                pass
            elif len(os.listdir(el)) != 0:
                thread = Thread(target=sorter, args=(el, path_f))
                thread.start()
                thread.join()
                if len(os.listdir(el)) == 0:
                    os.rmdir(el) 
            else:
                os.rmdir(el)  
    

if __name__ == '__main__':
    folder_creation(sys.argv[1])