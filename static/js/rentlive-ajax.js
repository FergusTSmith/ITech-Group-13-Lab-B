/* The following functions are adapted from the example AJAX functions given in Tango With Django page 301 - retrieved 17/03/2020 */

/* If user clicks follow button on a rental property page */
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

	/* This concerns a user liking a comment on a Property page */
	$('.LikeButton').click(function(){
		var commentID;
		commentID = $(this).attr('data-categoryid');

		$.get('/rentlive/likecomment/',
			{'commentID': commentID},
			function(data){
				$('#likes').html("Likes: " + data);
				$('.LikeButton').hide();
				$('.likemessage').html("You have liked this comment");
			})
	})
	/* This concerns a user liking a comment on an Agent page */


	$('.AgentLikeButton').click(function(){
		var commentID;
		commentID = $(this).attr('data-categoryid')

		$.get('/rentlive/likeagentcomment/',
			{'commentID': commentID},
			function(data){
				$('#agentLikes').html("Likes: " + data);
				$('.AgentLikeButton').hide();
				$('#Agentlikemessage').html("You have liked this comment");
			})
	})
	/* Allows city suggestions to pop up for the user */
	/* This function was adapted from a simular function in Tango With Django page 309 */
	$('#QuickSearch').keyup(function(){
		var query;
		query = $(this).val();
		$.get('/rentlive/suggestion/',
			{'suggestion': query},
			function(data){
				$('#CitySearch').html(data);
			})
	});

	/* Shows the properties a user has followed */
	$('#Followed').click(function(){
		var user;
		user = $(this).attr('data-categoryid');
		$('#ProfileContent').empty();
		$.get('/rentlive/follows/',
			function(data){
				$('#ProfileContent').html(data);
			})
	});

	/* Shows the messages a user has received */
	$('#MyMessage').click(function(){
		var user;
		user = $(this).attr('data-categoryid')
		$('#ProfileContent').empty();
		$.get('/rentlive/showmessages/',
			function(data){
				$('#ProfileContent').html(data);
			})
	})

	/* Shows the comments I have left */
	$('#MyComments').click(function(){
		$.get('/rentlive/showcomments',
			function(data){
				$('#ProfileContent').html(data);
			})
	})

	/* Loads the comment posting form */
	$('#CommentButton').click(function(){
		var user;
		user=$(this).attr('data-categoryid')
		$.get('/rentlive/addcomment/',
			function(data){
				$('#commentform').html(data);
			})
	})

	/* Loads the comment posting form for an agent page */
	$('#AgentComment').click(function(){
		var user;
		user=$(this).attr('data-categoryid')
		$.get('/rentlive/agentcomment/',
			function(data){
				$('#AgCommentForm').html(data);
			})
	})

	/* Gets the send message form for the user to send a message */
	$('#SendMessage').click(function(){
		$('#ProfileContent').empty();
		$.get('/rentlive/message/',
			function(data){
				$('#ProfileContent').html(data);
			})
	})

	/* User actually sends a message */
	$('#MessageSending').click(function(){
		$('#ProfileContent').empty();
		$.get('/rentlive/sent/',
			function(data){
				$('#ProfileContent').html(data);
			})
	})




});