#include <vector>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <ctime>

class Vertex {
public:

	Vertex(){
	};

	Vertex(int i, int k)
	:value(i,k)
	{
	};

	~Vertex(){};

	int color() const {
		return value.second;
	}

	int id() const {
		return value.first;
	}

	std::pair<int, int> value;
};


class Graph {
public:

	Graph(){};

	Graph(int n, int k){
		vertices.resize(n);
		colors.resize(k);
	};

	~Graph(){

	};

	Vertex at(int i) const {
		return vertices.at(i);
	};

	int size() const {
		return vertices.size();
	}

	void group_by_color(){
		int n = vertices.size();
		for(int i = 0; i < n; i++){
			colors.at(vertices.at(i).color()).push_back(vertices.at(i));		
		}
	}

	void fit(const std::vector< std::vector<bool> >& adj_matrix){
		fitness = 0;
		int n = adj_matrix.size();
		for (int i = 0; i < n; ++i) {
			for (int j = i; j < n; ++j) {
				if(adj_matrix.at(i).at(j) && (vertices.at(i).color() == vertices.at(j).color())){
						++fitness;
				}
			}
		}
	}


	std::vector<Vertex> vertices;
	std::vector<std::vector<Vertex> > colors;
	int fitness;
};



// TODO: napisati odgovarajuci nacin selekcije
template <typename T>
std::pair<T,T> selection(const std::vector<T>& population){
	T first = population.at(0);
	T second = population.at(1);
	return {first, second};
}

//TODO: crossover kako pise u pdfu
template <typename T>
T crossover( const std::pair<T,T>& parents, int k) {
	int n = parents.first.size();
	T child(n, k);
	for(int i = 0; i < n; i++){
		child.vertices.at(i) = std::rand() % 2 ? parents.first.at(i) : parents.second.at(i); 
	}
	return child;
}


int main(int argc, char** argv)
{
	if ( argc != 4){
		std::cout << "input error: ./name num_of_vertices num_of_colors size_of_pop";
		std::exit(1);
	}

    std::srand(std::time(NULL));

    int n = std::atoi(argv[1]);
    int k = std::atoi(argv[2]);
    int P = std::atoi(argv[3]);
    std::vector<Graph> population(P);
	std::vector<std::vector<bool> > adj_matrix(n);

	for(int i = 0; i < n; i++){
        adj_matrix.at(i).resize(n);

    }

    for(int i = 0; i < n; i++) {
    	for(int j = i; j < n ; j++){
    		if( i != j) {
   				adj_matrix.at(i).at(j) = std::rand() % 2 == 0 ? 0 : 1; 
   				adj_matrix.at(j).at(i) = adj_matrix.at(i).at(j); 
    		}
    		else {
    			adj_matrix.at(i).at(j) = 0;
    		}
    	}
    }

    for(int i = 0; i < n; i++) {
    	for(int j = 0; j < n ; j++){
    		std::cout << adj_matrix.at(i).at(j) << " ";
    	}
    	std::cout << std::endl;
    }

	for(int p = 0; p < P; p++) {

		Graph graph(n, k);
		for(int i = 0; i < n; i++){
			Vertex v(i, std::rand() % k);
			graph.vertices.at(i) = v;
		}
		graph.group_by_color();
		for(int i = 0; i < n; i++){
			std::cout << graph.at(i).value.first << " color:" << graph.at(i).value.second << std::endl;
		}
		std::cout << std::endl;

		population.at(p) = graph;
	}

	// selekcija
	std::pair<Graph, Graph> parents = selection(population);
	// crossover
	Graph child = crossover(parents, k);
	for(int i = 0; i < n; i++){
		std::cout << child.at(i).value.first << " color:" << child.at(i).value.second << std::endl;
	}

	child.group_by_color();
	child.fit(adj_matrix);
	for(int i = 0; i < k; i++){
		int m = child.colors.at(i).size();
		std::cout << "color: " << i << " size: " << m << std::endl;
		for (int j = 0; j < m; ++j)
		{
			std::cout << child.colors.at(i).at(j).id() << ", ";
		}
		std::cout << std::endl;
	}

	std::cout << child.fitness << std::endl;
    return 0;
}
