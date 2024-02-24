import math
import main

def mlc(list,n):
    """
    max of lens of a column:
    一条竖列的项长度最大值
    """
    column = []

    for i in list:
        column.append(len(i[n]))#存储此竖列每项的长度

    return max(column)#返回最大值

def lmlc(list):
    """
    alist of the maxs of lens of every column:
    一个包含所有竖列的 字符串长度最大值 的列表
    """
    lmlc = []
    lr = len(list)#存储列数即横排项数，尽量减少计算量

    i = 0#指向第一项
    while i <= (lr-1):
        lmlc.append(math.ceil(mlc(list,i)/8)*8)#求出并存储 此竖列每项应占格数量
        i += 1#递增

    return lmlc

def d_gf(str,lgf):
    """
    draw a girl of the form:
    按照给定的 单位表格宽度 书写一个表格元素
    """
    nt = math.ceil((lgf-len(str))/8)#求出并存储 应输出的制表符个数

    print(str,end = "\t"*nt)

    return 0

def d_r(list,lm):
    """
    draw a row:
    按照给定的 每竖列单位表哥宽度 书写一横排表哥元素
    """
    i = 0

    print("|",end="")
    for term in list:
        d_gf(term,lm[i])
        i += 1
        print("|",end="")
    print()#转行

    return 0

def p_rc(str,len):
    """
    print a row of chars:
    输出一排字符
    """
    print(str*len)

    return 0

def d_f(form):
    """
    draw a form:
    画出一张表格
    """
    lm = lmlc(form)
    len = sum(lm)

    p_rc("*",len)

    p_rc("-",len)
    for t in form:
        d_r(t,lm)
        p_rc("-",len)
    
    p_rc("*",len)

    return 0