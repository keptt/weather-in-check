import pickle

def pickle_get(pickle_filename: str):
    """
    
    Arguments:
        pickle_filename {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    """    
    with open(pickle_filename, 'rb') as pickle_handle:
        return pickle.load(pickle_handle) 

def pickle_put(pickle_filename: str, data):
    """
    
    Arguments:
        pickle_filename {[type]} -- [description]
        data {[type]} -- [description]
    """    
    with open(pickle_filename, 'bw') as pickle_handle: 
        pickle.dump(data, pickle_handle)
