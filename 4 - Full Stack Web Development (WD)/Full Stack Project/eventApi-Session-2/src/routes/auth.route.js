const router = require('express').Router();
const { authenticateUser, createUser } = require("../controllers/auth.controller")

router.post('/sign-up', createUser);
router.post('/login', authenticateUser);

module.exports = router;