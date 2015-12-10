function expand(elt) {
  $(this).addClass("node-focus", 150);
}

function contract() {
  $(this).removeClass("node-focus", 150);
}

function setQTip(n) {
  n.qtip({
    content: [
      n.data('text'),
      "<br><input data-id='" + n.data("id") + "'><br><button class='reply-button' id='reply_" + n.data("id") + "'>Reply</button>"
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
}

$(function() {

  var addReply = function(data, cy){
    console.log(data['text']);
    var n = cy.add({
      group: "nodes",
      data: {
        id: data['id'],
        text: data['text']
      },
      position: { x: 200, y: 200 }
    });
    cy.add({ // edge
      data: { id: data['parent_id'] + "_" + data['id'], source: data['parent_id'], target: data['id'] }
    });
    setQTip(n);
  }

  var replyToRoot = function(e) {
    var textBox = $(e.target).parent().find("input:first");

    data = {
        'node': textBox.attr("data-id"),
        'message': textBox.val(),
        'csrfmiddlewaretoken': csrf_,
    };
    $.post("/conversation/1/reply/", data, function(data){
      addReply(data['content'], cy);
    }, 'json');
  }

  $("body").on('click', '.reply-button', function(e) {replyToRoot(e);});

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
    setQTip(n);
  });

  cy.onRender(handler = function(){
    //console.log('frame rendered');
  });
});