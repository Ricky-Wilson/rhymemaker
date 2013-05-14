// The MIT License (MIT)

// Copyright (c) 2013 Yat Choi

// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:

// The above copyright notice and this permission notice shall be included in
// all copies or substantial portions of the Software.

// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
// THE SOFTWARE.

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

function encodeHTML(s) {
    return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/"/g, '&quot;');
}

function makeRequestCall() {
	var rhymeword = $("#rhyme-input").val();
	rhymeRequest(encodeHTML(rhymeword));
}

$("#rhyme-button").click(function() {
	makeRequestCall();
});

$('body').on("click", ".rhymeword", function(e) {
	rhymeRequest(e.target.text);
});

$('#rhyme-input').bind('keypress', function(e) {
	if(e.keyCode==13){
		makeRequestCall();
	}
});


	
