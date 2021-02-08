# `__class__,__new__,__init__,dir()`的使用

## `__class__`属性

实例调用`__class__`属性时会指向该实例对应的类

然后可以再去调用其它类属性，类属性由类调用
`example：`

```self.__classs__.__name__       //首先用self.__class__将实例变量指向类，然后再去调用__name__类属性```

##  `__self.__class__.__name__`

获取类名

```
class Parent(object):
  def __init__(self, name):
    self.name = name
    print("__class__:", self.__class__) // <class '__main__.Parent'> 此时的类
    print("create an instance of:", self.__class__.__name__) //Parent 此时的类名
    print("name attribute is:", self.name)

```

```python
当前位置类名是 Parent


__class__: <class '__main__.Parent'>
create an instance of: Parent
name attribute is: init Child
 

```

## dir（）

因为python中所有类默认继承object类。而object类提供了了很多原始的内建属性和方法，所以用户自定义的类在Python中也会继承这些内建属性。可以使用dir()函数可以查看，虽然python提供了很多内建属性但实际开发中常用的不多。而很多系统提供的内建属性实际开发中用户都需要重写后才会使用。对于python来说，属性或者函数都可以被理解成一个属性

```python
class Person(object):



    pass



#查看python中给对象提供的所有(内建)属性



print(dir(Person)) #使用dir()函数查看



'''



['__lass__', '__delattr__', '__dict__', '__dir__', '__doc__','__eq__', '__format__', '__ge__', '__getattribute__',



 '__gt__','__hash__', '__init__', '__init_subclass__', '__le__', '__lt__','__cmodule__', '__ne__',



 '__new__', '__reduce__', '__reduce_ex__','__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__','__weakref__']







'''
```

## 常用内建属性：__init__和__new__

```python
1.__init__方法使用与功能：



  1.用来构造初始化函数,用来给类的实例进行初始化属性，所以可以不需要返回值



  2.在创建类的实例时系统自动调用



  3.自定义类如果不定义的话，默认调用父类object的，同理继承也是，子类若无，调用父类，若有，调用自己的



class Student(object):



    def __init__(self,name):



        self.name = name



        print("这是__init__方法")



 



s = Student("tom")  



'''



这是__init__方法



'''



 



2.__new__方法使用与功能



  1.__new__功能：用所给类创建一个对象，并且返回这个对象。



  2.因为是给类创建实例，所以至少传一个参数cls,参数cls，代表要实例化的类，此参数在实例化时由Python解释器自动提供



  3.在类实例化时内部创建类实例的函数，并且返回这个实例，所以它是类实例时最先被调用的方法，一般不要人为定义该方法。



  4.因为要创建实例返回实例，所以要有返回值。return父类__new__出来的实例，或者直接是object的__new__出来的实例   



 



 



class Student(object):



    def __init__(self,name):



        self.name = name



        print("这是__init__方法")



 



    def __new__(cls, *args, **kwargs):



        print("这是__new__方法")



        return object.__new__(cls)



 



s = Student("tom")



'''结果如下：注意__new__的执行顺序在__init__之前



这是__new__方法



这是_init__方法



'''



 



3.__init__和__new__使用的联系



  1.__init__第一个参数是self，表示需要初始的实例，由python解释器自动传入，而这个实例就是这个__new__返回的实例



  2.然后 __init__在__new__的基础上可以完成一些其它初始化的动作



 



class Student(object):



    def __init__(self,name):



        self.name = name



        print("这是__init__方法")



 



    def __new__(cls, *args, **kwargs):



        print("这是__new__方法")



        id =object.__new__(cls)



        print(id) #打印这个__new__创建并返回的实例在内存中的地址



        return id



s1 = Student("JACK")



print(s1)



'''



这是__new__方法



<__main__.Student object at 0x000001EC6C8C8748>



这是__init__方法



<__main__.Student object at 0x000001EC6C8C8748>



'''



 



总结：很明显，这两个实例的内存地址一样，所以__init__接受的实例就是__new__创建的。
```

