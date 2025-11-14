import streamlit as st

# Define the directed graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['H'],
    'F': ['G'],
    'G': [],
    'H': []
}

# DFS function with alphabetical tie-breaking
def dfs(graph, start, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path.append(start)

    for neighbor in sorted(graph[start]):
        if neighbor not in visited:
            dfs(graph, neighbor, visited, path)
    return path

# Streamlit UI
st.title("Depth-First Search (DFS) Traversal")
st.write("This app demonstrates DFS traversal on a directed graph with alphabetical tie-breaking.")

start_node = st.selectbox("Select starting node:", sorted(graph.keys()))

if st.button("Run DFS"):
    dfs_path = dfs(graph, start_node)
    st.success(f"DFS Traversal Path from '{start_node}': {' → '.join(dfs_path)}")

    st.subheader("Complexity Notes")
    st.markdown("""
    - **Time Complexity**: O(V + E), where V is the number of vertices and E is the number of edges.
    - **Space Complexity**: O(V) for visited set and recursion stack.
    - **Use Case**: DFS is useful for exploring all paths, detecting cycles, and solving puzzles like mazes.
    """)

st.markdown("---")
st.write("Author: [Nur Izzati Binti Zakaria] | Student ID: [SD23007]")

st.markdown("Please ensure this app is deployed and linked in your lab report along with your GitHub repository.")

