import random

print("Santiago Sala")
print("Week 4 Exercise 4: Throwing the dice")
print("This program will count how many times are the dice results after throwing it 100 times")


dice_one = 0
dice_two = 0
dice_three = 0
dice_four = 0
dice_five = 0
dice_six = 0

dice_round = 0

while dice_round < 100:    
    dice_result = random.randint(1, 6)
    #print("Result is:" + str(dice_result))

    match dice_result:
        case 1:
            dice_one += 1
        case 2:
            dice_two += 1
        case 3:
            dice_three += 1
        case 4:
            dice_four += 1
        case 5:
            dice_five += 1
        case 6:
            dice_six += 1
    
    #print("Dice round is: " + str(dice_round))
    dice_round += 1
    
print("The dice results are: number 1 --> " + str(dice_one) +
      " times, dice number 2 --> " + str(dice_two) +
      " times, dice number 3 --> " + str(dice_three) +
      " times, dice number 4 --> " + str(dice_four) +
      " times, dice number 5 --> " + str(dice_five) +
      " times and dice number 6 --> " + str(dice_six) + " times.")

print("Thank you for playing")
