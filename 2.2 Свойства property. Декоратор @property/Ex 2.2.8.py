class TreeObj:
    def __init__(self, indx, value=None):
        self.indx = indx
        self.value = value
        self.__left = None
        self.__right = None
    
    @property
    def left(self):
        return self.__left
    
    @left.setter
    def left(self, left):
        self.__left = left
    
    @property
    def right(self):
        return self.__right
    
    @right.setter
    def right(self, right):
        self.__right = right
    
    
        
        
class DecisionTree:
    obj, node, left = None, None, None

    @classmethod
    def predict(cls, root, x):
        root = root
        for _ in x:
            index = root.indx
            if x[index] == 1 and root.indx != -1:  # переходим на лево
               root = root.left
            elif x[index] == 0 and root.indx != -1:  # переходим на право
                root = root.right
            elif root.indx == -1:
                return root.value


    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        cls.obj = obj
        cls.node = node
        if node != None and left == True:
            node.left = obj
        elif node != None and left == False:
            node.right = obj

        cls.left = left
        return cls.obj

root = DecisionTree.add_obj(TreeObj(0))
v_11 = DecisionTree.add_obj(TreeObj(1), root)
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
v_111 = DecisionTree.add_obj(TreeObj(3), v_11)
v_112 = DecisionTree.add_obj(TreeObj(4), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "1"), v_111)
DecisionTree.add_obj(TreeObj(-1, "2"), v_111, False)
DecisionTree.add_obj(TreeObj(-1, "5"), v_12)
DecisionTree.add_obj(TreeObj(-1, "6"), v_12, False)
DecisionTree.add_obj(TreeObj(-1, "3"), v_112)
DecisionTree.add_obj(TreeObj(-1, "4"), v_112, False)

x = [1,0,1,1,0]
res = DecisionTree.predict(root, x)
print(res)