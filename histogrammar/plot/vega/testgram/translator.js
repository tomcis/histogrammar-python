//loading our json
var requestURL = 'vega/test/test.json';
var request = new XMLHttpRequest();
request.open('GET',requestURL);
request.responseType = 'json';
request.send()
