$(function(){
    BindTapHideEvents($('#appling'), $('.appling-list'));
    BindTapHideEvents($('#doing'), $('.doing-list'));
    BindTapHideEvents($('#reject'), $('.reject-list'));
    BindTapHideEvents($('#finish'), $('.finish-list'));
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
    $('#studentInfoPage .appling-list').hide();
    $('#studentInfoPage .doing-list').hide();
    $('#studentInfoPage .reject-list').hide();
    $('#studentInfoPage .finish-list').hide();
    $('#studentInfoPage .unfinish-list').hide();
}