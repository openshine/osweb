$(document).ready(function() {
	
	//formulario
	var emailValido = {
	       email: function(el) {return /^[A-Za-z][A-Za-z0-9_]*@[A-Za-z0-9_]+\.[A-Za-z0-9_.]+[A-za-z]$/.test($(el).val());}
	}
	
	$("#userEmail").blur(function(){
		var v = $(this).attr("value");
		if (v) {
			$(this).removeClass("error");
			$($($(this).parents("p")[0]).children("span")[0]).removeClass("error").addClass("ok").text("Correcto");
			var er_email = /^(.+\@.+\..+)$/
			if(!er_email.test(v)) {
				$(this).addClass("error");
				$($($(this).parents("p")[0]).children("span")[0]).removeClass("ok").addClass("error").text("Email inválido");
			} else 	{
				$(this).removeClass("error");
				$($($(this).parents("p")[0]).children("span")[0]).removeClass("error").addClass("ok").text("Correcto");
			}
		}
		else {
			$(this).addClass("error");
			$($($(this).parents("p")[0]).children("span")[0]).removeClass("ok").addClass("error");
		}
	});
	
	//closeThis y openThat
	$('.closeThis').click(
		function()
		{
			var e = $(this).attr('rel');
			$('#'+e).slideUp('fast');
			return false;
		}
	);
	$('.openThat').click(
		function()
		{
			var e = $(this).attr('rel');
			$('#'+e).slideDown('fast');
			return false;
		}
	);
	

});