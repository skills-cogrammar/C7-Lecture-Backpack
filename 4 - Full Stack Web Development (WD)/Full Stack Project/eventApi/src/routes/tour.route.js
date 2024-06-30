const router = require("express").Router();
const { createTour, getAllTours, getTour } = require("../controllers/tour.controller")
const { createEvent, getAllEvents } = require("../controllers/event.controller");

router.post("/", createTour);
router.get("/", getAllTours);
router.get("/:id", getTour);
router.post("/:tourId/event", createEvent);
router.post("/events", getAllEvents) //

module.exports = router;
