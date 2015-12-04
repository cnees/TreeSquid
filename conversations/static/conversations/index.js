function expand(elt) {
  console.log('test');$(this).addClass("node-focus", 150);
}

function contract() {
  $(this).removeClass("node-focus", 150);
}

$(function(){
  console.log("Document ready");
  $(".node").focus(expand);
  $(".node").blur(contract);

  var cy = cytoscape({

    container: document.getElementById('cy'), // container to render in

    elements: GRAPH_ELEMENTS,

    style: [ // the stylesheet for the graph
      {
        selector: 'node',
        style: {
          'background-color': '#666',
          'label': 'data(id)'
        }
      },

      {
        selector: 'edge',
        style: {
          'width': 3,
          'line-color': '#ccc',
          'target-arrow-color': '#ccc',
          'target-arrow-shape': 'triangle'
        }
      }
    ],

    layout: {
      name: 'grid',
      rows: 1
    },

    headless: false,
    styleEnabled: true,
    hideEdgesOnViewport: false,
    hideLabelsOnViewport: false,
    textureOnViewport: false,
    motionBlur: false,
    motionBlurOpacity: 0.2,
    wheelSensitivity: 1,
    pixelRatio: 1
  });

  cy.add({
      group: "nodes",
      data: { weight: 75 },
      position: { x: 200, y: 200 }
  });

  cy.onRender(handler = function(){
    console.log('frame rendered');
  });
});