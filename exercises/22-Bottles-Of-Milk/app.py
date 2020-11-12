def number_of_bottles():
    for i in reversed(range(100)):
        if i==1:
            bottles=str(i)
            print("{} bottle of milk on the wall, {} bottle of milk.\nTake one down and pass it around, no more bottles of milk on the wall.".format(bottles,bottles))       
        elif i==0:            
            newBottles=str(i+99)
            print("No more bottles of milk on the wall, no more bottles of milk.\nGo to the store and buy some more, {} bottles of milk on the wall.".format(newBottles))
        elif i==2:
            bottles=str(i)
            newBottles=str(i-1)
            print("{} bottles of milk on the wall, {} bottles of milk.\nTake one down and pass it around, {} bottle of milk on the wall.".format(bottles,bottles,newBottles))
        else:
            bottles=str(i)
            newBottles=str(i-1)
            print("{} bottles of milk on the wall, {} bottles of milk.\nTake one down and pass it around, {} bottles of milk on the wall.".format(bottles,bottles,newBottles))

            
number_of_bottles()