import math

def calculate_abnormal_threshold(adv):
    k = 2.26 + 0.34 * math.log(adv)
    per_minute_volume = adv / 1440
    abnormal_threshold = k * per_minute_volume
    return abnormal_threshold

# Example usage:
adv_crypto = 17000000  # ADV for Bitcoin
threshold = calculate_abnormal_threshold(adv_crypto)
print(f"Abnormal threshold for crypto: {threshold:.2f} units/min")
