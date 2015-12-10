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
      "<br><textarea data-id='" + n.data("id") + "'></textarea><br><button class='reply-button' id='reply_" + n.data("id") + "'>Reply</button>"
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
    },
    show: {
      event: 'mouseover', // Show it on hover...
      solo: true, // ...and hide all other tooltips...
    },
    hide: {
      event: 'unfocus click',
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
    cy.layout({name: 'cose'});
  }

  var replyToRoot = function(e) {
    var textBox = $(e.target).parent().find("textarea:first");
    $("div").qtip("hide");
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
          'width': 'label',
          'height': 'label',
          'shape': 'roundrectangle',
          'padding-left': '10px',
          'padding-right': '10px',
          'padding-top': '10px',
          'padding-bottom': '10px',
          'background-color': '#ccc',
          'label': 'data(text)',
          'font-size': '12px',
          'text-halign': 'center',
          'text-valign': 'center',
          'text-wrap': 'wrap',
          'text-max-width': '120px',
          'color': '#000',
        }
      },

      {
        selector: 'edge',
        style: {
          'width': 1,
          'line-color': '#999',
          'target-arrow-color': '#999',
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