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
        with open("analysis/success_rate_"+ algorithm + ".txt", "r") as results:
            for i in range(number_of_graphs):
                graph_name = results.readline()
                test_vals = list(map(int, results.readline()[1:-2].split(", ")))
                success_rate = sum(test_vals)/len(test_vals)
                with open("analysis/analysis_success_rate_"+algorithm+".txt", "a+") as analysis:
                    analysis.write("SUCCESS RATE FOR " +graph_name+ ":\n")
                    analysis.write("SUM:" + str(success_rate) + "\n")

if __name__ == "__main__":
    main()