from statistics import  mean
import matplotlib.pyplot as plt

def pad(l, content, width):
    l.extend([content] * (width - len(l)))
    return l

def main():
    avg_best_fitness_h = []
    avg_best_fitness_s= []
    avg_sum_fitness_s = []
    avg_sum_fitness_h = []
    with open("analysis/analysis_iter_hybrid.txt") as hibridni:
        generation_sum_fitness = []
        generation_best_fitness = []
        i = 0
        while i < 20:
            test_best = list(map(float, hibridni.readline()[1:-2].split(", ")))
            if i % 2 == 0:
                pad(test_best, 0, 1000)
                generation_best_fitness.append(test_best)
            else:
                pad(test_best, 0, 1000)
                generation_sum_fitness.append(test_best)
            i += 1

        avg_best_fitness_h = list(map(mean, zip(*generation_best_fitness)))
        avg_sum_fitness_h = list(map(mean, zip(*generation_sum_fitness)))

    with open("analysis/analysis_iter_simple.txt") as prosti:
        generation_sum_fitness = []
        generation_best_fitness = []
        i = 0
        while i < 16:
            test_best = list(map(float, prosti.readline()[1:-2].split(", ")))
            if i % 2 == 0:
                pad(test_best, 0, 1000)
                generation_best_fitness.append(test_best)
            else:
                pad(test_best, 0, 1000)
                generation_sum_fitness.append(test_best)
            i += 1

        avg_best_fitness_s = list(map(mean, zip(*generation_best_fitness)))
        avg_sum_fitness_s = list(map(mean, zip(*generation_sum_fitness)))

    plt.plot(avg_sum_fitness_s, label = "GA")
    plt.plot(avg_sum_fitness_h, label = "HGA")
    plt.ylabel("prosečna prilagođenost populacije")
    plt.xlabel("generacija")
    ax = plt.subplot(111)
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.show()


    plt.plot(avg_best_fitness_s, label = "GA")
    plt.plot(avg_best_fitness_h, label = "HGA")
    plt.ylabel("prosečna prilagođenost najbolje jedinke")
    plt.xlabel("generacija")
    ax = plt.subplot(111)
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.show()
    plt.show()

if __name__ == "__main__":
    main()