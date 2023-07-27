d3.json('http://127.0.0.1:5000/api/v1.0/authors').then(function (data) {
    let title = 'Books by the same weird d00d'
    let books = []
    let timesRead = []
    
    for (const property in data) {
        books.push(property)
        timesRead.push(data[property].length)
    }
    
    let trace1 = {
        x: books,
        y: timesRead,
        type: 'bar'
    };

    let info = [trace1];

    let layout = {
        title: title
    };

    Plotly.newPlot("plot", info, layout);
});
