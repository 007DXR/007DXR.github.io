$(function () {
	$("#ill").click(function () {
		//先将所有的kepu hide起来
		$('[id$=-kepu]').hide();
		$('#ill-kepu').show();
	});
	$("#feed").click(function () {
		$('[id$=-kepu]').hide();
		$("#feed-kepu").show();
	});
	$("#adopt").click(function () {
		$('[id$=-kepu]').hide();
		$('#adopt-kepu').show();
	});
	$("#oper").click(function () {
		$('[id$=-kepu]').hide();
		$('#oper-kepu').show();
	});
	$("#lu").click(function () {
		$('[id$=-kepu]').hide();
		$('#lu-kepu').show();
	});
});

