import os


UNLABELED = "../splited/train/tiles_test/"



if __name__ == "__main__":
    files = os.listdir(UNLABELED)
    print(len(files))
