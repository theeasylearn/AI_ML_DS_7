#example of for loop on dictionary 
#calculate total run by team members and average 
team = {"Rohit":43,"Gill":27,"Kohli":54,"SKY":32,"Pant":18,"Hardik":29,"Jadeja":14,"Axar":21,"Bumrah":2,"Shami":6,"Arshdeep":3}
total = 0
for player in team:
    # print(player,end= ' ')
    total = total + team[player]

print(f"total = {total} average = ",total/11)

# findout player name and his maximum score 
# findout player name and his minimum score
 