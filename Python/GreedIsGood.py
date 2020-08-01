# https://www.codewars.com/kata/5270d0d18625160ada0000e4/train/python
#  Three 1's => 1000 points
#  Three 6's =>  600 points
#  Three 5's =>  500 points
#  Three 4's =>  400 points
#  Three 3's =>  300 points
#  Three 2's =>  200 points
#  One   1   =>  100 points
#  One   5   =>   50 point

def score(dice):
    total = dice.count(1) // 3 * 1000 + dice.count(1) % 3 * 100
    total += dice.count(6) // 3 * 600
    total += dice.count(5) // 3 * 500 + dice.count(5) % 3 * 50
    total += dice.count(4) // 3 * 400
    total += dice.count(3) // 3 * 300
    total += dice.count(2) // 3 * 200
    return total


print(score([2, 3, 4, 6, 2]))  # 0
print(score([4, 4, 4, 3, 3]))  # 400
print(score([2, 4, 4, 5, 4]))  # 450
