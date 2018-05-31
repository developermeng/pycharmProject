import os,sys,MySQLdb,time
class Operate:
    def __init__(self):
        self.__op1 = 'start'
        self.opp2 = 'end'

class DeepOperate(Operate):
    pass


if __name__ == '__main__':
    op1 = Operate()
    op2 = DeepOperate()
    print DeepOperate.__bases__
    print op2.__dict__
    print op2.__module__

