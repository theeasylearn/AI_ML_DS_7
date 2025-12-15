# nested list
delhi_aqi = [
    [145, 210, 189, 320, 275, 410, 380],  # Week 1
    [260, 305, 330, 285, 410, 395, 370],  # Week 2
    [420, 385, 440, 310, 295, 260, 355],  # Week 3
    [280, 360, 340, 455, 380, 410, 290],   # Week 4
    [300,400],   # Week 5
]
# findout average aqi
total = 0
count = 0
# print(delhi_aqi[0][0])
for week in delhi_aqi:
    # print(week)
    for day in week:
        total = total + day
        count = count + 1
print(f"total = {total} average aql = ",(total/count))

#generate week wise total & average
#generate average aqi of sunday