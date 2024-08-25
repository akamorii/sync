import os
from config import PATH_x

all_files = [] #хранит все найденные файлы


os.chdir(PATH_x)
def deep_search():
    global all_files
    for i in os.listdir():
        
        if os.path.isdir(i):
            os.chdir(os.getcwd()+f'\{i}')
            # print(os.getcwd())
            deep_search()
            
        else:
            all_files.append(i)
            
    os.chdir(os.getcwd()+"/..")
    
    
def main():
    deep_search()


if __name__ == "__main__":
    main()
    print(all_files)