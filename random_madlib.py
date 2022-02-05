# SImple madlib game in python 
# made by enal

from sample_madlibs import hewan, komputer_ajaib, zeus_olympia, zombie
import random

if __name__ == "__main__":
    m = random.choice([hewan, komputer_ajaib, zeus_olympia, zombie])
    m.madlib()