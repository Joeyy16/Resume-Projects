import copy
import random


"""
This is the __init__ method of the Hat class in the prob_calculator module. This method is called when a new Hat object is created, and it initializes the contents attribute of the object. The contents attribute is a list of strings, where each string represents a color. The colors and the number of balls of each color in the hat are passed as keyword arguments to the method.

Then the contents attribute of the hat object will be a list of 12 strings, where 4 of the strings are "blue", 2 of the strings are "red", and 6 of the strings are "green".
"""
class Hat:
    def __init__(self, **kwargs):
        self.contents = [k for k, v in kwargs.items() for _ in range(v)]

    
    # The draw method of the Hat class is used to draw n balls from the hat. The number of balls drawn, n, is limited by the total number of balls remaining in the hat. The method uses a list comprehension to draw n balls from the hat by removing a randomly chosen ball from the contents list of the hat and appending it to the list of balls being returned. The random.randrange(len(self.contents)) function is used to generate a random index for the ball to be removed from the contents list. This process is repeated n times, and the resulting list of balls is returned.
    def draw(self, n):
        n = min(n, len(self.contents))
        return [self.contents.pop(random.randrange(len(self.contents))) for _ in range(n)]

    """
    This code is performing a number of experiments on a hat to calculate the probability that a specific set of balls will be drawn from the hat. The hat is initialized with a certain number of balls of each color, and the experiment function is called with this hat and a dictionary specifying the expected number of balls of each color that should be drawn in each experiment. The experiment function also takes two integers, num_balls_drawn and num_experiments, which specify the number of balls to be drawn in each experiment and the total number of experiments to be performed, respectively.

    In each experiment, a copy of the hat is made using the copy module's deepcopy function. This ensures that the original hat is not modified during the experiments. The function then calls the draw method on the copied hat to draw num_balls_drawn balls. It counts the number of colors that meet or exceed the expected number of balls in the dictionary of expected balls. If this count is equal to the length of the dictionary, it increments the counter m by 1. After all the experiments are performed, the probability is calculated by dividing m by num_experiments.
    """

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    for _ in range(num_experiments):
        another_hat = copy.deepcopy(hat)
        balls_drawn = another_hat.draw(num_balls_drawn)
        balls_req = sum([1 for k, v in expected_balls.items() if balls_drawn.count(k) >= v])
        m += 1 if balls_req == len(expected_balls) else 0

        """
        The experiment function simulates a probability experiment where a number of balls are drawn from a hat. It takes in four arguments:

        hat: an instance of the Hat class representing the hat that the balls are drawn from
        expected_balls: a dictionary mapping colors of balls to the number of balls of that color expected to be drawn
        num_balls_drawn: an integer representing the number of balls that will be drawn from the hat
        num_experiments: an integer representing the number of times the experiment will be run
        The function runs the experiment num_experiments times by drawing num_balls_drawn balls from a copy of the hat instance each time. For each experiment, it counts the number of ball colors in expected_balls that are present in the balls drawn. If this number is equal to the number of colors in expected_balls, it increments a counter m. At the end, it returns the probability of the expected ball colors being drawn, calculated as m divided by num_experiments.
        """
    return m / num_experiments
