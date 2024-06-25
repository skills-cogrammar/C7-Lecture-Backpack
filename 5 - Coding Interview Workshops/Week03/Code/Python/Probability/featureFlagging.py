import numpy as np

# Define a simple feature flagging function using probabilities
def feature_flag(user_id, feature_probability):
    # Generate a random number between 0 and 1
    # This simulates the random nature of whether a user sees a feature.
    random_threshold = np.random.rand()
    
    # If the random number is less than the feature probability, enable the feature
    # This is a basic probability check.
    if random_threshold < feature_probability:
        return True  # Feature is enabled for this user
    else:
        return False  # Feature is disabled for this user

# Probability of enabling a new feature (50% chance)
feature_probability = 0.5

# Simulate feature flagging for a set of users
user_ids = [101, 102, 103, 104, 105]
for user_id in user_ids:
    # Check if the feature should be enabled for the user
    feature_enabled = feature_flag(user_id, feature_probability)
    print(f"Feature enabled for user {user_id}: {feature_enabled}")
