const { describe, beforeEach , test, expect } = require("@jest/globals")
const { getEvent } = require("../../src/controllers/event.controller")
const EventModel = require("../../src/models/event.model")

// Whenever the 'find' method is called from the mongoose object 
// what ever values we set will be returned, this will remove the 
// need to have a database connection running
const findSpy = jest.spyOn(EventModel, 'find');

describe("Test the functionality of the controllers", () => {
    beforeEach(() => {
        // We are setting what will be returned very time the method is called
        findSpy.mockReturnValue([
            {
                _id: "XXXXXXXXXX",
                name: "Test Event",
                description: "This is a test event",
                date: "2023-05-01"
            }                    
        ])
    })

    test("Gets all of the details when the ID is correct", async () => {
        // We won't need to connect to the database for this call to work        
        const output = await getEvent("", "");        
        expect(output).toHaveLength(1);
    })
})