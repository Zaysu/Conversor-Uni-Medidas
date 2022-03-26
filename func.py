class Medidas():
    def __init__(self, quantidade, unidademed, milha, polegada, pe, centimetro, metro, quilometro):
        self.__quant = quantidade
        self.__unidademed = unidademed
        self.__milha = milha
        self.__polegada = polegada
        self.__pe = pe 
        self.__centimetro = centimetro
        self.__metro = metro
        self.__quilometro = quilometro
                        
    def milha(self):
        
        print(f"{self.__quant} Metro(s) = {self.__quant} Metro(s)")
        
        valor1 = self.__polegada * self.__quant
        print(f"{self.__quant} Milhas(s) = {valor1} Polegadas(s)")
            
        valor2 = self.__pe * self.__quant 
        print(f"{self.__quant} Milhas(s) = {valor2} Pés(s)")
            
        valor3 = self.__centimetro * self.__quant
        print(f"{self.__quant} Milhas(s) = {valor3} Centimetros(s)")
            
        valor4 = self.__metro * self.__quant
        print(f"{self.__quant} Milhas(s) = {valor4} Metros(s)")
            
        valor5 = self.__quilometro * self.__quant
        print(f"{self.__quant} Milhas(s) = {valor5} Quilometros(s)")
        
    def polegada(self):
        
        print(f"{self.__quant} Polegada(s) = {self.__quant} Polegada(s)")
        
        valor1 = self.__quant / self.__milha  
        print(f"{self.__quant} Polegadas(s) = {valor1} Milhas(s)")
            
        valor2 =  self.__quant / self.__pe 
        print(f"{self.__quant} Polegadas(s) = {valor2} Pé(s)")
            
        valor3 =  self.__quant * self.__centimetro
        print(f"{self.__quant} Polegadas(s) = {valor3} Centimetros(s)")
            
        valor4 =  self.__quant / self.__metro
        print(f"{self.__quant} Polegadas(s) = {valor4} Metros(s)")
            
        valor5 =  self.__quant / self.__quilometro 
        print(f"{self.__quant} Polegadas(s) = {valor5} Quilometros(s)")
        
    def pe(self):
        
        print(f"{self.__quant} Pe(s) = {self.__quant} Pe(s)")
        
        valor1 = self.__quant / self.__milha  
        print(f"{self.__quant} Pe(s) = {valor1} Milhas(s)")
            
        valor2 =  self.__quant * self.__polegada 
        print(f"{self.__quant} Pe(s) = {valor2} Polegada(s)")
      
        valor3 =  self.__quant * self.__centimetro
        print(f"{self.__quant} Pe(s) = {valor3} Centimetros(s)")
            
        valor4 =  self.__quant / self.__metro
        print(f"{self.__quant} Pe(s) = {valor4} Metros(s)")
            
        valor5 =  self.__quant / self.__quilometro 
        print(f"{self.__quant} Pe(s) = {valor5} Quilometros(s)")
    
    def centimetro(self):
        
        print(f"{self.__quant} Centimetros(s) = {self.__quant} Centimetros(s)")
        
        valor1 = self.__quant / self.__milha
        print(f"{self.__quant} Centimetros(s) = {valor1} Milhas(s)")
        
        valor2 = self.__quant / self.__polegada
        print(f"{self.__quant} Centimetros(s) = {valor2} Polegadas(s)")

        valor3 = self.__quant / self.__pe
        print (f"{self.__quant} Centimetros(s) = {valor3} Pé(s)")

        valor4 = self.__quant / self.__metro
        print(f"{self.__quant} Centimetros(s) = {valor4} Metros(s)")
        
        valor5 = self.__quant / self.__quilometro
        print(f"{self.__quant} Centimetros(s) = {valor5} Quilometros(s)")

    def metro(self):
        
        print(f"{self.__quant} Metros(s) = {self.__quant} Metros(s)")
        
        valor1 = self.__quant / self.__milha
        print (f"{self.__quant} Metros(s) = {valor1} Milhas(s)")
        
        valor2 = self.__quant * self.__polegada
        print (f"{self.__quant} Metros(s) = {valor2} Polegadas(s)")
        
        valor3 = self.__quant * self.__pe
        print (f"{self.__quant} Metros(s) = {valor3} Pé(s)")
        
        valor4 = self.__quant / self.__centimetro
        print (f"{self.__quant} Metros(s) = {valor4} Centimetros(s)")
        
        valor5 = self.__quant / self.__quilometro
        print(f"{self.__quant} Metros(s) = {valor5} Quilometros(s)")
    
    def quilometro(self):
       print(f"{self.__quant} Quilometros(s) = {self.__quant} Quilometros(s)")
        
       valor1 = self.__quant / self.__milha
       print(f"{self.__quant} Quilometros(s) = {valor1} Milhas(s)")
       
       valor2 = self.__quant * self.__polegada
       print (f"{self.__quant} Quilometros(s) = {valor2} Polegadas(s)")
       
       valor3 = self.__quant * self.__pe
       print (f"{self.__quant} Quilometros(s) = {valor3} Pé(s)")
       
       valor4 = self.__quant * self.__centimetro
       print (f"{self.__quant} Quilometros(s) = {valor4} Centimetros(s)")
       
       valor5 = self.__quant * self.__metro
       print (f"{self.__quant} Quilometros(s) = {valor5} Metros(s)")
       
  ##################################################aaaaaaaaaaaaaa#############################################################  
    def quant(self):
        self.__quant
        print(f"{self.__quant}")
    
    def unimedida(self):
        self.__unidademed
        print(f"{self.__unidademed}")