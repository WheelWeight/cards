import math

def wct(table,n):
    """
    the weight of the column of the table
    表格中此列宽度
    """
    llc = []#a list for lens of the column:存储

    for line in table:
        llc.append(len(line[n].encode()))#存储此竖列每项的长度

    return max(llc)#返回最大值

def lwct(table):
    """
    a list for the weights of all the columns of the table
    一个包含 表格中所有列宽度的 列表
    """
    lwct = []
    nl = len(table[0])#the number of lines:存储列数即横排项数，尽量减少计算量

    i = 0#指向第一项
    for topic in table[0]:
        lwct.append(wct(table,i))#求出并存储 此竖列每项应占格数量
        i += 1#递增

    return lwct

def d_gt(str,wct,pattern = "right"):
    """
    draw a girl of the table:
    按照给定的 单位表格宽度和模式 书写元素
    """
    ss = (wct - len(str.encode()))#the number of the spaces

    if pattern == "left":
        print(str,end = ss * " ")

    elif pattern == "mid":
        print(math.floor(ss/2)*" " + str + math.ceil(ss/2)*" ",end = "")

    elif pattern == "right":
        print(ss * " ",end = str)

    return 0

def d_r(line,lwct):
    """
    draw a row:
    按照给定的 每竖列单位表格宽度 书写一横排表格元素
    """
    i = 0

    for term in line:
        d_gt(term,lwct[i])
        i += 1
        print(" ",end="")
    print()#转行

    return 0

def d_t(table):
    """
    draw a tabel:
    画出一张表格
    """
    lw = lwct(table)
    wlf = sum(lw)

    print("-"*wlf)
    for line in table:
        d_r(line,lw)
        print("-"*wlf)

    return 0