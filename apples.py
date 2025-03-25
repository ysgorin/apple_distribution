# apples.py

# Import random module to generate
# random apple weights
import random

# Define a class representing an apple
class Apple:

    # Class variables to track the total number
    # of apples and their total weight
    total_apples = 0
    total_weight = 0

    def __init__(self, weight):
        # Initialize an apple with a given weight
        # and update class totals.
        self.weight = weight
        Apple.total_apples += 1
        Apple.total_weight += self.weight

# Display order details
print('A shop owner has asked for 1000 apples, \
but the total weight cannot exceed 300 units.')

print('Fulfilling order...')

# Add apples until apple or
# weight limit is reached
while Apple.total_apples < 1000:
    # Generate a random weight for the apple
    apple_weight = random.uniform(0.2, 0.5)

    # Check if adding new apple will exceed
    # weight limit and stop loop
    if Apple.total_weight + apple_weight > 300:
        break

    # Create a new apple
    apple = Apple(apple_weight)

# Print the final count and total weight of
# apples packaged.
print(f'Number of Apples Packaged: \
{Apple.total_apples}\nTotal Weight: \
{Apple.total_weight:.2f}')