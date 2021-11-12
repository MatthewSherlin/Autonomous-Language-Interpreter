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

