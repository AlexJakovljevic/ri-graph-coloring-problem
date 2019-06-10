def main():
    with open("/home/aca/Desktop/RI_Projekat/solution.txt", "r") as result_output:
        chromosome = []
        result = result_output.read().split(", ")
        for color in result:
            chromosome.append(int(color))

        with open("/home/aca/Desktop/RI_Projekat/huck.col", "r") as graph_file:
            first_line = graph_file.readline().split(" ")
            num_vertices = int(first_line[0])
            adjacency_list = {i: [] for i in range(num_vertices)}

            for line in graph_file:
                edge = line.split(" ")
                adjacency_list[int(edge[0]) - 1].append(int(edge[1]) - 1)

            for i in range(num_vertices):
                for e in adjacency_list[i]:
                    if chromosome[i] == chromosome[e]:
                        print("NOT A VALID GRAPH COLORING")
                        exit(1)

    print("VALID GRAPH COLORING")


if __name__ == "__main__":
    main()
