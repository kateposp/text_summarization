var BASE_URL = "http://localhost:5000"
var FAILED_ERROR = "ERROR!!! Text is too long..."

function summarize() {
document.getElementById("output-textarea").value = ""
document.getElementById("error-message").innerHTML = ""

fetch("/summarize",
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
    if (response.status == 400) {
        document.getElementById("error-message").innerHTML = FAILED_ERROR
        throw response.json()
    }
    return response.json();

}).then(function(response_data) {
    console.log("Json", response_data);
    document.getElementById("output-textarea").value = response_data.text

}).catch(function(error) {
    console.log('Request failed', error);
});

}


