
//Google Maps JS
//Set Map
function initialize() {
    var myLatlng = new google.maps.LatLng(7.3697, 12.3547);
    var mapOptions = {
        zoom: 11,
        center: myLatlng,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    }

    var map = new google.maps.Map(document.getElementById('map'), mapOptions);

    //Resize Function
    google.maps.event.addDomListener(window, "resize", function() {
        var center = map.getCenter();
        google.maps.event.trigger(map, "resize");
        map.setCenter(center);
    });
}

google.maps.event.addDomListener(window, 'load', initialize);

