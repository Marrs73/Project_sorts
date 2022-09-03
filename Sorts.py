# Тренировка в написания сортировочных алгоритмов и оттачивание навыков питона в целом.
from time import *
import colorama
import random as r

colorama.init()

def Bubble_sort(listik):
    unfinished = True
    while(unfinished):
        unfinished = False
        for j in range(1, len(listik)):
            if (listik[j] < listik[j-1]):
                listik[j], listik[j-1] = listik[j-1], listik[j] 
                unfinished = True
    return listik

def Selection_sort(listik):
    n = len(listik)
    for i in range(n - 1):
        max_l = listik.index(max(listik[:n - i]))
        listik[max_l], listik[n-i-1] = listik[n-i-1], listik[max_l]
    return listik

def Insertion_sort(listik):
    for i in range(1, len(listik)):
        index_sorted =  i
        while index_sorted > 0:
            if (listik[index_sorted] < listik[index_sorted-1]): 
                listik[index_sorted], listik[index_sorted-1] = listik[index_sorted-1], listik[index_sorted]
                index_sorted -= 1
            else: 
                break
    return listik
fd
def Stalin_sort(listik):
    i = 0
    edge = len(listik)
    while i < edge - 1: 
        if (listik[i] > listik[i+1]):
            listik.remove(listik[i+1])
            edge -= 1
        else: i += 1
    return listik

def Memory_quick_sort(listik):
    length = len(listik)
    
    if (length > 1):
        greater, lower = list(), list()
        deleted = listik.pop(r.randint(0, length-1))
        for i in listik:
            if (i >= deleted): greater.append(i)
            else: lower.append(i)

        return Memory_quick_sort(lower) + [deleted] + Memory_quick_sort(greater)
    else: return listik

def Check_the_sort(function): # Проверка сортировки на верность на заготовленных массивах
    checks = [[[0], [0]],
              [[3, 3, 3], [3, 3, 3]],
              [[3, 2, 1], [1, 2, 3]],
              [[-3, 0, -1], [-3, -1, 0]],
              [[9, -5, 6, 0, 0, -3, 0, 11, -15], [-15, -5, -3, 0, 0, 0, 6, 9, 11]]]
    
    result_check = [0 if function(checks[i][0]) == checks[i][1] else 1 for i in range(len(checks))]
    if (sum(result_check) == 0): return True
    else: return False
    
def Do_sort(function): # Вызов сортиро
    time_start = perf_counter()
    listik_local = [4, 5, 2, -5, 70, 3, 95, 0, 0, -56, 20, 20]
    name = str(function)[10: str(function).find("at") - 1]
    sorted_list = function(listik_local)
    time_process = perf_counter() - time_start
    print(colorama.Fore.WHITE + "-" * 100)
    print(colorama.Fore.RED + name + ":" + " " * (15 - len(name)), 
          colorama.Fore.YELLOW, sorted_list, 
          colorama.Fore.RED, " || ", Check_the_sort(function), f", t = {time_process}", sep = "")

#[Do_sort(sort) for sort in [Bubble_sort, Selection_sort, Insertion_sort, Stalin_sort, Quick_sort(0, n)]]
print(colorama.Fore.WHITE + "-" * 100)
print(Memory_quick_sort([4, 5, 2, -5, 70, 3, 95, 0, 0, -56, 20, 20]))
