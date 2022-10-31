import numpy as np
import random

def generate_output_file(n=300):
    operators = ["+", "-", "*", "/"]
    num_carac = [i for i in range(-1000, 1000, 1)]
    error_carac = ["+", "-", "*", "/", "#", ":", "~", "&", "$", "^"]
    carac = num_carac + error_carac                     
    random.shuffle(carac)

    with open("input_file.txt", "w") as f:
        for i in range(n):
            f.write(
                f"{random.choice(carac)} " \
                f"{random.choice(operators)} " \
                f"{random.choice(carac)}\n")

if __name__ == "__main__":
    generate_output_file(1000)