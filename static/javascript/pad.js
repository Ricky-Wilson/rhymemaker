var textpad = document.getElementById("textpad");

var rhymeRequest = function(word) {
		$.ajax({
			url: "/rhyme?word=" + word,
			data: word,
			type: "GET",
			success: function(result) {
				$("#pad-output").html("");
				var obj = $.parseJSON(result);
				for (var i = 0; i < obj.length; i++) {
					var html = "<a class='rhymeword'>" + obj[i] + "</a>\&nbsp;\&nbsp;\t\t\t\t\t"
					$("#pad-output").append(html);
				}
				console.log("succss");
			}
		})
	};

function getSelection() {
	var start = textpad.selectionStart;
	var end = textpad.selectionEnd;
	return textpad.value.substring(start,end);
}

var lastSelected;

$('#textpad').click(function(e) {
	lastSelected = getSelection();
});

$("#pad-rhyme-button").click(function() {
	rhymeRequest(lastSelected);
});

