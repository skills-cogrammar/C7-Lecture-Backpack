const { parentPort } = require("worker_threads");

parentPort.on("message", ({ matrixA, matrixB, startRow, endRow }) => {
  const result = multiplyMatrices(matrixA, matrixB, startRow, endRow);
  parentPort.postMessage(result);
});

function multiplyMatrices(matrixA, matrixB, startRow, endRow) {
  const colsA = matrixA[0].length;
  const colsB = matrixB[0].length;

  const result = [];
  for (let i = startRow; i < endRow; i++) {
    result[i - startRow] = [];
    for (let j = 0; j < colsB; j++) {
      let sum = 0;
      for (let k = 0; k < colsA; k++) {
        sum += matrixA[i][k] * matrixB[k][j];
      }
      result[i - startRow][j] = sum;
    }
  }

  return result;
}
