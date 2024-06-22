const adjList = {
    'A': ['B', 'C'],
    'B': ['A', 'E', 'F'],
    'C': ['A', 'D'],
    'D': ['C', 'F'],
    'E': ['B', 'F'],
    'F': ['B', 'E', 'F']
}

function depthFirstSearch(starting, goal) {
    const stack = [starting];
    const visited = new Set();

    while (stack.length > 0) {
        const current = stack.pop();
        visited.add(current)

        if (current == goal)
            return true;

        const possibleMoves = adjList[current];
        if (!possibleMoves)
            continue

        for (let i = 0; i < possibleMoves.length; i++) {
            if (!visited.has(possibleMoves[i])) {
                stack.push(possibleMoves[i])
            }


        }
    }

    return false;
}


const output = depthFirstSearch("A", "E");

console.log(output)