import random
import functools

def decorator_to_str(func):
    def wrapper_function(*args,**kwargs):
        return(str(func(*args,**kwargs)))
    return wrapper_function


@decorator_to_str
def add(a, b):
    return a + b


@decorator_to_str
def get_info(d):
    return d['info']


def ignore_exception(exception):
    def decorator(func):
        def wrapper_function(*args,**kwargs):
            try :
                return func(*args,**kwargs)
            except exception as e :
                return None
        return wrapper_function
    return decorator                
    return lambda x: x


@ignore_exception(ZeroDivisionError)
def div(a, b):
    return a/b 


@ignore_exception(TypeError)
def raise_something(exception):
    raise exception


# exercise 4
class CacheDecorator:
    """Saves the results of a function according to its parameters"""
    def __init__(self):
        self.cache = {}

    def __call__(self, func):
        def _wrap(*a, **kw):
            if a[0] not in self.cache:
                self.cache[a[0]] = func(*a, **kw)
            return self.cache[a[0]]

        return _wrap


class MetaInherList(type):
    def __init__(self,name,bases,attrs):
        print("hello")
    def __new__(self,name,bases,attrs):
        self.list = [1,2,3]
        return type(name,bases,attrs)    
        
    pass    
   
   
     


class Ex:
    x = 4


class ForceToList(Ex, metaclass=MetaInherList):
    y=10
    pass



def random_gen():

   ran= random.randint(10,20)
   print(ran)
   while(ran != 15) :
    ran= random.randint(10,20)
    print(ran)
   
pass 




#random_gen()
#div(5,0)
c=ForceToList()





