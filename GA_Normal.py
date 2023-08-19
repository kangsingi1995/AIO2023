from pickle import POP
import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt


#class GA_Class():
#   def __init__(self):
#      self.chromosome = chromosome
#   def create_population(self):
#      result = 0
#      return result
def generate_random_value():
   return random.randint(0,1)

def create_population(size_individual = 1, size_chromosome = 1):
   return [generate_random_value() for _ in range(n)]

def fitness_GA(population):
   return sum(i for i in population)

def selection_GA(population):
   '''/brief  Thay đổi vị trí 1 giá trị trong cá thể để tăng giá trị'''
   index1 = random.randint(0, m-1)
   index2 = random.randint(0, m-1)
   # tạo ra 2 index để truy cập vào mảng - nếu 2 index random giống nhau thì tạo lại
   while(index1 == index2):
      index2 = random.randint(0, m-1)
   
   # Tạo 1 biến lưu trữ giá trị tại vị trí index1 của quần thể
   # Nếu vị trí 2 lớn hơn vị trí 1 - Chỗ này ngược lại cũng dc ko qtrong
   # swap 2 giá trị cá thể với nhau
   individual_s = population[index1]
   if index2 > index1:
      individual_s = population[index2]

   return individual_s

def Crossover_GA(population_1, population_2, rate = 0.9):
   chromosome_new_1 = population_1.copy()
   chromosome_new_2 = population_2.copy()

   for i in range(n):
       if random.random() < rate:
         chromosome_new_1[i] = population_2[i]
         chromosome_new_2[i] = population_1[i]

   return chromosome_new_1, chromosome_new_2

def Mutation_GA(population, rate = 0.05):
    '''Đột biến ngẫu nhiên giá trị của cá thể để tăng giá trị của cá thể'''
    population_Mutation = population.copy()

    for i in range(n):
        if random.random() < rate:
            population_Mutation[i] = random.randint(0,1)
    return population_Mutation

n = 20 #  size of individual (chromosome)
m = 50 # size of population
n_generation = 100

def main():
    population_loop = 0
    fitness_data = []
    # Tạo ra quần thể ban đầu
    population = [create_population(n) for _ in range(m)]


    for i in range(n_generation):
        # Thêm tổng điểm của 1 cá thể trong quần thể - Mục đích visualize
        fitness_data.append(fitness_GA(population[m-1]))

        new_population = []
        while(len(new_population) < m):
            # sắp xếp lại thứ tự quần thể từ bé đến lớn
            sorted_population = sorted(population, key = fitness_GA)

            # lựa chọn 2 cá thể tốt một cách ngẫu nhiên
            Selection_population_1 = selection_GA(sorted_population)
            Selection_population_2 = selection_GA(sorted_population)

            # Exchange cá thể để nâng cao giá trị của cá thể một cách ngẫu nhiên
            corssOver_population_1, corssOver_population_2 =  Crossover_GA(Selection_population_1, Selection_population_2) 

            # Đột biến cá thể
            Mutation_population_1 = Mutation_GA(corssOver_population_1)
            Mutation_population_2 = Mutation_GA(corssOver_population_2)

            # Thêm cá thể mới vào quần thể mới
            new_population.append(Mutation_population_1) 
            new_population.append(Mutation_population_2) 



    sorted_population_new = sorted(new_population, key = fitness_GA) # sắp xếp lại thứ tự quần thể từ bé đến lớn
    for i in population:
       print(i)
    print("\nQuần thể dc sắp xếp")
    for j in sorted_population:
       print(j)
    print("\nQuần thể sau khi crossover")
    for j in sorted_population_new:
       print(j)

    number_list = list(range(m))
    #number_list = number_list[:1000]
    fig, ax = plt.subplots()
    y = [sum(i) for i in sorted_population_new]
    #ax.set(xlim=(0, 8), xticks=np.arange(1, 8))
    ax.plot(number_list, y)
    plt.show()

if __name__ == "__main__":
    main()



#for j in selection:
#   print(j)