// Create a scene
let scene = new THREE.Scene();

// Create a camera
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.z = 5;

// Create a renderer
const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

let meshes =[] ;


// Render the scene
function animate() {
    requestAnimationFrame(animate);
    
    meshes.forEach(x => {
        x.mesh.rotation.x += (0.01 * x.rotation_speed); 
    })
    
    renderer.render(scene, camera);
}

function viewCubes(rotating_cubes){
    scene.clear();
    meshes = [];
    let start = -5;
    rotating_cubes.forEach(cube => {
        let geometry = new THREE.BoxGeometry();
        let material = new THREE.MeshBasicMaterial({ color: cube.color })
        let mesh = new THREE.Mesh(geometry, material);
        mesh.position.x += start;
        start+=5;
        scene.add(mesh);
        meshes.push({ 
            mesh: mesh, 
            rotation_speed: cube.rotation_speed 
        });
    });

}
animate();
