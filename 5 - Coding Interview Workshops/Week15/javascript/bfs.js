const adjList = {
    'A': ['B', 'C'],
    'B': ['A', 'E', 'F'],
    'C': ['A', 'D'],
    'D': ['C', 'F'],
    'E': ['B', 'F'],
    'F': ['B', 'E', 'F']
}

function depthFirstSearch(starting, goal) {
    const queue = [starting];
    const visited = new Set();

    while (queue.length > 0) {
        const current = queue.pop();
        visited.add(current)

        if (current == goal)
            return true;

        const possibleMoves = adjList[current];
        if (!possibleMoves)
            continue

        for (let i = 0; i < possibleMoves.length; i++) {
            if (!visited.has(possibleMoves[i])) {
                queue.unshift(possibleMoves[i])
            }


        }
    }

    return false;
}


const output = depthFirstSearch("A", "E");

console.log(output)