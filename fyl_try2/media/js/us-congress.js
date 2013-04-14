
$(document).ready(function() {
		
	for (i = 0; i < max;i++) {
		 $("#tweet-"+i).delay(3000*(Math.abs(max-i))).slideDown(600).fadeIn(3000);
	}
	 
})
