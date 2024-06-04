fetch("https://api.kanye.rest/")
    .then((response) => response.json())
    .then((data) => console.log(data))
    .catch((error) => console.log(error));