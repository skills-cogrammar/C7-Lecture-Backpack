const express = require('express');
const bodyParser = require('body-parser')
const app = express();
const port = process.env.PORT || 5000;

// middleware
app.use(bodyParser.json())

// api storage
let apis = {
    '/api/data': {
        enable: false,
        handler: (req, res) => res.json({
            data: "Initial Data"
        })
    }
}

// Route to manage enabling APIs
app.post('/manage/enable', (req, res) => {
    const { apiPath } = req.body;
    if (apis[apiPath]) {
        apis[apiPath.enable] = true;
        app.use(apiPath, apis[apiPath].handler);
        res.send(`API ${apiPath} enabled!`);
    } else {
        res.status(404).send('API NOT FOUND!!!')
    }
})

// Route to manage disabling APIs
app.post('/manage/disable', (req, res) => {
    const { apiPath } = req.body;
    if (apis[apiPath]) {
        apis[apiPath.enable] = false;
        // app.use(apiPath, apis[apiPath].handler);
        res.send(`API ${apiPath} disabled!`);
    } else {
        res.status(404).send('API NOT FOUND!!!')
    }
})


// Route to modify API
app.post('/manage/modify', (req, res) => {
  const { apiPath, newHandler } = req.body;
  if (apis[apiPath] && typeof eval(newHandler) === 'function') {
    apis[apiPath].handler = eval(newHandler);
    if (apis[apiPath].enabled) {
      res.send(`API ${apiPath} modified and enabled.`);
    } else {
      res.send(`API ${apiPath} modified.`);
    }
  } else {
    res.status(404).send('API not found or handler is invalid.');
  }
});


// Route to list all APIs
app.get('/manage/list', (req, res) => {
  res.json(apis);
});

// Home route
app.get('/', (req, res) => {
  res.send('API Management Portal is running!');
});

// Start the server
app.listen(port, () => {
    console.log(`Server is running on port ${port}`)
})