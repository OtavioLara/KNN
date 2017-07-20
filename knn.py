import random
import math


class Individual:
    count = 0
    def __init__(self, atributes=[], type=""):
        Individual.count += 1
        self.__id = Individual.count
        self.__atributes = atributes
        self.__type = type


    def getAtributes(self):
        return self.__atributes

    def euclidean_distance(self, otherElem):
        l1 = self.getAtributes()
        l2 = otherElem.getAtributes()
        sum_sqr = 0
        for i in range(len(l2)):
            print(sum_sqr)
            sum_sqr += (l2[i] - l1[i])**2
        return sum_sqr ** 0.5

    def __str__(self):
        s = ""
        for item in self.__atributes:
            s += str(item) + ", "
        return "(" + str(self.__id) + ") " + s + "[" + self.__type + "]"


class KNN:


    def __init__(self, file_name, num_blocks):
        self.__file_name = file_name
        self.__num_blocks = num_blocks
        self.__block_list = []
        self.__classifieds_per_type = []


    def loadDB(self):
        individuals =[]
        file_DB = open(self.__file_name, 'r')
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

    def loadPerPiaceDB(self):
        elem_list = self.loadDB()
        size_file = int(math.floor(len(elem_list)/self.__num_blocks))

        self.__block_list = []
        for cont_block in range(0,self.__num_blocks):
            list = []
            for i in range((cont_block*size_file),(cont_block+1)*size_file):
                list.append(elem_list[i])
            self.__block_list.append(list)

    def print_blocks(self):
        for block in self.__block_list:
            for elem in block:
                print(elem)
            print('\n')

    def train_knn(self, block):
        pass

if __name__ == '__main__':
    knn = KNN("data.txt",10);
    block_list = knn.loadPerPiaceDB()
    knn.print_blocks()