var view = new vega.View(vega.parse(vegaJSONSpec))
  .renderer('canvas')  // set renderer (canvas or svg)
  .initialize('#view') // initialize view within parent DOM container
  .hover()             // enable hover encode set processing
  .run(); 
