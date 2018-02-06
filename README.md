# A Flask Matplotlib Tutorial

Hopefully this will walk you through integrating semi-responsive matplotlib charts in a small flask app. 

## Background
There is a spectrum of responsive web plotting options that I am aware of, in the order of more Python/Flask to more JS:
 * Static charts made on demand: Generate plots with [matplotlib](https://matplotlib.org/) and a URL (I don't know if this counts as responsive, it's kinda responsive). This is great if your plots are going to get fancier than lines, bars, and scatter plots and you don't want to add a bunch of JS overhead to your app.
 * Dynamic charts that let you zoom and stuff: [Vega-lite](https://vega.github.io/vega-lite/) is the new grammar-of-graphics hottness and Python libraries like [Altair](https://altair-viz.github.io/) and [pdvega](https://jakevdp.github.io/pdvega/) make it easy to use and give you all sorts of free cool features. They mostly focus on statistical plotting, so this might not be the one to pick for your 
 * I think Bokeh fits in about here. [Bokeh](https://bokeh.pydata.org) is great if you have a lot of data and you want to stream it to the chart, there is more setup than vega because it creates servers and streams data. 
 * Responsive D3 plotting: [D3](https://d3js.org/) is great and really fun and creates pretty mind-blowing plots, but you're gonna be writing some JS.
 * Fancy 3D WebGL: [Three.js](https://threejs.org/) is amazing, but at this point you are basically building a 3D video game. 
 
 They are all good! It just depends on what you are trying to do. They can all work with any web framework, we're going to use Flask here.

## Overview
We are going to make an app in Flask that makes a chart based on URL data and serves it to the page.
## Setting up a virtual environment
 