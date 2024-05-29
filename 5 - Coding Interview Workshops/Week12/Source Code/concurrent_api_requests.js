const axios = require("axios");
const { ChartJSNodeCanvas } = require("chartjs-node-canvas");

const apiUrl = "https://api.github.com/users/octocat";
const token = "your_token_here";
const headers = { Authorization: `token ${token}` };

async function makeSequentialRequests(numRequests) {
  const startTime = Date.now();
  for (let i = 0; i < numRequests; i++) {
    await axios.get(apiUrl, { headers });
  }
  const endTime = Date.now();
  const duration = endTime - startTime;
  return duration;
}

async function makeConcurrentRequests(numRequests) {
  const startTime = Date.now();
  const promises = [];
  for (let i = 0; i < numRequests; i++) {
    promises.push(axios.get(apiUrl, { headers }));
  }
  await Promise.all(promises);
  const endTime = Date.now();
  const duration = endTime - startTime;
  return duration;
}

async function generateGraph() {
  const numRequestsArray = [1, 5, 10, 20, 30, 40, 50];
  const sequentialTimes = [];
  const concurrentTimes = [];

  for (const numRequests of numRequestsArray) {
    const sequentialTime = await makeSequentialRequests(numRequests);
    const concurrentTime = await makeConcurrentRequests(numRequests);
    sequentialTimes.push(sequentialTime);
    concurrentTimes.push(concurrentTime);
    console.log(`Number of Requests: ${numRequests}`);
    console.log(`Sequential Time: ${sequentialTime} ms`);
    console.log(`Concurrent Time: ${concurrentTime} ms`);
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
      labels: numRequestsArray,
      datasets: [
        {
          label: "Sequential",
          data: sequentialTimes,
          borderColor: "rgba(75, 192, 192, 1)",
          fill: false,
        },
        {
          label: "Concurrent",
          data: concurrentTimes,
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
            text: "Number of Requests",
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
  const outputPath = path.join(__dirname, "api_requests_graph.png");
  fs.writeFileSync(outputPath, buffer);
  console.log("Graph saved as api_requests_graph.png");

  process.exit();
}

generateGraph();
