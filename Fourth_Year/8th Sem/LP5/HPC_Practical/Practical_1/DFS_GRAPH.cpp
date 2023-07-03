#include <iostream>
#include <vector>
#include <stack>
#include <omp.h>

using namespace std;

class Graph {
private:
    int num_vertices;
    vector<vector<int>> adjacency_list;

public:
    Graph(int n) : num_vertices(n), adjacency_list(n) {}

    void add_edge(int u, int v) {
        adjacency_list[u].push_back(v);
        adjacency_list[v].push_back(u);
    }

    vector<int> get_neighbors(int v) const {
        return adjacency_list[v];
    }

    int get_num_vertices() const {
        return num_vertices;
    }
};

bool dfs(const Graph& graph, int start_node, int target_val) {
    stack<int> s;
    s.push(start_node);
    vector<bool> visited(graph.get_num_vertices(), false);
    visited[start_node] = true;
    bool found = false;

    while (!s.empty()) {
        vector<int> visited_nodes; // to store the order of visited nodes in each iteration
        #pragma omp parallel shared(found) // Begin parallel section
        {
            vector<int> local_stack; // to store the nodes in the local stack
            #pragma omp single // only one thread will execute this block
            {
                local_stack.push_back(s.top());
                s.pop();
            }
            while (!local_stack.empty()) {
                int node = local_stack.back();
                local_stack.pop_back();
                visited_nodes.push_back(node); // add the visited node to visited_nodes vector

                if (node == target_val) {
                    #pragma omp critical
                    {
                        found = true; // Node found!
                    }
                }

                vector<int> neighbors = graph.get_neighbors(node);
                for (int i = 0; i < neighbors.size(); i++) {
                    int neighbor = neighbors[i];
                    if (!visited[neighbor]) {
                        #pragma omp critical
                        {
                            visited[neighbor] = true;
                            local_stack.push_back(neighbor);
                        }
                    }
                }
            }
        }
        // Print the order of visited nodes in this iteration
        cout << "Visited nodes: ";
        for (int i = 0; i < visited_nodes.size(); i++) {
            cout << visited_nodes[i] << " ";
        }
        cout << endl;
        if (found) {
            // Node found!
            return true;
        }
    }

    // Node not found
    return false;
}

int main() {
    Graph g(7);
    g.add_edge(0, 1);
    g.add_edge(0, 2);
    g.add_edge(1, 3);
    g.add_edge(1, 4);
    g.add_edge(2, 5);
    g.add_edge(2, 6);

    int start_node = 0;
    int target_val = 5;

    bool found = dfs(g, start_node, target_val);

    if (found) {
        cout << "Node with value " << target_val << " found in the graph!" << endl;
    } else {
        cout << "Node with value " << target_val << " not found in the graph." << endl;
    }

    return 0;
}
