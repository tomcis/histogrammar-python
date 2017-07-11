$.getJSON("https://raw.githubusercontent.com/histogrammar/histogrammar-python/vega/histogrammar/plot/vega/test/test.json", function(json) {
    console.log(json);
    for(var i=0;i<json.length;i++)
    {
        console.log(data.values[i]);
    }
});

