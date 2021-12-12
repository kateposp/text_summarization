var BASE_URL = "http://localhost:5000"
var BAD_REQUEST = "Sorry, text is too long...";
var SERVER_ERROR = "ERROR!!! Something went wrong. Please try again after some minutes"

function summarize() {
document.getElementById("output-textarea").value = "";
document.getElementsByClassName("spinner-border")[0].style.visibility = "visible";

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
        document.getElementById("output-textarea").value = BAD_REQUEST
        throw response.json()
    }
    if (response.status == 500) {
        document.getElementById("output-textarea").value = SERVER_ERROR
        throw response.json()
    }
    return response.json();

}).then(function(response_data) {
    console.log("Json", response_data);
    document.getElementById("output-textarea").value = response_data.text
    document.getElementsByClassName("spinner-border")[0].style.visibility = "hidden";


}).catch(function(error) {
    console.log('Request failed', error);
    document.getElementsByClassName("spinner-border")[0].style.visibility = "hidden";

});

}



