import sys
import re
import warnings
warnings.filterwarnings("ignore")

pattern = r"((?:[+\-*\/#:~&$^])?[0-9]*) ([+\-*\/]) ((?:[+\-*\/#:~&$^])?[0-9]*)"

with open("output_file.txt", "a") as f:
    for line in sys.stdin:
        line = line.strip()
        try:
            if re.match(pattern, line):
                f.write(f"{line} = {eval(line)}\n")
            else:
                f.write(f"{line} = Wrong format !\n")
        except:
            f.write(f"{line} = Error !\n")
    else:
        print("End !")