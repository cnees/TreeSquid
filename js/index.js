function expand(elt) {
  var h = $(this).children().height();
  var maxHeight = $(window).height() - $(this).position().top - 20;
  h = Math.min(h, maxHeight);
  $(this).css({
    height: h,
    transition: 'height 0.15s'
  });
  $(this).addClass("node-focus", 150);
  
}

function contract() {
  $(this).css({
    height: 100,
    transition: 'height 0.15s'
  });
  $(this).removeClass("node-focus", 150);
}

$(function() {
  $(".node").draggable();
  $(".node").click(function() {
    $(this).focus();
  });
  $(".node").focus(expand);
  $(".node").blur(contract);
});