# Q1 — Cinema Seat Decoder

# A cinema stores seat numbers like this:

# seats = ["A12", "B07", "C15", "A03", "D09", "B14"]

# For each seat:

# 1. Print the row letter and seat number separately.
# 2. Count how many seats belong to row A.
# 3. Calculate the total of all seat numbers.

# Expected output:

# A -> 12
# B -> 7
# C -> 15
# A -> 3
# D -> 9
# B -> 14

# Row A Seats: 2
# Total Seat Numbers: 60


# seats = list(map(str, input("Enter a cinema seats: ").split()))

# ca = 0
# s = 0
# for i in range(len(seats)):
#     if seats[i][0] == "A":
#         ca+=1
#     s+= int(seats[i][1:])
#     print(seats[i][0], "->", seats[i][1:])

# print(f"Row A seats : {ca}\nTotal Seat Numbers : {s}")


# ==============================================


# Q2 — Strange Password Checker

# A system receives these passwords:

# passwords = ["cat123", "HELLO", "robot42", "sun", "Python99"]

# For each password:

# 1. Print "Strong" if it has at least 6 characters and contains at least one digit.
# 2. Otherwise, print "Weak".
# 3. At the end, count how many passwords are strong.

# Expected output:

# cat123 -> Strong
# HELLO -> Weak
# robot42 -> Strong
# sun -> Weak
# Python99 -> Strong

# Strong Passwords: 3

# password = list(map(str, input("Enter a password: ").split()))
# s = 0
# for i in range(len(password)):
#     has_digit = False
#     for char in password[i]:
#         if char in "1234567890":
#             has_digit = True
            
#     if has_digit and len(password[i]) >= 6:
#         s+=1
#         print(f"{password[i]} -> Strong")
#     else:
#         print(f"{password[i]} -> Weak")

# print(f"Strong Password : {s}")


# =================================================

# Q3 — Delivery Route Analyzer

# A delivery robot travels through several checkpoints. The distance between each checkpoint is stored in a list:

# distances = [5, 8, 3, 12, 7, 10, 4]

# The robot starts with 100 energy points.

# Rules:

# 1. Every 1 km consumes 2 energy points.
# 2. Calculate the energy used for each checkpoint.
# 3. Show the remaining energy after every checkpoint.
# 4. Find the checkpoint with the longest distance.
# 5. Calculate the total distance traveled.
# 6. If energy becomes less than or equal to 20, print "Energy Critical".

# Expected output:

# Checkpoint 1: 90
# Checkpoint 2: 74
# Checkpoint 3: 68
# Checkpoint 4: 44
# Checkpoint 5: 30
# Checkpoint 6: 10
# Energy Critical
# Checkpoint 7: 2
# Energy Critical

# Total Distance: 49 km
# Longest Distance: 12 km
# Longest Distance At Checkpoint: 4
# Final Energy: 2


# distances = list(map(int, input("Enter a distances: ").split()))
# t =0
# l = 0
# f = 100

# for i in range(len(distances)):
#     f-= (distances[i]*2)
#     print(f"Checkpoint {i+1} : {f}")
#     if f <=20:
#         print("Energy Critical")
#     t+=distances[i]
#     if distances[i] > distances[l]:
#         l = i 
    
# print(f"Total Distance : {t}km\nLongest Distance : {distances[l]}km\nLongest Distance At Checkpoint : {l+1}\nFinal Energy : {f}")