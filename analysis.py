import statistics, os

def main():
    algorithm_name = ["simple", "hybrid"]
    graph_list = []
    rootDir = './graphs'
    for dirName, subdirList, fileList in os.walk(rootDir):
         print('Found directory: %s' % dirName)
         for fname in fileList:
             graph_list.append(fname)
    number_of_graphs = len(graph_list)
    for algorithm in algorithm_name:
        with open("results/results_"+ algorithm + ".txt", "r") as results:
            for i in range(number_of_graphs):
                graph_name = results.readline()
                test_vals = list(map(float, results.readline()[1:-2].split(", ")))
                test_iter = list(map(int, results.readline()[1:-2].split(", ")))
                with open("analysis/analysis_"+algorithm+".txt", "a+") as analysis:
                    analysis.write("STATISTICS FOR " +graph_name+ ":")
                    analysis.write("TIME:\n")
                    analysis.write("SUM:" + str(sum(test_vals)) + "\n")
                    analysis.write("MEAN:" + str(statistics.mean(test_vals)) + "\n")
                    analysis.write("MEDIAN:" + str(statistics.median(test_vals)) + "\n")
                    analysis.write("BEST:" + str(min(test_vals)) + "\n")
                    analysis.write("WORST:" + str(max(test_vals)) + "\n")
                    analysis.write("ITERS:\n")
                    analysis.write("SUM:" + str(sum(test_iter)) + "\n")
                    analysis.write("MEAN:" + str(statistics.mean(test_iter)) + "\n")
                    analysis.write("MEDIAN:" + str(statistics.median(test_iter)) + "\n")
                    analysis.write("BEST:" + str(min(test_iter)) + "\n")
                    analysis.write("WORST:" + str(max(test_iter)) + "\n")


if __name__ == "__main__":
    main()