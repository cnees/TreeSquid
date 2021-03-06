function expand(elt) {
  $(this).addClass("node-focus", 150);
}

function contract() {
  $(this).removeClass("node-focus", 150);
}

function eraseText(ID) {
//	$('[data-id='ID']').val('');
}

function setQTip(n) {
  n.qtip({
    content: [
	  n.data('user'),
	  "<br>",
      n.data('text').replace(/\r?\n/g, '<br />'),
      "<br><textarea class='reply-box' data-id='" + n.data("id") + "' placeholder='Reply'></textarea><br><button onclick='eraseText(" + n.data("id") + ")' class='reply-button' id='reply_" + n.data("id") + "'>Reply</button>"
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
  });
}

$(function() {

  console.log("index.js loaded");

  var layoutParams = {
    name: 'breadthfirst',
    directed: true, // whether the tree is directed downwards (or edges can point in any direction if false)
    padding: 30, // padding on fit
    spacingFactor: 1.1, // positive spacing factor, larger => more space between nodes (N.B. n/a if causes overlap)
    animate: true, // whether to transition the node positions
  };

  $("#create-root-button").click(function(){
    //$("#create-root-textarea").val()
	if ($("#topicField").val()) {
		if ($("#messageField").val()) {
			new_root = {
			'topic': $("#topicField").val(),
			'message': $("#messageField").val(),
			'csrfmiddlewaretoken': csrf_,
			}
		}
		else {
			new_root = {
			'topic': $("#topicField").val(),
			'message': $("#topicField").val(),
			'csrfmiddlewaretoken': csrf_,
			}	
		}
    $.post("/add_root/", new_root, function(data){
      window.location.replace("/conversation/" + data['content']['id']);
    }, 'json');
	}
  });
  
  $("#exitOverlay").click(function(){
		document.getElementById( 'overlay' ).style.display = 'none';
		document.getElementById( 'createMessage' ).style.display = 'none';
	});
	
	$("#overlay").click(function(){
		document.getElementById( 'overlay' ).style.display = 'none';
	  document.getElementById( 'createMessage' ).style.display = 'none';
	});

  $("#createMessage").click(function(event){
    event.stopPropagation();
  });
	
	$("#createOverlay").click(function(){
		document.getElementById( 'overlay' ).style.display = 'block';
		document.getElementById( 'createMessage' ).style.display = 'block';
	});

  var addReply = function(e, data, cy, layoutParams){
    var n = cy.add({
      style: {
        'border-color': color(data['user_id']),
      },
      group: "nodes",
      data: {
        id: data['id'],
        text: data['user'] + ': ' + data['text'],
        label: data['user'] + ': ' + data['text'],
      },
      renderedPosition: {x: e.originalEvent.clientX - $("#cy").offset().left, y: e.originalEvent.clientY - $("#cy").offset().top},
    });
    cy.add({ // edge
      data: {
        id: data['parent_id'] + "_" + data['id'],
        source: data['parent_id'],
        target: data['id']
      }
    });
    setQTip(n);
    var view = {
      zoom: cy.zoom(),
      pan: cy.pan()
    };
    cy.layout(layoutParams);
    cy.viewport(view);
    //add reply's sidebar
    var url = $(location).attr('href').split('/');
    if (url[url.length - 1].length > 0) var root_id = url[url.length - 1];
    else var root_id = url[url.length - 2];
    var sidebarItem = $("#sidebar #" + root_id + " div.lastMessage");
    sidebarItem.html(data['text']);
  }

  var replyToMessage = function(e) {
    var textBox = $(e.target).parent().find("textarea:first");
    if($.trim( textBox.val() ) == '') {
      return; // No  message
    }
    $("div").qtip("hide");
    data = {
        'node': textBox.attr("data-id"),
        'message': textBox.val(),
        'csrfmiddlewaretoken': csrf_,
    };
    $.post("/conversation/1/reply/", data, function(data){
      addReply(e, data['content'], cy, layoutParams);
      textBox.val('');
    }, 'json');
  }

  $("body").on('click', '.reply-button', function(e) {replyToMessage(e);});

  $("body").on('keypress', '.reply-box', function(e) {
    if (e.keyCode == 13 && !e.shiftKey) {
      replyToMessage(e);
      return false;
    }
  });

  $(".node").focus(expand);
  $(".node").blur(contract);

  var shifted_pan;

  var cy = cytoscape({

    container: document.getElementById('cy'), // container to render in

    elements: GRAPH_ELEMENTS,

    style: [ // the stylesheet for the graph
      {
        selector: 'node',
        style: {
          'border-opacity': 1,
          'border-style': 'solid',
          'border-width': 6,
          'width': 'label',
          'height': 'label',
          'shape': 'roundrectangle',
          'padding-left': '10px',
          'padding-right': '10px',
          'padding-top': '10px',
          'padding-bottom': '10px',
          'background-color': '#FFF',
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
          'width': 2,
          'line-color': '#996633',
          'target-arrow-color': '#996633',
          'target-arrow-shape': 'triangle-backcurve',
        }
      }
    ],

    
    layout: {
      name: 'breadthfirst',
      directed: true, // whether the tree is directed downwards (or edges can point in any direction if false)
      padding: 30, // padding on fit
      'padding-left': 250,
      spacingFactor: 1.1, // positive spacing factor, larger => more space between nodes (N.B. n/a if causes overlap)
      animate: false, // whether to transition the node positions
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

  var defaults = {
    zoomFactor: 0.05, // zoom factor per zoom tick
    zoomDelay: 45, // how many ms between zoom ticks
    minZoom: 0.1, // min zoom level
    maxZoom: 10, // max zoom level
    fitPadding: 50, // padding when fitting
    panSpeed: 10, // how many ms in between pan ticks
    panDistance: 10, // max pan distance per tick
    panDragAreaSize: 75, // the length of the pan drag box in which the vector for panning is calculated (bigger = finer control of pan speed and direction)
    panMinPercentSpeed: 0.25, // the slowest speed we can pan by (as a percent of panSpeed)
    panInactiveArea: 8, // radius of inactive area in pan drag box
    panIndicatorMinOpacity: 0.5, // min opacity of pan indicator (the draggable nib); scales from this to 1.0
    zoomOnly: false, // a minimal version of the ui only with zooming (useful on systems with bad mousewheel resolution)
    // icon class names
    sliderHandleIcon: 'fa fa-minus',
    zoomInIcon: 'fa fa-plus',
    zoomOutIcon: 'fa fa-minus',
    resetIcon: 'fa fa-expand'
  };

  cy.panzoom( defaults );
  cy.nodes().forEach(function(n){
    setQTip(n);
  });

});