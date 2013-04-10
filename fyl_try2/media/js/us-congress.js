
$(document).ready(function() {
		
	for (i = 0; i < max;i++) {
		 $("#tweet-"+i).delay(3000*(Math.abs(max-i))).slideDown(600).fadeIn(3000);
	}
	 
})

function initialize() {
		var mapOptions = {
			zoom : 3,
			center : new google.maps.LatLng(41.835265, -87.622279),
			mapTypeId : google.maps.MapTypeId.ROADMAP
		};
		var latLng;
		var marker;

		map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
		for (var i = 0; i < tweetData.length; i++) {
          // var coords = results.features[i].geometry.coordinates;
          latLng = new google.maps.LatLng(parseFloat(tweetData[i][8]),parseFloat(tweetData[i][7]));
          var marker = new google.maps.Marker({
            position: latLng,
            title: tweetData[i][1],
            map: map
          });
          attachPopUpInfo(marker, i);
        }
	}

function attachPopUpInfo(marker, i){
		
          var infowindowContentString = '<div id="infoWindow">'+
				'<div id="example" class="">'+
					'<div class="tweeterific'+tweetData[i][0] +'" id="{{forloop.counter}}" style="display:none;">'+
						'<img width="40" height="40" src='+tweetData[i][3]+'>'+
						'<p class="text">'
							'<span class="username"><a href="http://twitter.com/#!/'+tweetData[i][4]+'">'+tweetData[i][1]+'</a>:</span>'+tweetData[i][2]+'<span ><a href='+tweetData[i][5]+'>'+tweetData[i][0]+'</a></span>'
						'</p></div></div></div>';
		 var tweetWindowContent= '<div id="content">'+
        '<img width="40" height="40" src='+tweetData[i][3]+'>'+
        '<b>'+'<span class="username"><a href="http://twitter.com/#!/'+tweetData[i][4]+'">'+tweetData[i][1]+'</a>:</span>' +'</b>'+
        '<p>'+ tweetData[i][2]+'</p>'+
        '<span><a href='+tweetData[i][5]+'>'+tweetData[i][0]+'</a></span>'+
        '</div>';
          var infowindow = new google.maps.InfoWindow({
          	 content: tweetWindowContent,
          	 size: new google.maps.Size(50,50)
          	 });
          google.maps.event.addListener(marker, 'click', function() {
          	infowindow.open(map,marker);
    		});
	} 
