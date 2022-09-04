# Тренировка в написания сортировочных алгоритмов и оттачивание навыков питона в целом.
# Test commit
from time import *
import colorama
import random as r

colorama.init()

def Bubble_sort(listik): 
    """
    Сортировка пузырьком.
    Сложность алгоритма:

    
    """
    r = 0
    unfinished = True
    while(unfinished):
        unfinished = False
        for j in range(1, len(listik) - r):
            if (listik[j] < listik[j-1]):
                listik[j], listik[j-1] = listik[j-1], listik[j] 
                unfinished = True
        r += 1
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

def Functional_quick_sort(nums):
   if len(nums) <= 1:
       return nums
   else:
       q = r.choice(nums)
   l_nums = [n for n in nums if n < q]
 
   e_nums = [q] * nums.count(q)
   b_nums = [n for n in nums if n > q]
   return Functional_quick_sort(l_nums) + e_nums + Functional_quick_sort(b_nums)

def Quick_sort(nums, fst=0, lst=-1):
   if (lst == -1): lst = len(nums)-1
   if (fst >= lst): return

   i, j = fst, lst
   pivot = nums[r.randint(fst, lst)]
 
   while i <= j:
       while nums[i] < pivot: i += 1
       while nums[j] > pivot: j -= 1
       if (i <= j):
           nums[i], nums[j] = nums[j], nums[i]
           i, j = i + 1, j - 1
   Quick_sort(nums, fst, j)
   Quick_sort(nums, i, lst)

def Check_the_sort(function): # Проверка сортировки на верность на заготовленных массивах
    checks = [[[0], [0]],
              [[3, 3, 3], [3, 3, 3]],
              [[3, 2, 1], [1, 2, 3]],
              [[-3, 0, -1], [-3, -1, 0]],
              [[9, -5, 6, 0, 0, -3, 0, 11, -15], [-15, -5, -3, 0, 0, 0, 6, 9, 11]]]
    
    result_check = [0 if function(checks[i][0]) == checks[i][1] else 1 for i in range(len(checks))]
    if (sum(result_check) == 0): return True
    else: return False
    
def Do_sort(function, do_show=True): # Вызов сортировок
    if (do_show == False): return 0

    time_start = perf_counter()
    listik_local = [4, 5, 2, -5, 70, 3, 95, 0, 0, -56, 20, 20]
    name = str(function)[10: str(function).find("at") - 1]
    sorted_list = function(listik_local)
    time_process = perf_counter() - time_start
    print(colorama.Fore.WHITE + "-" * 100)
    print(colorama.Fore.RED + name + ":" + " " * (15 - len(name)), 
          colorama.Fore.YELLOW, sorted_list, 
          colorama.Fore.RED, " || ", Check_the_sort(function), f", t = {time_process}", sep = "")

def Do_random_sort(function, do_show=[True, False]): # Вызов сортировок
    if (do_show[0] == False): return 0

    time_start = perf_counter()
    listik_local = [r.randint(-1000, 1000) for i in range(20000)]
    name = str(function)[10: str(function).find("at") - 1]
    copied_list = [listik_local[i] for i in range(len(listik_local))]
    if (do_show[1] == False):
        sorted_list = function(listik_local)
    elif (do_show[1] == True):
        function(listik_local)
        sorted_list = listik_local
    time_process = perf_counter() - time_start
    print(colorama.Fore.WHITE + "-" * 100)
    print(colorama.Fore.RED + name + ":" + " " * (25 - len(name)), sorted_list == sorted(copied_list), f", t = {time_process}", sep = "")
    #print(colorama.Fore.MAGENTA, sorted_list)

# Первай аргумент в списке значения ключа - вызывать ли сортировку, 
# второй показывает работает ли сортировка возвращая значение или изменяя первоначальный список непосредственно [False\True]
[Do_random_sort(name, arg) for  name, arg in 
{Bubble_sort:[False, False], 
Selection_sort:[False, False], 
Insertion_sort:[False, False], 
Stalin_sort:[True, False], 
Memory_quick_sort:[True, False],
Functional_quick_sort:[True, False],
Quick_sort:[True, True]
}.items()]


"""print(colorama.Fore.WHITE + "-" * 100)
list = [4, 5, 2, -5, 70, 3, 95, 0, 0, -56, 20, 20]
Quick_sort(list)"""
#print(Check_the_sort(Quick_sort))
