"""
программа регулировки направления дрона БПЛА на основе нечеткой логики, угол отклонения -125+125 градусов
"""

import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

#определение значений нечетких лингвистических переменных
fVLN=-125 #Очень большое отрицательное
fLN=-90 #Большое отрицательное
fMN=-55 #Среднее отрицательное
fSN=-20 #Малое отрицательное
fNO=0 #Нулевое
fSP=20 #Малое положительное
fMP=55 #Среднее положительное
fLP=90 #Большое положительное
fVLP=125 #Очень сильное положительное

rule = []


def mu(x,A):
    """
    функция меры принадлежности переменной к нечеткому множеству в виде функции Гаусса.
    :param x: х Элемент из Х
    :param A: Нечеткое множество Ã
    :return: Мера принадлежности
    """
    return math.exp((-(x-A)**2)/(2*(30**2)))

# def mu(x, A):
#     #     """
#     #     функция меры принадлежности переменной к нечеткому множеству в виде треугольника
#     #     :param x: х Элемент из Х
#     #     :param A: Нечеткое множество Ã
#     #     :return: Мера принадлежности
#     #     """
#     if ((x < (-125+A)) or (x > (125+A))):
#         return 0.0
#     elif x < (0+A):
#         return (x-(-125+A))/((0+A)-(-125+A))
#     else:
#         return (1.0-((x-(0+A))/((125+A)-(0+A))))



def addrule(fe, op, fde, z):
    """
    :param fe: fe значение лингвистической переменной "отклонение" для ошибки
    :param op: op оператор И / ИЛИ
    :param fde: fde значение лингвистической переменной "отклонение" первой разности ошибки
    :param z: z значение лингвистической переменной "воздействие"
    :return:
    """
    rule.append([fe, op, fde, z])

addrule(fNO,'AND',fNO,fNO)#Нулевое
addrule(fVLN,'OR',fVLN,fVLP)#fLN Большое отрицательное fLP Большое положительное
addrule(fVLP,'OR',fVLP,fVLN)
addrule(fLN,'AND',fSN,fVLP)#fSN #Малое отрицательное
addrule(fLP,'AND',fSP,fVLN)
addrule(fSN,'AND',fSN,fSP)
addrule(fSP,'AND',fSP,fSN)

def processRules(e,de):
    """
    e=50 de=-30, то было то 80, а стало 50, то есть воздействие туда куда надо
    :param e: e текущая ошибка
    :param de: de первая разница ошибок
    :return: Управляющее воздействие
    """
    summ_alpha_c = 0
    summ_alpha = 0
    for i in range(0, len(rule)):
        alpha = 0 #
        mue = 0 # степень соответствия ошибки нечеткому множеству fe для i-го правила
        mude = 0 # степень соответствия первой разности ошибки нечеткому множеству fde для i-го правила
        mue = mu(e, rule[i][0])
        mude = mu(de, rule[i][2])
        if rule[i][1]=='AND':
            alpha = min(mue,mude)
        elif rule[i][1]=='OR':
            alpha = max(mue,mude)
        #print(i, alpha)
        summ_alpha_c += (alpha * rule[i][3])
        summ_alpha += alpha
    return summ_alpha_c / summ_alpha

print(processRules(10,-30))



