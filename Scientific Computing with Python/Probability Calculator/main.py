# Entrypoint file 
import prob_calculator

# The experiment function in prob_calculator performs a series of experiments where it draws a certain number of balls from the hat and checks if the drawn balls match a certain expected distribution of colors.
prob_calculator.random.seed(95)
hat = prob_calculator.Hat(blue=4, red=2, green=6) # Class represents a hat with a certain number of balls of different colors
probability = prob_calculator.experiment(
    hat=hat,
    expected_balls={"blue": 2, # Expected distribution of colors (2 blue balls and 1 red ball)
                    "red": 1},
    num_balls_drawn=4, # The number of balls to draw (4),
    num_experiments=3000) # The number of experiments to perform (3000)
print("Probability:", probability) # Prints the result of the function


