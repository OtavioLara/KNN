import random
import math

class Individual():
    id = 0
    def __init__(self, atributes=[], type=""):
        Individual.id += 1
        self.__atributes = atributes
        self.__type = type

    def __str__(self):
        s = ""
        for item in self.__atributes:
            s += str(item)+", "
        return s +"["+ self.__type+"]"

    def getAtributes(self):
        return self.__atributes

def loadDB(name):
    individuals =[]
    file_DB = open(name, 'r')
    full_text = file_DB.readlines()
    for line in full_text:
        line = line.replace('\n', '')
        atribute_list_str = line.split(',')
        atribute_list_int = []
        for i in range(len(atribute_list_str)-1):
            atribute_list_int.append(float(atribute_list_str[i]))
        type = atribute_list_str.pop()
        individuals.append(Individual(atribute_list_int,type))
    random.shuffle(individuals)
    return individuals

def loadPerPiaceDB(name, size):
    elem_list = loadDB(name)
    size_file = int(math.floor(len(elem_list)/size))

    block_list = [[] for i in range(size)]
    for cont_block in range(0,size):
        list = []
        for i in range((cont_block*size_file),(cont_block+1)*size_file):
            list.append(elem_list[i])
        block_list[cont_block] = list

    return block_list

def euclidean_distance(elem1, elem2):
    l1 = elem1.getAtributes()
    l2 = elem2.getAtributes()
    sum_sqr = 0
    for i in range(len(l2)):
        print(sum_sqr)
        sum_sqr += (l2[i] - l1[i])**2
    return (sum_sqr ** 0.5)

if __name__ == '__main__':
    lista_elem = loadPerPiaceDB("data.txt",10)


    # print(euclidean_distance(lista_elem[0], lista_elem[1]))
    # for elem in lista_elem:
    #     print(elem)
