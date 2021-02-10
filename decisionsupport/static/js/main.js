var lat = 0.9887;
var lng = 37.998;
var accessToken = 'pk.eyJ1IjoiZGF1ZGk5NyIsImEiOiJjanJtY3B1bjYwZ3F2NGFvOXZ1a29iMmp6In0.9ZdvuGInodgDk7cv-KlujA';

var map = L.map('map',{
    zoom:11,
    center:{lat: -0.2455, lng: 35.3383}
});

var propertyIcon = L.divIcon({
    className:'property-marker',
    html:""
});

let outdoor = L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token='+ accessToken , {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: accessToken
}).addTo(map);


var landuse = L.geoJSON(null, {
    style:function(feature) {
        return {
            fillColor:getColor(feature),
            weight:0
        }
    }
}).addTo(map);

function getColor(feature) {
    let use = feature.properties ? feature.properties.Type : feature;
    return use == "Plantations" ? "#70fc63" : use == "Forest" ? "#0d8902" : use == "Urban" ? "#f34207" : "#e0cc82";
}


fetch("/static/data/landuse.pbf", { responseType:'ArrayBuffer'})
.then(res => res.arrayBuffer())
.then(data => {
    let geojson =geobuf.decode(new Pbf(data));

    console.log(geojson);
    landuse.addData(geojson);
    filterByYear(1989);
})
.catch(error => {
    console.error(error);
});

// layer control
var overlay = {
    'Land Use':landuse,
};

var baseLayers = {
    "Mapbox Outdoor":outdoor
}

L.control.layers(baseLayers, overlay).addTo(map);

// land use legend
var legendControl = new L.Control({position:"bottomright"});
legendControl.onAdd = function(map) {
    let div = L.DomUtil.create("div", "accordion bg-white");

    div.innerHTML += '<button class="btn btn-block bg-light text-left" type="button" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">'+
    'Land Use Land Cover</button>';
   
    let values = ["Farmlands", "Plantations", "Forest", "Urban"];
    let labels = ["Farmlands", "Plantations", "Forest", "Urban"];

    let legendItems = "";
    values.forEach((value, index) => {
        let color = getColor(value);

        console.log(color);
        let name = labels[index];
        legendItems += "<div class='legend_wrapper'><div class='legend-item' style='background-color:"+color+"'></div><span>"+name+"</span></div>";
    });

    div.innerHTML += '<div class="collapse" id="collapseOne">'+ legendItems +'</div>';

    return div;
}

legendControl.addTo(map);

map.on("overlayadd", function(e) {
    console.log(e);
    if(e.name == "Land Use") {
        legendControl.addTo(map);
    }
});

map.on("overlayremove", function(e) {
    console.log(e);
    if(e.name == "Land Use") {
        map.removeControl(legendControl);
    }
});

function filterByYear(year) {
    landuse.eachLayer(layer => {
        
        layer.setStyle({
            fillOpacity:0.7,
            opacity:1
        });

        if(layer.feature.properties.year != year) {
            // console.log(layer);

            layer.setStyle({
                fillOpacity:0,
                opacity:0
            });
            return;
        }
    });
}


// Year control
$("#year-slider").on("change", function(e) {
    let { value } = e.target;

    console.log(value);
    $("#title-year").text(value);

    filterByYear(parseInt(value));
});


// QUERY TOOL: 