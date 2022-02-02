from sample_madlibs import hewan, komputer_ajaib
import random

if __name__ == "__main__":
    m = random.choice([hewan, komputer_ajaib])
    m.madlib()