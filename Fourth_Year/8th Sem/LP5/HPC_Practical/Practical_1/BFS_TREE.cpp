#include <iostream>
#include <queue>
#include <vector>
#include <omp.h>

using namespace std;

struct TreeNode {
    int val;         // Value of the node
    TreeNode* left;  // Pointer to the left child
    TreeNode* right; // Pointer to the right child

    TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};

bool bfs(TreeNode* root, int target_val, int* visited_nodes) {
    queue<TreeNode*> q;
    q.push(root);

    int num_visited = 0;
    visited_nodes[num_visited++] = root->val;

    while (!q.empty()) {
        bool found = false;
        #pragma omp parallel for // Begin parallel section
        for (int i = 0; i < q.size(); i++) {
            TreeNode* node = q.front();
            q.pop();

            if (node->val == target_val) {
                // Node found!
                found = true;
            }

            if (node->left) {
                #pragma omp critical
                {
                    q.push(node->left);
                    visited_nodes[num_visited++] = node->left->val;
                }
            }

            if (node->right) {
                #pragma omp critical
                {
                    q.push(node->right);
                    visited_nodes[num_visited++] = node->right->val;
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
    // Example binary tree
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);
    root->right->left = new TreeNode(6);
    root->right->right = new TreeNode(7);

    int target_val = 10;

    int visited_nodes[7]; // Array to store visited nodes
    for (int i = 0; i < 7; i++) {
        visited_nodes[i] = -1; // Initialize array with -1
    }
    bool found = bfs(root, target_val, visited_nodes);

    if (found) {
        cout << "Node with value " << target_val << " found in the tree!" << endl;
    } else {
        cout << "Node with value " << target_val << " not found in the tree." << endl;
    }

    cout << "Nodes visited in order: ";
    for (int i = 0; i < 7; i++) {
        if (visited_nodes[i] != -1) {
            cout << visited_nodes[i] << " ";
        }
    }
    cout << endl;

    return 0;
}
