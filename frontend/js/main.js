$(window).load(function(){
	var sidebar = document.getElementById("sidebar")
	var sidebarToggleWrap = document.getElementById("sidebarToggleWrap");
	var container = document.getElementsByClassName("container")[0];

	sidebarToggle.addEventListener("click", () => {
		sidebarToggleWrap.classList.toggle("open-sidebar");
		sidebar.classList.toggle("open-sidebar");
		container.classList.toggle("open-sidebar");
	});

	/*
	$("[data-toggle]").click(function() {
	  var toggle_el = $(this).data("toggle");
	  $(toggle_el).toggleClass("open-sidebar");
	});
	 $(".swipe-area").swipe({
		   swipeStatus:function(event, phase, direction, distance, duration, fingers){
				 if (phase=="move" && direction =="right") {
					   $(".container").addClass("open-sidebar");
					   return false;
				 }
				 if (phase=="move" && direction =="left") {
					   $(".container").removeClass("open-sidebar");
					   return false;
				 }
		   }
	 }); 
	 */
});