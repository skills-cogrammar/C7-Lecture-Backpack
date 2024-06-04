function RotatingCube(
    cube_name, 
    color, 
    rotation_speed){
    this.cube_name = cube_name;
    this.color = color;
    this.rotation_speed = rotation_speed;
}

let cubes = [];

let cube1 = new RotatingCube("Zahir", "blue", 1);
cubes.push(cube1);

let cube2 = new RotatingCube("Bongani", "red", 18);
cubes.push(cube2);

let cube3 = new RotatingCube("Troy", "green", 15);
cubes.push(cube3);

// console.table(cubes);
viewCubes(cubes)

function findCube(cubes, property, value){
    return cubes.find(c => c[property] == value)
}

// console.log(findCube(cubes, "cube_name", "Bongani"));

function getSlowestCube(cubes){
    cubes.sort((a,b)=> a.rotation_speed - b.rotation_speed);
    return cubes[0];
}

// console.table(getSlowestCube(cubes));

function getFastestCube(cubes){
    cubes.sort((a,b)=> b.rotation_speed - a.rotation_speed);
    return cubes[0];
}

// console.table(getFastestCube(cubes));

function editProperty(obj, prop, new_val){
    obj[prop] = new_val;
    viewCubes(cubes)
}

function sortByRotationSpeed(cubes){
    cubes.sort((a,b)=> a.rotation_speed - b.rotation_speed);
    viewCubes(cubes);
}

