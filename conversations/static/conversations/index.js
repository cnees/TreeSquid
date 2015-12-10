function expand(elt) {
  console.log('test');$(this).addClass("node-focus", 150);
}

function contract() {
  $(this).removeClass("node-focus", 150);
}

// var csrf = "";

$(function() {

  var addReply = function(a){
    var span = "<br/><span>" + a['content']['reply'] + "</span>"
    $("#replyDiv").append(span);
  }

  var replytoroot = function() {
    // alert(csrf_);
    data = {
        'node': 1,
        'message': "I'm a new message. Hello to you",
        'csrfmiddlewaretoken': csrf_,
    };
    $.post("/conversation/1/reply/", data, function(data){
      addReply(data);
    }, 'json');
    // $.ajax({
    //   type: "POST",
    //   url: "/conversation/1/reply/",
    //   // contentType: false,
    //   data: {
    //     csrfmiddlewaretoken: csrf_,
    //     'node': 1,
    //     'message': "I'm a new message. Hello to you",
    //   },
    // }).done(function(a){
      
    // });
  }

  $("#reply").click(replytoroot);


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