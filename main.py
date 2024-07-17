import logic
from decouple import config


attempts = int(config("ATTEMPTS"))
amount_left = int(config("STARTING_CAPITAL"))
bet = int(input("How much do you want to bet "))

logic.play(attempts, amount_left, bet)
