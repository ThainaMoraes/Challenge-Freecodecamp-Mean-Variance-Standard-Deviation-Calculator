import numpy as np
import random

def calculate(matrix):
    dictionary = {}
    list_np = [np.mean, np.var, np.std, np.max, np.min, np.sum]
    name_np = ['mean','variance','standard devitation','max','min','sum']
    dictionary = {}

    for i  in range(6):
        axis1 = [list_np[i](x) for x in zip(*matrix)]
        axis2 = [list_np[i](x) for x in zip(matrix)]

        flattened  = list_np[i](axis1 + axis2)
        dictionary[name_np[i]] = [axis1, axis2, flattened]
    
    print('matrix:\n', matrix)
    print('-'*10)
    print('calculator:\n', dictionary)
    return matrix, dictionary

def check(input_answer):
    valid = False
    while not valid:
            try:
                input_numbers = input('Type 9 numbers:\n ')
                input_lis = input_numbers.split()
                input_listt = [float(i) for i in input_lis]
                
                if len(input_listt) == 9:
                    listt_to_matrix = [input_listt[i-3:i] for i in np.arange(3,10,3)]
                    listt_to_matrix = [input_listt[i-3:i] for i in np.arange(3,10,3)]
                    matrix = np.array(listt_to_matrix)  
                    valid = True
                return matrix
            except:
                print ("\nList must contain nine numbers!\n")

def initiate(input_answer):   
    
    if input_answer == 1:     
        matrix = check(input_answer)
        
    elif input_answer == 2:
        input_listt = [random.randint(0,100) for i in range(9)]
        listt_to_matrix = [input_listt[i-3:i] for i in np.arange(3,10,3)]
        matrix = np.array(listt_to_matrix) 
        
    else: first()
        
    return matrix

def first():
    valid = False
    while not valid:
            try:
                print("\nDo you want to create your matrix or generate a random one?\n ")
                print("1 - My own matix")
                print("2 - Random matix")
                input_answer = int(input("\n What is your choice? \n "))
                
                if input_answer == 1 or input_answer==2:
                    matrix = initiate(input_answer)
                    return matrix
                    valid = True
                
            except ValueError:
                print ("You didn't type a number!\n")
      


def init():
    matrix =  first()
    return matrix
  