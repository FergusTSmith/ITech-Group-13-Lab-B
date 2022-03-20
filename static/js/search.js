
/* The three gotodata() functions deal with the search bars on the search page, and return the correct url */
function gotodata(){

    window.location.href="/rentlive/search/results/?search="+$("#search-input").val()
}
function gotodata1(){

    window.location.href="/rentlive/search/results1/?search="+$("#search-input2").val()
}
function gotodata2(){
	window.location.href="/rentlive/search/propertyresult/?search="+$("#search-input3").val()
}

/* The below handles the rendering of the Google Maps API, and displays some example markers for the properties in the population script. This was sourced on the 20/03/2020 and adapted from https://javascript.plainenglish.io/add-custom-markers-with-the-google-maps-javascript-api-43e8b83f4f7d */
function initMap(){
	var options = {
		zoom:5,
		center:{lat:55.8642, lng:-4.2518}
	}
	var map = new google.maps.Map(document.getElementById('map'), options);
	var marker = new google.maps.Marker({
   		position:{lat: 55.870403, lng:-4.263236}, // Brooklyn Coordinates
  		 map:map //Map that we need to add
  		});
	var marker2 = new google.maps.Marker({
		position:{lat: 55.860577, lng: -4.279727},
		map:map
		});
	var marker3 = new google.maps.Marker({
		position:{lat: 55.924096, lng: -3.216024},
		map:map
	})
	var marker4 = new google.maps.Marker({
		position:{lat: 55.960215, lng: -3.173376},
		map:map
	})
	var marker5 = new google.maps.Marker({
		position:{lat: 55.941981, lng: -3.208809},
		map:map
	})

	var marker6 = new google.maps.Marker({
		position:{lat: 55.069946, lng: -3.607992}
	})

	var information1 = new google.maps.InfoWindow({content: '<h4>321 Fake Av</h4>'});
	marker.addListener('click', function() {information.open(map, marker);});

	var information2 = new google.maps.InfoWindow({content: '<h4>445 Unreal St'});
	marker2.addListener('click', function() {information2.open(map, marker2);});

	var information3 = new google.maps.InfoWindow({content: '<h4>321 Fake Av</h4>'});
	marker3.addListener('click', function() {information3.open(map, marker3);});

	var information4 = new google.maps.InfoWindow({content: '<h4>745 Henderson Row</h4>'});
	marker4.addListener('click', function() {information4.open(map, marker4);});

	var information5 = new google.maps.InfoWindow({content: '<h4>155 Fake Row</h4>'});
	marker5.addListener('click', function() {information5.open(map, marker5);});
}





