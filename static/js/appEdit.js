$(function(){
	//给所有Input标签都加上form-control类
	$("input").addClass("form-control");
	$("textarea").addClass("form-control");
	$("button").addClass("form-control btn-primary");

	//给表单添加验证功能
	$("#activityEditForm").validate({
		rules:{
			phone:{
				required:true,
				number:true
			}
		},
		messages:{
			phone:{
				number:"请输入数字"
			}

		}
	});
});
