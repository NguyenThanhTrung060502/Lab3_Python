print("""======================================================
                Main exercises 
======================================================\n""")
stuffdict = {'Винтовка':(25,3,"в"), 
             'Пистолет':(15,2,"п"), 
             'Боекомплект':(15,2,"б"), 
             'Аптечка':(20,2,"а"), 
             'Ингалятор':(5,1,"и"), 
             'Нож':(15,1,"н"), 
             'Топор':(20,3,"т"),
             'Оберег':(25,1,"о"),
             'Фляжка':(15,1,"ф"),
             'Антидот':(10,1,"д"), 
             'Еда':(20,2,"к"),
             'Арбалет':(20,2,"р")          
            }
 
def get_total_score(stuffdict):
    total_score = sum([stuffdict[item][0] for item in stuffdict]) - 5
    return total_score

def get_area_value_symbol(stuffdict):
    value = [stuffdict[item][0] for item in stuffdict]
    area = [stuffdict[item][1] for item in stuffdict]
    symbol = [stuffdict[item][2] for item in stuffdict] 

    return value, area, symbol

def get_memtable(stuffdict, A=8):
    value, area, symbol = get_area_value_symbol(stuffdict)
    n = len(value)
 
    V = [[0 for a in range(A+1)] for i in range(n+1)]

    for i in range(n+1):
        for a in range(A+1):
            if i == 0 or a == 0:
                V[i][a] = 0
            elif i == 9 and a == 1:
                V[i][a] = 10
            elif area[i-1] <= a:
                V[i][a] = max(value[i-1] + V[i-1][a-area[i-1]], V[i-1][a])
            else:
                V[i][a] = V[i-1][a]

    return V, value, area, symbol

def get_selected_items_list(stuffdict, A=8):

    V, value, area, symbol = get_memtable(stuffdict)
    n = len(value)
    res = V[n][A]                
    items_list = []   
    
    for i in range(n, 0, -1): 
        if res != V[i-1][A]:          
            items_list.append((value[i-1], area[i-1], symbol[i-1]))
            res -= value[i-1]  
            A -= area[i-1]  
    return items_list

def result():
    new_stuff = get_selected_items_list(stuffdict) 

    new_arr = []
    new_arr2 = []
    survival_score = 0

    for i in new_stuff:
        i = list(i)           
        if i[1] == 1:
            new_arr.append((i[2]))
        else:
            new_arr2.append(i[2])
            new_arr2.append(i[2])
        survival_score += i[0]
    survival_score = 2*survival_score - get_total_score(stuffdict)

    return new_arr, new_arr2, survival_score

def print_result():
    element = result()
    for i in range(len(element)):
        if i != 2:
            print(element[i])
        else:
            print("Итоговые очки выживания: " + str(element[i]))
    print("\n")
print_result()

print("""======================================================
                First additional exercises 
======================================================\n""")

def get_new_memtable(stuffdict, A=7):
    value, area, symbol = get_area_value_symbol(stuffdict)
    n = len(value)
 
    V = [[0 for a in range(A+1)] for i in range(n+1)]

    for i in range(n+1):
        for a in range(A+1):
            if i == 0 or a == 0:
                V[i][a] = 0
            elif area[i-1] <= a:
                V[i][a] = max(value[i-1] + V[i-1][a-area[i-1]], V[i-1][a])
            else:
                V[i][a] = V[i-1][a]
                
    return V[n][A]

def first_additional_request():
    new_total = get_new_memtable(stuffdict)
    survival_score = 2*new_total - get_total_score(stuffdict) - 5

    if survival_score < 0:
        print("""Нет решения для случая с инвентарём в 7 ячеек !!!
Так как максимальные итоговые очки выживания = -15 меньше 0""")
    else:
        pass

first_additional_request()

print("""\n======================================================
                Second additional exercises 
======================================================\n""")

def second_additional_request(stuffdict):
    value, area, symbol = get_area_value_symbol(stuffdict)
    new_items_list = []

    for i in range(len(value)):
        if value[i] == 20 and area[i] == 2:
            new_items_list.append(symbol[i])

    array = result()
    survival_score = array[2]
    array = array[0]
    array2 = []
    array3 = []

    for i in new_items_list:
        if i != 'к' :
            array2.append(i)
            array2.append(i)
        if i != 'а':
            array3.append(i)
            array3.append(i)

    print("Первая комбинация" + "\n" + str(array))
    print(array2)
    print("Итоговые очки выживания: " + str(survival_score))

    print("\n")

    print("Вторая комбинация" + "\n" + str(array))
    print(array3)
    print("Итоговые очки выживания: " + str(survival_score))
second_additional_request(stuffdict)
      





   

