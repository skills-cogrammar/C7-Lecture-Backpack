const express = require('express');
const controllers = require('../controllers/controller');

const router = express.Router();

router.post('/admin_login', controllers.loginUser);
router.post('/admin_signup', controllers.createAdminUser);

// app.get('/admin_resource', (req, res) => {
//     const headers = req.headers['authorization'];
//     const token = headers.split(' ')[1];

//     try {
//       const decoded = jwt.verify(token, 'lecture-1-secret');

//       if (decoded.admin) {
//         res.send({
//             "message": "Success!" 
//         });
//       } else {
//         res.status(403).send({
//             "message": "Your JWT was verified, but you do not have admin access."
//         });
//       }
//     } catch (e) {
//       res.sendStatus(401);
//     }
// });

// Exports
module.exports = {
    router
}