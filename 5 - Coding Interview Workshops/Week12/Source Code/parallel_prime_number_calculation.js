const { Worker } = require("worker_threads");
const { ChartJSNodeCanvas } = require("chartjs-node-canvas");
const os = require("os");

function nonParallelMultiply(matrixA, matrixB) {
  const rowsA = matrixA.length;
  const colsA = matrixA[0].length;
  const rowsB = matrixB.length;
  const colsB = matrixB[0].length;

  if (colsA !== rowsB) {
    throw new Error("Incompatible matrix dimensions");
  }

  const result = [];
  for (let i = 0; i < rowsA; i++) {
    result[i] = [];
    for (let j = 0; j < colsB; j++) {
      let sum = 0;
      for (let k = 0; k < colsA; k++) {
        sum += matrixA[i][k] * matrixB[k][j];
      }
      result[i][j] = sum;
    }
  }

  return result;
}

function parallelMultiply(matrixA, matrixB) {
  return new Promise((resolve, reject) => {
    const numWorkers = os.cpus().length;
    const workers = [];
    const results = [];

    const rowsA = matrixA.length;
    const chunkSize = Math.ceil(rowsA / numWorkers);

    for (let i = 0; i < numWorkers; i++) {
      const startRow = i * chunkSize;
      const endRow = Math.min(startRow + chunkSize, rowsA);

      const worker = new Worker("./worker.js");
      worker.on("message", (result) => {
        results.push(result);
        if (results.length === numWorkers) {
          const finalResult = results.reduce((acc, val) => acc.concat(val), []);
          resolve(finalResult);
        }
      });
      worker.on("error", (error) => {
        reject(error);
      });
      worker.postMessage({ matrixA, matrixB, startRow, endRow });
      workers.push(worker);
    }
  });
}

function generateMatrix(rows, cols) {
  const matrix = [];
  for (let i = 0; i < rows; i++) {
    matrix[i] = [];
    for (let j = 0; j < cols; j++) {
      matrix[i][j] = Math.floor(Math.random() * 10);
    }
  }
  return matrix;
}

async function measureExecutionTime(matrixSize) {
  const matrixA = generateMatrix(matrixSize, matrixSize);
  const matrixB = generateMatrix(matrixSize, matrixSize);

  const startNonParallel = Date.now();
  await nonParallelMultiply(matrixA, matrixB);
  const endNonParallel = Date.now();
  const nonParallelTime = endNonParallel - startNonParallel;

  const startParallel = Date.now();
  await parallelMultiply(matrixA, matrixB);
  const endParallel = Date.now();
  const parallelTime = endParallel - startParallel;

  return { nonParallelTime, parallelTime };
}

async function generateGraph() {
  const matrixSizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000];
  const nonParallelTimes = [];
  const parallelTimes = [];

  for (const size of matrixSizes) {
    const { nonParallelTime, parallelTime } = await measureExecutionTime(size);
    nonParallelTimes.push(nonParallelTime);
    parallelTimes.push(parallelTime);
    console.log(`Matrix Size: ${size}x${size}`);
    console.log(`Non-parallel time: ${nonParallelTime} ms`);
    console.log(`Parallel time: ${parallelTime} ms`);
    console.log("--------------------");
  }

  const width = 800;
  const height = 600;
  const backgroundColour = "white";
  const chartJSNodeCanvas = new ChartJSNodeCanvas({
    width,
    height,
    backgroundColour,
  });

  const configuration = {
    type: "line",
    data: {
      labels: matrixSizes.map((size) => `${size}x${size}`),
      datasets: [
        {
          label: "Non-parallel",
          data: nonParallelTimes,
          borderColor: "rgba(75, 192, 192, 1)",
          fill: false,
        },
        {
          label: "Parallel",
          data: parallelTimes,
          borderColor: "rgba(255, 99, 132, 1)",
          fill: false,
        },
      ],
    },
    options: {
      scales: {
        x: {
          title: {
            display: true,
            text: "Matrix Size",
          },
        },
        y: {
          title: {
            display: true,
            text: "Execution Time (ms)",
          },
        },
      },
    },
  };

  const buffer = await chartJSNodeCanvas.renderToBuffer(configuration);
  const fs = require("fs");
  const path = require("path");
  const outputPath = path.join(__dirname, "execution_time_graph.png");
  fs.writeFileSync(outputPath, buffer);
  console.log("Graph saved as execution_time_graph.png");

  process.exit();
}

generateGraph();
