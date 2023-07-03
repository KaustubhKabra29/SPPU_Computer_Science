#include <iostream>
#include <queue>
#include <vector>
#include <omp.h>

using namespace std;

const int MAX_NODES = 100;

// Graph representation using an adjacency list
vector<int> graph[MAX_NODES];

bool bfs(int start_node, int target_node, int n, int* visited_nodes) {
    bool visited[MAX_NODES] = {false};
    queue<int> q;

    visited[start_node] = true;
    q.push(start_node);

    int num_visited = 0;
    visited_nodes[num_visited++] = start_node;

    while (!q.empty()) {
        bool found = false;
        #pragma omp parallel for
        for (int i = 0; i < q.size(); i++) {
            int node = q.front();
            q.pop();

            if (node == target_node) {
                // Node found!
                found = true;
            }

            for (int j = 0; j < graph[node].size(); j++) {
                int neighbor = graph[node][j];

                if (!visited[neighbor]) {
                    #pragma omp critical
                    {
                        visited[neighbor] = true;
                        q.push(neighbor);
                        visited_nodes[num_visited++] = neighbor;
                    }
                }
            }
        }
        if (found) {
            // Node found!
            return true;
        }
    }

    // Node not found
    return false;
}

int main() {
    // Example graph
    graph[0] = {1, 2};
    graph[1] = {0, 3, 4};
    graph[2] = {0, 5};
    graph[3] = {1};
    graph[4] = {1};
    graph[5] = {2};

    int num_nodes = 6;
    int start_node = 0;
    int target_node = 5;

    int visited_nodes[MAX_NODES];
    bool found = bfs(start_node, target_node, num_nodes, visited_nodes);

    if (found) {
        cout << "Node " << target_node << " found in the graph!" << endl;
    } else {
        cout << "Node " << target_node << " not found in the graph." << endl;
    }

    cout << "Nodes visited in order: ";
    for (int i = 0; i < num_nodes; i++) {
        if (visited_nodes[i] != -1) {
            cout << visited_nodes[i] << " ";
        }
    }
    cout << endl;

    return 0;
}
