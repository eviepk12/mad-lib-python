from sample_madlibs import hewan, komputer_ajaib, zeus_olympia
import random

if __name__ == "__main__":
    m = random.choice([hewan, komputer_ajaib, zeus_olympia])
    m.madlib()