# Python code to find frequency of each word 
def wordCounter(sentence):    
    sentence = sentence.replace('.',' ')
    sentence = sentence.replace(',',' ')    
    sentence = sentence.split()  
    sentence2 = [] 
    for i in sentence:            
        if i not in sentence2:          
            sentence2.append(i)              
    for i in range(0, len(sentence2)):  
        if sentence.count(sentence2[i])>1 :
        	print('Frequency of', sentence2[i], 'is :', sentence.count(sentence2[i]))   
  
def main(): 
    sentence = input("Enter a sentence : ")
    wordCounter(sentence)                     
  
if __name__=="__main__": 
    main()            