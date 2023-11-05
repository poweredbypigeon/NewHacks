// alert("The test extension is up and running")

/*
So how Forest tracks usage is that it does so in the background. 
*/// background.js
/*
TODO:
1. save data
2. integrate with .h5 file
- have a big red button that allows you to pause/unpause it. 
3. list of good/bad websites
in the end it's just supposed to trakc whether you're focused or not, and may give you warnings if you're under time. 
*/

document.getElementById('toggle').addEventListener('click', function() {
    // Send a request to your Python script
    fetch('http://localhost:5000/endpoint', {
        method: 'POST',
        body: JSON.stringify({ signal: document.getElementById('toggle').getAttribute('value')}),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response from your Python script
        console.log(data);
    });
});