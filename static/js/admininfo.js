$(function(){
    BindTapHideEvents($('#student'), $('.student-list'));
    BindTapHideEvents($('#black-student'), $('.black-student-list'));
    BindTapHideEvents($('#cor'), $('.cor-list'));
    BindTapHideEvents($('#black-cor'), $('.black-cor-list'));
    BindTapHideEvents($('#wait-cor'), $('.wait-cor-list'));
    BindTapHideEvents($('#all-admin'), $('.all-admin-list'));
    BindTapHideEvents($('#all-activity'), $('.all-activity-list'));

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
    $('#adminInfoPage .student-list').hide();
    $('#adminInfoPage .black-student-list').hide();
    $('#adminInfoPage .cor-list').hide();
    $('#adminInfoPage .black-cor-list').hide();
    $('#adminInfoPage .wait-cor-list').hide();
    $('#adminInfoPage .all-admin-list').hide();
    $('#adminInfoPage .all-activity-list').hide();
}