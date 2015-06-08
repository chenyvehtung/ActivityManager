$(function(){
	$("#queneDialog").dialog({
		autoOpen: false,
		close: function( event, ui ) {
			$(".coverModel").fadeOut(500);
		}
	});
	$("#openDialog").on("click",function(){
		$("#queneDialog").dialog("open");
		$(".coverModel").fadeIn(500);
	});
	$(".coverModel").hide();
});
