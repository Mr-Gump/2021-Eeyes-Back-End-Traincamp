# 1、__getattr__

当我们访问一个不存在的属性的时候，会抛出异常，提示我们不存在这个属性。而这个异常就是__getattr__方法抛出的，其原因在于他是访问一个不存在的属性的最后落脚点，作为异常抛出的地方提示出错再适合不过了。

看例子，我们找一个存在的属性和不存在的属性。

```python
class A(object):



    def __init__(self, value):



        self.value = value



 



    def __getattr__(self, item):



        print "into __getattr__"



        return  "can not find"



 



a = A(10)



print a.value



# 10



print a.name



# into __getattr__



# can not find
```

可以看出，访问存在的属性时，会正常返回值，若该值不存在，则会进入最后的兜底函数__getattr__。

# 2、__setattr__

在对一个属性设置值的时候，会调用到这个函数，每个设置值的方式都会进入这个方法。

```python
class A(object):



    def __init__(self, value):



        print "into __init__"



        self.value = value



 



    def __setattr__(self, name, value):



        print "into __setattr__"



        if value == 10:



            print "from __init__"



        object.__setattr__(self, name, value)



 



 



a = A(10)



# into __init__



# into __setattr__



# from __init__



print a.value



# 10



a.value = 100



# into __setattr__



print a.value



# 100
```

在实例化的时候，会进行初始化，在__init__里，对value的属性值进行了设置，这时候会调用__setattr__方法。

在对a.value重新设置值100的时候，会再次进入__setattr__方法。

需要注意的地方是，在重写__setattr__方法的时候千万不要重复调用造成死循环。

比如：

```python
class A(object):



    def __init__(self, value):



        self.value = value



 



    def __setattr__(self, name, value):



        self.name = value
```

这是个死循环。当我们实例化这个类的时候，会进入__init__，然后对value进行设置值，设置值会进入__setattr__方法，而__setattr__方法里面又有一个self.name=value设置值的操作，会再次调用自身__setattr__，造成死循环。

除了上面调用object类的__setattr__避开死循环，还可以如下重写__setattr__避开循环。

```python
class A(object):



    def __init__(self, value):



        self.value = value



 



    def __setattr__(self, name, value):



        self.__dict__[name] = value



 



 



a = A(10)



print a.value



# 10
```

# 3、__delattr__

__delattr__是个删除属性的方法

```python
class A(object):



    def __init__(self, value):



        self.value = value



 



    def __delattr__(self, item):



        object.__delattr__(self, item)



 



    def __getattr__(self, item):



        return "when can not find attribute into __getattr__"



 



 



 



a = A(10)



print a.value



# 10



del a.value



print a.value



# when can not find attribute into __getattr__
```

__delattr__也要避免死循环的问题，就如__setattr__一样，在重写__delattr__，避免重复调用。