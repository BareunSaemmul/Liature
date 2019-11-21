function init()
        {
            window.navigator.geolocation.getCurrentPosition(current_position);
        }
        
        function current_position(position)
        {
            var latlng = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
            
            var map_options = {
                center:latlng,zoom:14,
                mapTypeId:google.maps.MapTypeId.ROADMAP,
                mapTypeControl:false,
                navigationControlOptions:{style:google.maps.NavigationControlStyle.SMALL}
            }
            
            var map = new google.maps.Map(document.getElementById("google_map"), map_options);
            
            var marker = new google.maps.Marker({position:latlng,map:map,title:"You are here!"});

            var infowindow = new google.maps.InfoWindow({
            content:"Hello World!"
            });
            
            google.maps.event.addListener(marker, 'click', function() {
            infowindow.open(map,marker);
            });
        }
        window.addEventListener("load", init);