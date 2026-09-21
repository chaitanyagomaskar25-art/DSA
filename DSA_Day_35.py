# Q1 — Digital Speedometer

# A car records its speed every minute:

# speeds = [45, 52, 48, 61, 55, 72, 49]

# Find:

# 1.The highest speed
# 2.The lowest speed
# 3.How many times the car exceeded 60 km/h
# 4.The average speed

# Expected output:

# Highest Speed: 72
# Lowest Speed: 45
# Above 60: 2
# Average Speed: 54.57

# a = list(map(int, input().split()))

# h = 0
# l = a[0]
# gs = 0
# s = 0

# for i in a:
#     s+=i
#     if i > h:
#         h = i
#     if i < l:
#         l = i
#     if i >= 60:
#         gs+=1

# print(f"Highest Speed : {h}\nLowest Speed : {l}\nAbove 60 : {gs}\nAverage Speed : {round(s/len(a), 2)}")

# ===========================================

# Q2 — Secret Word Scanner

# A security system receives a message:

# message = "meet me at the old bridge at midnight"

# Check the message and find:

# 1.How many words contain the letter e
# 2.The longest word
# 3.How many words have more than 4 characters
# 4.Print the words that contain two or more e's

# Expected output:

# Words containing e: 4
# Longest word: midnight
# Words longer than 4: 2
# Words with 2+ e: meet


# a = input()
# e = 0
# l = ""
# moreThanFour = 0
# withTwoE = []
# words = a.split()

# for i in range(len(words)):
#     if "e" in words[i]:
#         e+=1
#     if words[i].count("e") >=2:
#         withTwoE.append(words[i])
#     if len(words[i]) > len(l):
#         l = words[i]
#     if len(words[i]) > 4:
#         moreThanFour+=1
        
# print(f"Words containing e : {e}\nLongest word : {l}\nWords longer than 4 : {moreThanFour}\nWord with 2+ e : {" ".join(withTwoE)}")

# =================================

# Q3 — Robot Battery Journey

# A robot starts with 100% battery and travels through different locations. Each number represents the battery consumed at each location:

# battery_usage = [12, 8, 15, 20, 7, 18, 10]

# The robot follows these rules:

# 1.Start with 100% battery
# 2.Subtract each usage value one by one.
# 3.If the battery becomes 20% or lower, print "LOW BATTERY".
# 4.Find the battery percentage after the complete journey.
# 5.Find which step/location caused the largest battery consumption.
# 6.If the battery reaches 0 or below, stop the journey immediately.

# Expected output:

# LOW BATTERY
# Final Battery: 10%
# Highest Consumption: 20%
# At Location: 4

# a = list(map(int, input().split()))

# isLower = False
# fb = 100
# hc = 0
# location = 0
# for i in range(len(a)):
#     fb-=a[i]
#     if fb <= 20:
#         isLower = True
#     if a[i] > hc:
#         hc = a[i]
#         location = i
    
# if isLower:
#     print(f"LOWER BATTERY")

# print(f"Final battery : {fb}%\nHighest Consumption : {hc}%\nAt Location : {location+1}")