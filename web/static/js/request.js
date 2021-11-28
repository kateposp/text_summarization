var BASE_URL = "http://localhost:5000"

function summarize() {
fetch("summarize",
{
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    method: "POST",
    body: JSON.stringify({
        "text" : document.getElementById("input-textarea").value}
    )
}).then(function(response) {
    return response.json();

}).then(function(response_data) {
    console.log("Json", response_data);
    document.getElementById("output-textarea").value = response_data.text

}).catch(function(error) {
    console.log('Request failed', error);
});

}


