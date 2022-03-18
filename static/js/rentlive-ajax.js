/* TWD pg 301 */

$(document).ready(function(){
	$('.FollowButton').click(function(){
		var propertyNameVar;
		propertyNameVar = $(this).attr('data-categoryid');

		$.get('/rentlive/follow_property',
			{'name': propertyNameVar},
			function(data){
				$('#FollowerCount').html("Followers: " + data);
				$('.FollowButton').hide();
				$('.FollowMessage').html("You have followed this property!");
			})
	})

/* TWD pg 309 */
	$('#QuickSearch').keyup(function(){
		var query;
		query = $(this).val();
		$.get('/rentlive/suggestion/',
			{'suggestion': query},
			function(data){
				$('#CitySearch').html(data);
			})
	});
});