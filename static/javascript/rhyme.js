$(document).ready(function() {
	$("#resultinfo").hide();
});

var rhymeRequest = function(word) {

		$.ajax({
			url: "/rhyme?word=" + word,
			data: word,
			type: "GET",
			success: function(result) {
				$("#output").html("");
				$("#rhyme-input").val("");
				$("#queried").html(word);
				$("#resultinfo").show();
				var obj = $.parseJSON(result);
				for (var i = 0; i < obj.length; i++) {
					var html = "<a class='rhymeword'>" + obj[i] + "</a>\&nbsp;\&nbsp;\t\t\t\t\t"
					$("#output").append(html);
				}
				console.log("succss");
			}
		})
	};

$("#rhyme-button").click(function() {
	console.log("click");
	rhymeRequest($("#rhyme-input").val());
});

$('body').on("click", ".rhymeword", function(e) {
	rhymeRequest(e.target.text);
});

$('#rhyme-input').bind('keypress', function(e) {
	if(e.keyCode==13){
		rhymeRequest($("#rhyme-input").val());
		console.log("enter");
	}
});
	
