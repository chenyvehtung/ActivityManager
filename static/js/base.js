$(function(){
	//给所有Input标签都加上form-control类
	$("input").addClass("form-control");
	$("textarea").addClass("form-control");
	$("form table").css("width","100%");

	$(".toTop").click(function(e) {
            //以1秒的间隔返回顶部
            $('body,html').animate({scrollTop:0},500);
   });

	$(".toTop").hide();
	$(window).scroll(function(e) {
         //若滚动条离顶部大于100元素
         if($(window).scrollTop()>100)
             $(".toTop").fadeIn(1000);//以1秒的间隔渐显id=gotop的元素
         else
             $(".toTop").fadeOut(1000);//以1秒的间隔渐隐id=gotop的元素
     });
});


