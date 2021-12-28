import time

#Timer Variable
##a=0

#Info Screen
print("<===Type 1 to Power on and 0 to Power off===>")
print("<---Type 1 to Commence Washing--->")





#Creating a Class for Washing Machine 
class w_machine:
    def __init__(self,state,process,door_state):
     self.state = 0
     self.process = 0
     self.door_state = 0




#Making an object from w_machine
washing_machine=w_machine






#Power State Function
def power_on(x):
    if x == 1:
        print("Turned on")
        washing_machine.state=1
        return(1)
    elif x == 0:
        print("Turned off")
        washing_machine.state=0
        return(0)


#Washing Function
def washing(x):
    a=0
    if x == 1 and washing_machine.state == 1 :
          while a<=100:
                 print("Washing Clothes"+ str(a)+"%")
                 washing_machine.door_state=int(input("Door State :"))
                 if washing_machine.door_state==1:
                         print("Door Has been Opened")
                         washing_machine.process=0
                         break
                 washing_machine.process=1
                 a=a+1
                 time.sleep(0.05)
              
    print("Washing Finished")   
    washing_machine.process=0 
    #print("Washing machine is Turned off")



        




#User Input to Turn on the Machine
switch_input=input("Your Input for Power :")

power_on(int(switch_input))


washing_machine.door_state=0

#User Input to Commence Washing
washing_input=input("Your Input for Washing :")
washing(int(washing_input))








#while a<100:
 #   print("Running "+str(a)+ "%" )
  #  a=a+1
   # time.sleep(0.01)