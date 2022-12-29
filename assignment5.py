"""
   CISC-121 2022F

   Name:   <Elill Mathivannan>
   Student Number: <20342676>
   Email:  <elillmath2004@gmail.com>
   Date: 2022-12-05

   I confirm that this assignment solution is my own work and conforms to
   Queen's standards of Academic Integrity
"""
#import necessary functions
from er_class import Emergency_Room
import random

#create new Emergency_Room class (priority queue)
er_room = Emergency_Room()
#list of 10 names
names = ["Sam","Tyler","James","Lisa","Jerry","Chris","Jessica","Rebecca","Terry","John"]
#variable for sequence number
seq=1
for i in names:
    #add patients to the emergency room queue (name, priority, time)
    er_room.arrive(str(seq)+i, random.randint(0,10), str(random.randint(seq-1,seq-1))
                   +':'+str(random.randint(0,5))+str(random.randint(0,9)))
    seq+=1

#print patients in emergency room
for i in er_room:
    print(f"{i[0]} arrived at {i[2]}, with a priority level of {i[1]}")

#announce next patient to be scheduled
print(f"\nPatient to be announced:\nName: {er_room.announce()[0]}\nArrival time: {er_room.announce()[2]}\nPriority level: {er_room.announce()[1]}")

#schedule patient with highest priority
appointment = er_room.schedule()
print(f"\nPatient: {appointment[0]}, who arrived at: {appointment[2]}, with a priority of: {appointment[1]}, has been scheduled")



