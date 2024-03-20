// 3D vector space
// const v1 = [1, 2, 3];
// const v2 = [4, 5, 6];

// Vector addition
// const v3 = v1.map((val, i) => val + v2[i]);
console.log(v3); // Output: [5, 7, 9]

// Scalar multiplication
const v4 = v1.map((val) => 2 * val);
console.log(v4); // Output: [2, 4, 6]

function isLinearlyIndependent(vectors) {
  const matrix = vectors[0].map((_, colIndex) =>
    vectors.map((row) => row[colIndex])
  );
  const rank = matrix.length;

  for (let i = 0; i < rank; i++) {
    if (matrix[i][i] !== 0) {
      for (let j = 0; j < vectors.length; j++) {
        if (j !== i) {
          const ratio = matrix[j][i] / matrix[i][i];
          for (let k = 0; k < rank; k++) {
            matrix[j][k] -= ratio * matrix[i][k];
          }
        }
      }
    } else {
      return false;
    }
  }
  return true;
}

// Example usage
const v1 = [1, 0];
const v2 = [0, 1];
const v3 = [2, 2];

// const vectors = [v1, v2, v3];
// console.log(isLinearlyIndependent(vectors)); // Output: false

// const A = [
//   [1, 2],
//   [3, 4],
// ];
// const B = [
//   [5, 6],
//   [7, 8],
// ];

// // Matrix addition
// const C = A.map((row, i) => row.map((val, j) => val + B[i][j]));
// console.log(C);
// // Output: [[6, 8], [10, 12]]

// // Matrix subtraction
// const D = A.map((row, i) => row.map((val, j) => val - B[i][j]));
// console.log(D);
// // Output: [[-4, -4], [-4, -4]]

// const A = [
//   [1, 2],
//   [3, 4],
// ];
const B = [
  [5, 6],
  [7, 8],
];

// Scalar multiplication
const C = A.map((row) => row.map((val) => 2 * val));
console.log(C);
// Output: [[2, 4], [6, 8]]

// Matrix multiplication
const D = A.map((row, i) =>
  B[0].map((_, j) => row.reduce((sum, val, k) => sum + val * B[k][j], 0))
);
console.log(D);
// Output: [[19, 22], [43, 50]]

const math = require("mathjs");

const A = math.matrix([
  [2, 1],
  [1, 2],
]);

const { values, vectors } = math.eig(A);

console.log("Eigenvalues:");
console.log(values);
// Output: [3, 1]

console.log("Eigenvectors:");
console.log(vectors);
// Output:
// [
//   [0.7071067811865475, -0.7071067811865475],
//   [0.7071067811865475, 0.7071067811865475]
// ]

const PCA = require("ml-pca");

// Generate sample data
const X = [
  [1, 2],
  [3, 4],
  [5, 6],
  [7, 8],
];

// Apply PCA
const pca = new PCA(X);
const X_pca = pca.predict(X);

console.log("Original Data:");
console.log(X);
// Output:
// [[1, 2],
//  [3, 4],
//  [5, 6],
//  [7, 8]]

console.log("PCA-transformed Data:");
console.log(X_pca);
// Output:
// [[-2.82842712],
//  [-1.41421356],
//  [ 1.41421356],
//  [ 2.82842712]]

const math = require("mathjs");

function rotationMatrix(theta) {
  const cosTheta = math.cos(theta);
  const sinTheta = math.sin(theta);
  return math.matrix([
    [cosTheta, -sinTheta],
    [sinTheta, cosTheta],
  ]);
}

function scalingMatrix(sx, sy) {
  return math.matrix([
    [sx, 0],
    [0, sy],
  ]);
}

function shearingMatrix(kx, ky) {
  return math.matrix([
    [1, kx],
    [ky, 1],
  ]);
}

// Example usage
const v = math.matrix([1, 1]);

// Rotation by 45 degrees
const rotation = rotationMatrix(math.pi / 4);
const vRotated = math.multiply(rotation, v);
console.log("Rotated vector:", vRotated);

// Scaling by 2 along x-axis and 3 along y-axis
const scaling = scalingMatrix(2, 3);
const vScaled = math.multiply(scaling, v);
console.log("Scaled vector:", vScaled);

// Shearing by 1 along x-axis and 2 along y-axis
const shearing = shearingMatrix(1, 2);
const vSheared = math.multiply(shearing, v);
console.log("Sheared vector:", vSheared);
