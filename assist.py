from operator import truediv
def generate_tree(num):
    q = [num]
    tree = [[num]]

    done = False

    if num == 9 or num == 10:
        done = True

    while not done:
        n = len(q)
        level = []
        while n > 0:
            e = q.pop()
            q.insert(0, 8 - e)
            q.insert(0, 10 - e)
            level.append(8 - e)
            level.append(10 - e)
            if(8 - e >= 9 or 10 - e >= 9): done = True
            n -= 1
        tree.append(level)

    return tree

def wait_to_advance():
    input("Press enter to continue.....")


my_name = input("Enter your name: ")
other_name = input("Enter other player's name: ")
first = True if input("Are you going first? (y/n): ").lower() == 'y' else False
num = int(input("Enter your number: "))

tree = generate_tree(num)
options = [8-num, 10-num]

round = 0

complete = False
sum = None

if num == 9 or num == 10:
    sum = 10
print()
print("===============================")
print("GAME START")
print("===============================")


if not first:
    passes = True if input(other_name + " goes. Did they pass or guess? (p/g): ").lower() == 'p' else False
    if not passes:
        complete = True

while not complete:
    if round % 2 == 1:
        passes = True if input(other_name + " goes. Did they pass or guess? (p/g): ").lower() == 'p' else False
        if not passes:
            complete = True
            sum = None # sometimes this is "wrong" if the background calc still happened
            break

    if round % 2 == 0:
        if sum is not None:
            print("Your turn: GUESS -> THE SUM IS " + str(sum))
            complete = True
            wait_to_advance()
            break
        else:
            print("Your turn: PASS")
            wait_to_advance()
            print()

    if sum is None:
        index = -1
        if(9 in tree[round]):
            index = tree[round].index(9)
        elif(10 in tree[round]):
            index = tree[round].index(10)

    if index != -1 and sum is None: # tree ended!
        if index < len(tree[round]) / 2: 
            sum = 10
        else:
            sum = 8
    
    round += 1

print("===============================")
print("GAME COMPLETE")
print("===============================")

if sum is not None:
    print("The numbers summed to: " + str(sum))
    print("Your number: " + str(num))
    print(other_name + "'s number: " + str(sum - num))
else:
    print("Other player guessed (hopefully correctly!)")



