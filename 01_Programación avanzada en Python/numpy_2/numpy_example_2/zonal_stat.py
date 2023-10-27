import numpy as np


def read_data(fname: str, tipo: type) -> np.ndarray:
   """
    funtion that returns an array of a file.txt
    :param fname: str
        adress of the file in string format
    :param tipo: type
        type of the values (float, integer, ...) contained in the file
    :return: ndarray
        array containing the data in the selected file
    """
    d=np.loadtxt(fname, dtype=tipo)
    return d 

def set_of_areas(zonas: np.ndarray)-> set[int]:
    """
    function that returns a set of unique zones
    :param zonas: np.array
        array of the different zones as intergers
    :return: set
        set of individual values for set
    Examples:
    --------
    >>> set_of_areas(np.arange(10).reshape(5, 2))
    {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    >>> set_of_areas(np.zeros(10, dtype=np.int_).reshape(5, 2))
    {0}
    >>> set_of_areas(np.array([2, 3, 4, 2, 3, 4], dtype=np.int_).reshape(3, 2))
    {2, 3, 4}
    >>> set_of_areas(np.zeros(3, dtype=np.float_))
    Traceback (most recent call last):
        ...
    TypeError: The elements type must be int, not float64
    """
    return set(np.unique(zonas))

def mean_areas(zonas:[int], valores:[float]) ->[float]:
    
    """
    function that returns the average value of valores for each zone
    :param zonas: ndarray
        array with zones markated as different integers
    param valores: ndarray
        array with a values for each zone
    :return: ndarray
       array same size as input with the mean of the values per zone
    Examples
    --------
    >>> mean_areas(np.array([1, 1, 2, 2]),np.array([1,9,4,6]))
    array([5., 5., 5., 5.])
    >>> mean_areas(np.array([1, 1, 2, 2]),np.array([1,10,4,7]))
    array([5.5, 5.5, 5.5, 5.5])
    >>> mean_areas(np.array([1, 1, 2, 2, 5]),np.array([1,10,4,7]))
    IndexError: input arrays are not equal in shape. valores size:(4,) and zonas size: (5,)
    
    """
    try:
        calculo=np.array([np.mean(valores[zonas==x]) for x in zonas.flatten()])
        return np.around(calculo.reshape(np.shape(zonas)), decimals=1)
    except IndexError:
        
        print(f"IndexError: input arrays are not equal in shape. valores size:{valores.shape} and zonas size: {zonas.shape}")
        
        

# ------------ test  --------#
import doctest

def test_doc()-> None:
    """
    The following instructions are to execute the tests of same functions
    If any test is fail, we will receive the notice when executing
    :return: None
    """
    doctest.run_docstring_examples(read_data, globals(), verbose=True)  # vemos los resultados de los test que fallan
    doctest.run_docstring_examples(set_of_areas, globals(), verbose=True)  # vemos los resultados de los test que fallan
    doctest.run_docstring_examples(mean_areas, globals(), verbose=True)  # vemos los resultados de los test que fallan


if __name__ == "__main__":
    test_doc()   # executing tests

