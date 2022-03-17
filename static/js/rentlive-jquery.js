/*This is TWD Chapter 16 page 288
*/
$(document).ready(function() {
	$('.Nav-Link').hover(
		function(){
			$(this).css('color', 'blue');
		},
		function(){
			$(this).css('color', 'white');
		});

	$('.City-Link').hover(
		function(){
			$(this).css('color', 'blue');
		},
		function(){
			$(this).css('color', 'white');
		});
});