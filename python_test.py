x = [100,110,120,130,140,150]
new_list = [y*5 for y in x]
print(new_list)

def divisible_by_three(n):
      if n%3==0:
           print(n)
      else:
        print("It's not divisible by three")
        divisible_by_seven(5)

num_list= [[1, 2], [3, 4], [5,6]]
x = [liste for sublist in num_list for liste in sublist]
print('Transformed list', x)

def smallest():
    numbers=[9,3,6,8,2,4,1,5,7]
    numbers.sort()
    print(*numbers[:1])
smallest()

def list_numbers():

 letter= ['a','b','a','e','d','b','c','e','f','g','h']
 new_list= []
# for i in letter:
      #   if i is not letter:
      #     letter.append(i)
      #  letter = new_list

# print(new_list)
x=range(100,200)
def divisible_by_seven():
    for i in x:
        if i%7==0:
          print(i)
    else:
       print("Is not divisible by 7")
divisible_by_seven()



def greetings(name,year):
    name=name
    year=year
    return ("Hello {name} you were born in {year} ")

print(greetings("Jeannine",20))
print(greetings("Eunice",20))
print(greetings("Mutoni",23))












