fetch("https://api.open-meteo.com/v1/forecast?latitude=35.0211&longitude=135.7538&hourly=temperature_2m,rain,showers&daily=sunrise,sunset&timezone=auto")
    .then((response) => response.json())
    .then((data) => console.log(data.hourly.temperature_2m))
    .catch((error) => console.error(error));


async function getImage(){
    let item = await fetch("http://thecatapi.com/api/images/get?format=src&type=gif");
    console.log(item.urlList);
}

getImage();