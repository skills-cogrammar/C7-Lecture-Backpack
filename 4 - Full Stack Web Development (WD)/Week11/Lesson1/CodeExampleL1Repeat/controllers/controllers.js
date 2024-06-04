const models = require("../model/schema");
const model = models.personModel;

const createPerson = async (req, res) => {
    try {
        const {reqName, reqAge} = req.body;
        const person = await model.create( {
            name: reqName,
            age: reqAge
        });
        const newPerson = await model.save();
        res.send(newPerson);
        console.log("Person created successfully");
    } catch (error) {
        console.error("Error occured while creating new Person", error);
    }
};

module.exports = {
    createPerson
};