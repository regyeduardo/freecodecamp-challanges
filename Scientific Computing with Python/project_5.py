import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kargs):
        contents = []
        for item in kargs.keys():
            for times in range(kargs[item]):
                contents.append(item)
        self.contents = contents
    
    def draw(self, balls):
        if balls > len(self.contents):
            rest = self.contents
            # self.contents.clear()
            return rest

        choices = random.sample(self.contents, k=balls)
        for choice in choices:
            self.contents.remove(choice)
        return choices

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    contador = 0
    for experiment in range(num_experiments):
        eb = copy.deepcopy(expected_balls)
        hat_copy = copy.deepcopy(hat)
        colors = hat_copy.draw(num_balls_drawn)

        for color in colors:
            if color in eb:
                eb[color] -= 1
        

        # if(all(value <= 0 for value in eb.values())):
        #     contador += 1

        zero = [value <= 0 for value in eb.values()]
        if zero[0]:
            contador += 1

    return contador / num_experiments

# hat1 = Hat(yellow=3, blue=2, green=6)
# hat1.draw(2)

hat = Hat(blue=3,red=2,green=6)
probability = experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)
print(probability)