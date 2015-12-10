function expand(elt) {
  console.log('test');$(this).addClass("node-focus", 150);
}

function contract() {
  $(this).removeClass("node-focus", 150);
}

$(document).ready(function() {
  var replytoroot = function() {
    $.ajax({
      type: "GET",
      url: "/conversation/1/reply/",
      data: {
        'node': 1
      },
    }).done(function(a){
      var span = "<br/><span>" + a['content']['reply'] + "</span>"
      $("#replyDiv").append(span);
    });
  }

  $("#reply").click(replytoroot);
});

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
      name: 'cose'
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

  cy.nodes().forEach(function(n){
    n.qtip({
      content: [
        n.data('text'),
        "<form><input><br><button type='submit' id='" + n.data("text") + "'>Reply</button></form>"
      ],
      position: {
        my: 'top center',
        at: 'bottom center'
      },
      style: {
        classes: 'qtip-bootstrap',
        tip: {
          width: 16,
          height: 8
        }
      }
    });
  });

  cy.onRender(handler = function(){
    console.log('frame rendered');
  });
});