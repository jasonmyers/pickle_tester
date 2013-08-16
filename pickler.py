import pickle

def list_pickler(file_path, my_list):
    pickle_file = open(file_path, 'wb')
    pickle.dump(my_list, pickle_file)
    pickle_file.close()

def unpickler(file_path):
    pickle_file = open(file_path,'rb')
    another_list = pickle.load()
    pickle_file.close()
    return another_list