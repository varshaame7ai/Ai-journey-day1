import random

secret_number = random.randint(1, 10)
guess = 0
tries = 0

print("🎮 Number Guessing Game 🎮")
print("Maine 1 se 10 ke beech ek number socha hai")

while guess != secret_number:
    guess = int(input("Apna guess daal: "))
    tries = tries + 1
    
    if guess < secret_number:
        print("Thoda bada socho ⬆️")
    elif guess > secret_number:
        print("Thoda chhota socho ⬇️")
    else:
        print(f"🎉 Jeet gayi Varsha! Number {secret_number} tha")
        print(f"Tune {tries} try mein guess kar liya")

print("Game khatam. Phir khelna ho to program dobara run kar")
