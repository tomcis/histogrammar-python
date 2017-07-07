var view = new vega.View(runtime)
  .logLevel(vega.Warn) // set view logging level
  .initialize(document.querySelector('#view')) // set parent DOM element
  .renderer('canvas') // set render type (defaults to 'canvas')
  .hover() // enable hover event processing
  .run()// update and render the view
