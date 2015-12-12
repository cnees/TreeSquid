function expand(elt) {
  $(this).addClass("node-focus", 150);
}

function contract() {
  $(this).removeClass("node-focus", 150);
}

function setQTip(n) {
  n.qtip({
    content: [
      n.data('text').replace(/\r?\n/g, '<br />'),
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
        event: 'mouseover'
    },
    hide: {
        event: 'mouseout'
    },
  });
}

$(function() {

  $("#create-root-button").click(function(){
    //$("#create-root-textarea").val()
    new_root = {
      'message': $("#create-root-textarea").val(),
      'csrfmiddlewaretoken': csrf_,
    }
    $.post("/add_root/", new_root, function(data){
      window.location.replace("/conversation/" + data['content']['id']);
    }, 'json');
  });2

  var addReply = function(e, data, cy){
    console.log(data['text']);
    var n = cy.add({
      group: "nodes",
      data: {
        id: data['id'],
        text: data['text'],
        label: data['text']
      },
    });
    cy.add({ // edge
      data: { id: data['parent_id'] + "_" + data['id'], source: data['parent_id'], target: data['id'] }
    });
    setQTip(n);
    var view = {
      zoom: cy.zoom(),
      pan: cy.pan()
    };
    cy.layout({name: 'breadthfirst'});
    //cy.viewport(view);
  }

  var replyToMessage = function(e) {
    var textBox = $(e.target).parent().find("textarea:first");
    $("div").qtip("hide");
    data = {
        'node': textBox.attr("data-id"),
        'message': textBox.val(),
        'csrfmiddlewaretoken': csrf_,
    };
    $.post("/conversation/1/reply/", data, function(data){
      addReply(e, data['content'], cy);
      console.log(data)
    }, 'json');
  }

  $("body").on('click', '.reply-button', function(e) {replyToMessage(e);});

  $(".node").focus(expand);
  $(".node").blur(contract);

  var cy = cytoscape({

    container: document.getElementById('cy'), // container to render in

    elements: GRAPH_ELEMENTS,

    style: [ // the stylesheet for the graph
      {
        selector: 'node',
        style: {
          'border-opacity': 1,
          'border-style': 'solid',
          'border-width': 1,
          'width': 'label',
          'height': 'label',
          'shape': 'roundrectangle',
          'padding-left': '10px',
          'padding-right': '10px',
          'padding-top': '10px',
          'padding-bottom': '10px',
          'background-color': '#fff',
          'label': 'data(label)',
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
          'line-color': '#000',
          'target-arrow-color': '#000',
          'target-arrow-shape': 'triangle-backcurve',
        }
      }
    ],

    layout: {
      name: 'breadthfirst'
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