class Zoo(object):

    def __init__(self,name):
        self.name = name
        self.animals = []

    def add_animal(self,animal):
        if animal in self.animals:
            print(f'已经有{animal.name},无法重复添加')
        else:
            self.animals.append(animal)
            animal_kind = animal.__class__.__name__
            setattr(self,animal_kind,animal)


class Animal(object):
    kind_dict = {'小':0,'中等':1,'大':2}

    def __new__(cls,*args):
        if cls.__name__ == 'Animal':
            print('Animal不能被实例化!')
        else:
            return super().__new__(cls)

    def __init__(self,kind,shape,chara):
        self.kind = kind
        self.shape = Animal.kind_dict[shape]
        self.chara = chara
        #“体型 >= 中等”并且是“食肉类型”同时“性格凶猛”
    @property
    def is_fierce(self):
        if self.shape >= 1 and self.kind == '食肉' and self.chara == '凶猛':
            return True
        else:
            return False


class Cat(Animal):
    sound = 'miao~'

    def __init__(self,name,kind,shape,chara):
        super().__init__(kind,shape,chara)
        self.name = name
    @property
    def fit(self):
        if self.is_fierce == True:
            return False
        else:
            return True


class Dog(Animal):
    sound = 'wolf~'

    def __init__(self , name , kind , shape , chara):
        super().__init__(self,kind , shape , chara)
        self.name = name

    @property
    def fit(self):
        if self.is_fierce == True:
            return False
        else:
            return True



if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1' , '食肉' , '小' , '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    print(cat1.__dict__)
    have_cat = hasattr(z , 'Cat')
    print(have_cat)