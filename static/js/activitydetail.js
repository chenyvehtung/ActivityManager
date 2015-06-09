$(function(){
	$("#queneDialog").dialog({
		autoOpen: false,
		close: function( event, ui ) {
			$(".coverModel").fadeOut(500);
		},
        position:{
            of:$(window),
            my:"center center-250",
        }

	});
	$("#openDialog").on("click",function(){
		$("#queneDialog").dialog("open");
		$(".coverModel").fadeIn(500);
	});
	$(".coverModel").hide();

    BindTapHideEvents($('#waiting'), $('.waiting-list'));
    BindTapHideEvents($('#reject'), $('.reject-list'));
    BindTapHideEvents($('#finish'), $('.finish-list'));
    BindTapHideEvents($('#accept'), $('.accept-list'));
    BindTapHideEvents($('#unfinish'), $('.unfinish-list'));

    HideNav();

});
function BindTapHideEvents(btnSelector, contentSelector) {
    //debugger;
    btnSelector.bind('click', function () {
        if (contentSelector.is(':hidden')) {
            contentSelector.slideDown(500);
            btnSelector.find(".hint_pic_down").removeClass("hint_pic_down").addClass("hint_pic_up");
        }
        else {
            contentSelector.slideUp(500);
            btnSelector.find(".hint_pic_up").addClass("hint_pic_down").removeClass("hint_pic_up");
        }
    })
}

function HideNav(){
    $('#queneDialog .waiting-list').hide();
    $('#queneDialog .reject-list').hide();
    $('#queneDialog .finish-list').hide();
    $('#queneDialog .accept-list').hide();
    $('#queneDialog .unfinish-list').hide();


}