关于__new__的实际开发使用可以参考：[python使用__new__实现单例模式创建对象](https://blog.csdn.net/qq_26442553/article/details/94393191) 

### 2.常用内建属性：__class__

```python
1.__class__功能与用法：



    1.__class__功能和type()函数一样，都是查看对象所在的类。



    2.__class__可以套用



 



class Student(object):



    def __init__(self,name):



        self.name = name



stu = Student("tom")



print(type(stu),type(Student))



print(stu.__class__, Student.__class__, stu.__class__.__class__)



'''结果如下：



<class '__main__.Student'> <class 'type'>



<class '__main__.Student'> <class 'type'> <class 'type'>



'''
```

**python中的内建（内嵌）属性是系统自带的，用户不用导入包就可以直接使用的属性。如何查看python中所有的内建属性（内嵌） 呢？ 很简单，内建属性既然到处都可以使用，肯定属于全局变量，使用globals()查看所有全局变量，可以看到有一个__builtins__的属性，使用__dict__即可查看。**

```python
>>> globals()



{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'a': 10, 'AA': <class '__main__.AA'>, 'xx': {...}}



>>> AA = globals()



>>> AA['__builtins__'].__dict__



{'__name__': 'builtins', '__doc__': "Built-in functions, exceptions, and other objects.\n\nNoteworthy: None is the `nil' object; Ellipsis represents `...' in slices.", '__package__': '', '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': ModuleSpec(name='builtins', loader=<class '_frozen_importlib.BuiltinImporter'>), '__build_class__': <built-in function __build_class__>,



 '__import__': <built-in function __import__>, 'abs': <built-in function abs>, 'all': <built-in function all>, 'any': <built-in function any>, 'ascii': <built-in function ascii>, 'bin': <built-in function bin>, 'breakpoint': <built-in function breakpoint>, 'callable': <built-in function callable>, 'chr': <built-in function chr>, 'compile': <built-in function compile>, 'delattr': <built-in function delattr>, 'dir': <built-in function dir>, 'divmod': <built-in function divmod>, 'eval': <built-in function eval>, 'exec': <built-in function exec>, 'format': <built-in function format>, 'getattr': <built-in function getattr>, 'globals': <built-in function globals>, 'hasattr': <built-in function hasattr>, 'hash': <built-in function hash>, 'hex': <built-in function hex>, 'id': <built-in function id>, 'input': <built-in function input>, 'isinstance': <built-in function isinstance>, 'issubclass': <built-in function issubclass>, 'iter': <built-in function iter>, 'len': <built-in function len>, 



'locals': <built-in function locals>, 'max': <built-in function max>, 'min': <built-in function min>, 'next': <built-in function next>, 'oct': <built-in function oct>, 'ord': <built-in function ord>, 'pow': <built-in function pow>, 'print': <built-in function print>, 'repr': <built-in function repr>, 'round': <built-in function round>, 'setattr': <built-in function setattr>, 'sorted': <built-in function sorted>, 'sum': <built-in function sum>, 'vars': <built-in function vars>, 'None': None, 'Ellipsis': Ellipsis, 'NotImplemented': NotImplemented, 'False': False, 'True': True, 'bool': <class 'bool'>, 'memoryview': <class 'memoryview'>, 'bytearray': <class 'bytearray'>, 'bytes': <class 'bytes'>, 'classmethod': <class 'classmethod'>, 'complex': <class 'complex'>, 'dict': <class 'dict'>, 'enumerate': <class 'enumerate'>, 'filter': <class 'filter'>, 'float': <class 'float'>, 'frozenset': <class 'frozenset'>, 'property': <class 'property'>, 'int': <class 'int'>, 'list': <class 'list'>, 



'map': <class 'map'>, 'object': <class 'object'>, 'range': <class 'range'>, 'reversed': <class 'reversed'>, 'set': <class 'set'>, 'slice': <class 'slice'>, 'staticmethod': <class 'staticmethod'>, 'str': <class 'str'>, 'super': <class 'super'>, 'tuple': <class 'tuple'>, 'type': <class 'type'>, 'zip': <class 'zip'>, '__debug__': True, 'BaseException': <class 'BaseException'>, 'Exception': <class 'Exception'>, 'TypeError': <class 'TypeError'>, 



'StopAsyncIteration': <class 'StopAsyncIteration'>, 'StopIteration': <class 'StopIteration'>, 'GeneratorExit': <class 'GeneratorExit'>, 'SystemExit': <class 'SystemExit'>, 'KeyboardInterrupt': <class 'KeyboardInterrupt'>, 'ImportError': <class 'ImportError'>, 'ModuleNotFoundError': <class 'ModuleNotFoundError'>, 'OSError': <class 'OSError'>, 'EnvironmentError': <class 'OSError'>, 'IOError': <class 'OSError'>, 'WindowsError': <class 'OSError'>, 'EOFError': <class 'EOFError'>, 'RuntimeError': <class 'RuntimeError'>, 'RecursionError': <class 'RecursionError'>, 'NotImplementedError': <class 'NotImplementedError'>, 'NameError': <class 'NameError'>, 'UnboundLocalError': <class 'UnboundLocalError'>, 'AttributeError': <class 'AttributeError'>, 'SyntaxError': <class 'SyntaxError'>, 'IndentationError': <class 'IndentationError'>, 'TabError': <class 'TabError'>, 'LookupError': <class 'LookupError'>, 'IndexError': <class 'IndexError'>, 'KeyError': <class 'KeyError'>, 'ValueError': <class 'ValueError'>, 'UnicodeError': <class 'UnicodeError'>, 'UnicodeEncodeError': <class 'UnicodeEncodeError'>, 'UnicodeDecodeError': <class 'UnicodeDecodeError'>, 'UnicodeTranslateError': <class 'UnicodeTranslateError'>, 'AssertionError': <class 'AssertionError'>, 'ArithmeticError': <class 'ArithmeticError'>, 



'FloatingPointError': <class 'FloatingPointError'>, 'OverflowError': <class 'OverflowError'>, 'ZeroDivisionError': <class 'ZeroDivisionError'>, 'SystemError': <class 'SystemError'>, 'ReferenceError': <class 'ReferenceError'>, 'MemoryError': <class 'MemoryError'>, 'BufferError': <class 'BufferError'>, 'Warning': <class 'Warning'>, 'UserWarning': <class 'UserWarning'>, 'DeprecationWarning': <class 'DeprecationWarning'>, 'PendingDeprecationWarning': <class 'PendingDeprecationWarning'>, 'SyntaxWarning': <class 'SyntaxWarning'>, 'RuntimeWarning': <class 'RuntimeWarning'>, 'FutureWarning': <class 'FutureWarning'>, 'ImportWarning': <class 'ImportWarning'>, 'UnicodeWarning': <class 'UnicodeWarning'>, 'BytesWarning': <class 'BytesWarning'>, 'ResourceWarning': <class 'ResourceWarning'>, 'ConnectionError': <class 'ConnectionError'>, 'BlockingIOError': <class 'BlockingIOError'>, 'BrokenPipeError': <class 'BrokenPipeError'>, 'ChildProcessError': <class 'ChildProcessError'>, 'ConnectionAbortedError': <class 'ConnectionAbortedError'>, 'ConnectionRefusedError': <class 'ConnectionRefusedError'>, 'ConnectionResetError': <class 'ConnectionResetError'>, 'FileExistsError': <class 'FileExistsError'>, 'FileNotFoundError': <class 'FileNotFoundError'>, 'IsADirectoryError': <class 'IsADirectoryError'>, 'NotADirectoryError': <class 'NotADirectoryError'>, 'InterruptedError': <class 'InterruptedError'>, 'PermissionError': <class 'PermissionError'>, 'ProcessLookupError': <class 'ProcessLookupError'>, 'TimeoutError': <class 'TimeoutError'>, 'open': <built-in function open>, 'quit': Use quit() or Ctrl-Z plus Return to exit, 'exit': Use exit() or Ctrl-Z plus Return to exit, 
```

