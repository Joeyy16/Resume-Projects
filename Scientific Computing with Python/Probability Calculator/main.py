"""
The code is using a module called prob_calculator that contains a class Hat and a function experiment. The Hat class represents a hat with a certain number of balls of different colors. The experiment function performs a series of experiments where it draws a certain number of balls from the hat and checks if the drawn balls match a certain expected distribution of colors.

In this specific example, a hat is created with 4 blue balls, 2 red balls, and 6 green balls. Then, the experiment function is called with the hat, the expected distribution of colors (2 blue balls and 1 red ball), the number of balls to draw (4), and the number of experiments to perform (3000). The function returns the probability that the expected distribution of colors will be obtained when drawing 4 balls from the hat. The probability is calculated by performing 3000 experiments, counting the number of times that the expected distribution is obtained, and dividing that number by 3000.
"""

# This entrypoint file to be used in development. Start by reading README.md
import prob_calculator


prob_calculator.random.seed(95)
hat = prob_calculator.Hat(blue=4, red=2, green=6)
probability = prob_calculator.experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=3000)
print("Probability:", probability)


