const EventModel = require("../../src/models/event.model");
const { createEvent, updateEvent } = require("../../src/repository/event.repository");
const { describe, beforeEach, expect, test } = require("@jest/globals");

/*
    By having the repository for the events, we are able to test the functions since they 
    return values.

    We can have many different tests for the same function to make sure that it's doing what it needs to do.
    If we are taking a test driven approach, we can make sure that the function will do what it's expected to do
    before connecting it to the controller and the final endpoint.

    Since we are running unit tests, we don't want to be dependent on other factors like the MongoDB connection being live
    we can make sure of mocks and the spy in JEST to make the methods from the object return what we want them to return 
    when they are called. this will ensure that we are performing true unit tests and not integration tests.    
*/


// We are creating a fake implementation of the EventModel.create() method.
// The jest.spyOn() method allows us to basically say that whenever the
// EventModel.create() method is called by anything within our test suite
// the values we set for createSpy should be returned instead.
const createSpy = jest.spyOn(EventModel, "create"); 

describe("Create Event Correct Values", () => {
    beforeEach(() => {
        // We are specifying that the EventModel.create() should return 
        // the following values whenever it's called
        createSpy.mockReturnValue({
            _id: "1",
            location: "London",
            dates: []
        })
    });

    test("Should return success when event created", async () => {
        const eventBody = {
            location: "London"
        }

        const result = await createEvent(eventBody);

        expect(result.success).toBe(true);
    });

    test("Should only return the id and success message", async () => {
        const eventBody = {
            location: "London"
        }

        const result = await createEvent(eventBody);

        expect(Object.keys(result).length).toEqual(2);
    });
});

describe("Create event Invalid Input", () => {
    beforeEach(() => {
        createSpy.mockRejectedValue(new Error("Invalid Input"));    
    });

    test("Should return error when invalid input", async () => {
        const eventBody = {
            location: ""
        }

        const result = await createEvent(eventBody);

        expect(result.success).toBe(false)
    });

    test("Should return 400 error", async () => {
        const eventBody = {
            location: ""
        }

        const result = await createEvent(eventBody);

        expect(result.error.status).toBe(400)
    })
})