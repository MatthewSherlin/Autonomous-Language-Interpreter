window.onload = function () {
	if (localStorage.getItem("hasCodeRunBefore") === null) {
	  alert("DISCLAIMER:\nALI is not responsible for any personal damages, injuries, or death arising from the usage of the ALI software, or for any decision or action taken based upon the ALI software.\nALI is intended for use as an aide in communicating between language barriers, and as a result may not always be accurate. It is the responsibility of the professional user to make the final determining decision in any medical scenario, regardless of the information displayed within ALI. ALI and all associated components are protected under this disclaimer.\nOnly use this software if you've read and understood this message.")
	  localStorage.setItem("hasCodeRunBefore", true);
	}
  }

function submit() {
	document.forms[0].action = "/translate";
    document.forms[0].submit(); 
}

$(".hamburger").click(function() {
	$(".links").toggleClass("move");
});

$(".link-close").click(function() {
  	$(".links").toggleClass("move");
});

$(".translation-tab").click(function() {
  	$(".text-wrapper").toggleClass("move-text");
});

$(".text-close").click(function() {
	$(".text-wrapper").toggleClass("move-text");
});

$(".notes-tab").click(function() {
	$(".notes").toggleClass("move-notes");
});

$(".record-close").click(function() {
	$(".notes").toggleClass("move-notes");
});

$(".fa-sync-alt").click(function() {
   var val1 = $("#languages1 option:selected").val();
   var text1 = $("#languages1 option:selected").text();
   var val2 = $("#languages2 option:selected").val();
   var text2 = $("#languages2 option:selected").text();

   if (val1 != "" && val2 != "") {
		$("#languages1 option:selected").val(val2);
		$("#languages1 option:selected").text(text2);
		$("#languages2 option:selected").val(val1);
		$("#languages2 option:selected").text(text1);
   }
});	

