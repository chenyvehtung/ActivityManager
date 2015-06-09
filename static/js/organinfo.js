$(function(){
    BindTapHideEvents($('#mycreate'), $('.mycreate-list'));
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
    $('#OrganInfoPage .mycreate-list').hide();

}