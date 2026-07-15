#        模块下的功能
#        对列表进行降序排序(不修改原列表) :
#            def sort1(l) -> list:
#
#        对列表进行升序排序(不修改原列表):
#            def sort2(l) -> list:
#
#        获取列表中所有与指定元素重复的元素下标，并返回这些下标所组成的列表
#             def find_index(l, n) -> list:


def sort1(l) -> list:
    newList = l.copy()
    newList.sort()
    return newList[::-1]
def sort2(l) -> list:
    newList = l.copy()
    newList.sort()
    return newList
def find_index(l: list, n) -> list:
    idx = []
    for i in range(len(l)):
        if l[i] == n:
            idx.append(i)
    return idx