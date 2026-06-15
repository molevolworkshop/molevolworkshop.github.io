---
layout: applet
title: Group Photo Key 2023
permalink: /group-photos/2023/
---
## Key to people in the 2023 group photo

Mouse-over faces to show names. Please contact [Paul Lewis](paul.lewis@uconn.edu) to report any errors.

<div id="arbitrary"></div>
<script type="text/javascript">
// written by Paul O. Lewis 10-Aug-2019, last updated 2-June-2023

let production = true; // set to false to work on labeling, true to post
let randomize_label_positions = false;  // set to true to randomize label positions, false to leave cx,cy as is
let editable       = production ? false : true; // can't reposition labels in production mode
let showing_labels = production ? false : true; // labels hidden until moused-over in production mode
let allow_toggle   = production ? false : true; // toggling between showing and hiding labels not allowed in production mode

// Usage:

// 1. Set image_file_path
var image_file_path = "https://molevolworkshop.github.io/assets/img/group-photos/group-photo-2023.jpg"

// 2. Specify {"id":0, "first":xxx, "last":yyy, "hide":false, "cx":0, "cy":0} for each person, supplying xxx and yyy
var namedata = [
{"id":0    , "first":"Peter"              , "last":"Beerli"             , "hide":false     , "cx":777.0     , "cy":143.0     , "xoffset":0.0       },
{"id":1    , "first":"Joseph"             , "last":"Bielawski"          , "hide":false     , "cx":710.5     , "cy":107.0     , "xoffset":0.0       },
{"id":2    , "first":"Jeremy"             , "last":"Brown"              , "hide":false     , "cx":730.5     , "cy":122.0     , "xoffset":0.0       },
{"id":3    , "first":"Minh"               , "last":"Bui"                , "hide":false     , "cx":349.0     , "cy":127.0     , "xoffset":0.0       },
{"id":4    , "first":"Scott"              , "last":"Edwards"            , "hide":false     , "cx":935.0     , "cy":125.0     , "xoffset":0.0       },
{"id":5    , "first":"Laura"              , "last":"Eme"                , "hide":false     , "cx":313.0     , "cy":152.0     , "xoffset":0.0       },
{"id":6    , "first":"Tracy"              , "last":"Heath"              , "hide":false     , "cx":325.0     , "cy":268.0     , "xoffset":0.0       },
{"id":7    , "first":"Lacey"              , "last":"Knowles"            , "hide":false     , "cx":253.0     , "cy":145.5     , "xoffset":0.0       },
{"id":8    , "first":"Laura"              , "last":"Kubatko"            , "hide":false     , "cx":746.9     , "cy":161.0     , "xoffset":0.0       },
{"id":9    , "first":"Paul"               , "last":"Lewis"              , "hide":false     , "cx":89.0      , "cy":252.0     , "xoffset":0.0       },
{"id":10   , "first":"Claudia"            , "last":"Solís-Lemus"        , "hide":false     , "cx":173.0     , "cy":262.0     , "xoffset":0.0       },
{"id":11   , "first":"Megan"              , "last":"Smith"              , "hide":false     , "cx":584.0     , "cy":121.0     , "xoffset":0.0       },
{"id":12   , "first":"Edward"             , "last":"Susko"              , "hide":false     , "cx":292.0     , "cy":107.0     , "xoffset":0.0       },
{"id":13   , "first":"David"              , "last":"Swofford"           , "hide":false     , "cx":858.0     , "cy":138.0     , "xoffset":0.0       },
{"id":14   , "first":"Anne"               , "last":"Yoder"              , "hide":false     , "cx":953.0     , "cy":150.0     , "xoffset":0.0       },
{"id":15   , "first":"Blake"              , "last":"Fauskee"            , "hide":false     , "cx":539.0     , "cy":92.0      , "xoffset":0.0       },
{"id":16   , "first":"Kevin (Sungsik)"    , "last":"Kong"               , "hide":false     , "cx":655.0     , "cy":113.0     , "xoffset":0.0       },
{"id":17   , "first":"Analisa"            , "last":"Milkey"             , "hide":false     , "cx":656.0     , "cy":152.0     , "xoffset":0.0       },
{"id":18   , "first":"Jordan"             , "last":"Satler"             , "hide":false     , "cx":787.0     , "cy":101.0     , "xoffset":0.0       },
{"id":19   , "first":"Kate"               , "last":"Taylor"             , "hide":false     , "cx":396.0     , "cy":262.0     , "xoffset":0.0       },
{"id":20   , "first":"Elena"              , "last":"Korte"              , "hide":false     , "cx":715.5     , "cy":155.5     , "xoffset":0.0       },
{"id":21   , "first":"Adetunji(Teejay)"   , "last":"Adesina"            , "hide":false     , "cx":130.0     , "cy":147.0     , "xoffset":0.0       },
{"id":22   , "first":"Avrami"             , "last":"Aharonoff"          , "hide":false     , "cx":686.0     , "cy":147.0     , "xoffset":0.0       },
{"id":23   , "first":"Michael"            , "last":"Alam"               , "hide":false     , "cx":106.0     , "cy":120.0     , "xoffset":0.0       },
{"id":24   , "first":"Aurelia"            , "last":"Balestra"           , "hide":false     , "cx":456.0     , "cy":216.0     , "xoffset":0.0       },
{"id":25   , "first":"Roland"             , "last":"Bamou"              , "hide":false     , "cx":249.0     , "cy":270.0     , "xoffset":0.0       },
{"id":26   , "first":"Charlotte"          , "last":"Benedict"           , "hide":false     , "cx":535.5     , "cy":154.2     , "xoffset":0.0       },
{"id":27   , "first":"Meg"                , "last":"Branine"            , "hide":false     , "cx":189.0     , "cy":130.0     , "xoffset":0.0       },
{"id":28   , "first":"Michael"            , "last":"Chen"               , "hide":false     , "cx":217.0     , "cy":113.5     , "xoffset":0.0       },
{"id":29   , "first":"Blair"              , "last":"Christensen"        , "hide":false     , "cx":381.0     , "cy":213.0     , "xoffset":0.0       },
{"id":30   , "first":"Elizabeth"          , "last":"Flesch"             , "hide":false     , "cx":366.0     , "cy":151.0     , "xoffset":0.0       },
{"id":31   , "first":"Alex"               , "last":"Franzen"            , "hide":false     , "cx":466.0     , "cy":124.0     , "xoffset":0.0       },
{"id":32   , "first":"Keating"            , "last":"Godfrey"            , "hide":false     , "cx":236.5     , "cy":98.0      , "xoffset":0.0       },
{"id":33   , "first":"Emily"              , "last":"Griffith"           , "hide":false     , "cx":820.0     , "cy":140.0     , "xoffset":0.0       },
{"id":34   , "first":"Zihan"              , "last":"Huang"              , "hide":false     , "cx":369.2     , "cy":83.4      , "xoffset":0.0       },
{"id":35   , "first":"Odion"              , "last":"Ikhimiukor"         , "hide":false     , "cx":894.0     , "cy":147.0     , "xoffset":0.0       },
{"id":36   , "first":"Amanda"             , "last":"Ivanoff"            , "hide":false     , "cx":230.0     , "cy":202.0     , "xoffset":0.0       },
{"id":37   , "first":"Cedric"             , "last":"Kamaleson"          , "hide":false     , "cx":699.0     , "cy":74.7      , "xoffset":0.0       },
{"id":38   , "first":"Carlotta"           , "last":"Kück"               , "hide":false     , "cx":542.0     , "cy":264.0     , "xoffset":0.0       },
{"id":39   , "first":"Emma"               , "last":"Lehmberg"           , "hide":false     , "cx":422.0     , "cy":119.0     , "xoffset":0.0       },
{"id":40   , "first":"Polina"             , "last":"Len"                , "hide":false     , "cx":802.0     , "cy":282.0     , "xoffset":0.0       },
{"id":41   , "first":"Yixuan"             , "last":"Li"                 , "hide":false     , "cx":446.0     , "cy":114.0     , "xoffset":0.0       },
{"id":42   , "first":"Giulia"             , "last":"Lin"                , "hide":false     , "cx":607.0     , "cy":273.0     , "xoffset":0.0       },
{"id":43   , "first":"Carly"              , "last":"Lo"                 , "hide":false     , "cx":478.0     , "cy":155.0     , "xoffset":0.0       },
{"id":44   , "first":"Nahui"              , "last":"Medina-Chavez"      , "hide":false     , "cx":499.0     , "cy":101.0     , "xoffset":0.0       },
{"id":45   , "first":"Agustín"            , "last":"Moreira-Saporiti"   , "hide":false     , "cx":302.0     , "cy":76.5      , "xoffset":0.0       },
{"id":46   , "first":"Lydia"              , "last":"Morley"             , "hide":false     , "cx":163.0     , "cy":203.0     , "xoffset":0.0       },
{"id":47   , "first":"Olivia"             , "last":"Morrison"           , "hide":false     , "cx":308.3     , "cy":204.7     , "xoffset":0.0       },
{"id":48   , "first":"Shelby"             , "last":"Moshier"            , "hide":false     , "cx":558.0     , "cy":145.0     , "xoffset":0.0       },
{"id":49   , "first":"Susanne"            , "last":"Reier"              , "hide":false     , "cx":666.0     , "cy":279.0     , "xoffset":0.0       },
{"id":50   , "first":"Chris"              , "last":"Robinson"           , "hide":false     , "cx":632.0     , "cy":82.0      , "xoffset":0.0       },
{"id":51   , "first":"Ulises"             , "last":"Rosas"              , "hide":false     , "cx":64.0      , "cy":137.0     , "xoffset":0.0       },
{"id":52   , "first":"Katie"              , "last":"Sanbonmatsu"        , "hide":false     , "cx":735.0     , "cy":281.5     , "xoffset":0.0       },
{"id":53   , "first":"Avery"              , "last":"Selberg"            , "hide":false     , "cx":423.0     , "cy":151.0     , "xoffset":0.0       },
{"id":54   , "first":"Samyuktha"          , "last":"Senthil"            , "hide":false     , "cx":52.0      , "cy":241.0     , "xoffset":20.0      },
{"id":55   , "first":"Crístían"           , "last":"Sharma"             , "hide":false     , "cx":168.0     , "cy":95.0      , "xoffset":0.0       },
{"id":56   , "first":"Daniel"             , "last":"Sultanov"           , "hide":false     , "cx":625.5     , "cy":146.7     , "xoffset":0.0       },
{"id":57   , "first":"Tommy"              , "last":"TraversCook"        , "hide":false     , "cx":574.0     , "cy":83.0      , "xoffset":0.0       },
{"id":58   , "first":"Alexa"              , "last":"Tyszka"             , "hide":false     , "cx":601.3     , "cy":145.0     , "xoffset":0.0       },
{"id":59   , "first":"Yee-Ann"            , "last":"Wong"               , "hide":false     , "cx":457.0     , "cy":268.0     , "xoffset":0.0       }
];

// {"id":33   , "first":"Joshua                                             ", "last":"Doby                                                  ", "hide":false     , "cx":64.0      , "cy":359.0     },
//  {"id":38   , "first":"Akacia                                             ", "last":"Halliday-Isaac                                        ", "hide":false     , "cx":88.0      , "cy":404.0     },
//  {"id":49   , "first":"Leticia                                            ", "last":"MagpaliMouraEstevao                                   ", "hide":false     , "cx":224.0     , "cy":363.0     },
//  {"id":51   , "first":"Daniel                                             ", "last":"MendezAranda                                          ", "hide":false     , "cx":246.0     , "cy":401.7     },
//  {"id":59   , "first":"Mahdi                                              ", "last":"Safarpour                                             ", "hide":false     , "cx":411.3     , "cy":361.7     },
//  {"id":64   , "first":"Philip                                             ", "last":"Shirk                                                 ", "hide":false     , "cx":407.3     , "cy":403.7     },
//  {"id":8    , "first":"John                                               ", "last":"Huelsenbeck                                           ", "hide":false     , "cx":936.5     , "cy":431.5     },
//  {"id":4    , "first":"Belinda                                            ", "last":"Chang                                                 ", "hide":false     , "cx":937.0     , "cy":388.0     },
//  {"id":12   , "first":"Emily Jane                                         ", "last":"McTavish                                              ", "hide":false     , "cx":935.0     , "cy":349.0     },


let nnames = namedata.length;
console.log("Number of names: " + nnames);

// 3. Set production=false above (this will set editable=true, showing_labels=true, and allow_toggle=true)

// 4. Position labels over faces

// 5. Press the 's' key to save label coordinates to the console

// 6. Use what has been spit out to the console to replace the definition of namedata above

// 7. Set production=true (sets editable=false, showing_labels=false, and allow_toggle=false)

// 8. Copy this file to server that can serve javascript

// width and height of svg
var w = 1000;
var h = 500;

var wscaler = 1.0;   // only change this if you change w to rescale all target coordinates
var hscaler = 1.0;   // only change this if you change h to rescale all target coordinates

var label_spacer = 15;
var labelsize = 14;
var targetradius = 10;
var targethiddencolor  = d3.rgb(255,255,255, editable ? 0.3 : 0.0);
var targetvisiblecolor = d3.rgb(255,255,255, 0.3)
            
function defaultCoordinates() {
    // choose x,y coordinates of labels uniformly within a rectangle
    // having 15% smaller width and height
    let boxw = 0.85*w;
    let boxh = 0.85*h;
    for (let id = 0; id < nnames; id++) {
        namedata[id].cx = Math.random()*boxw;
        namedata[id].cy = Math.random()*boxh;
        //console.log("id = " + id + ", cx = " + namedata[id].cx.toFixed(1) + ", cy = " + namedata[id].cy.toFixed(1));
    }
    //let nrows = Math.floor(1 + nnames/10)
    //console.log("Number of rows: " + nrows);
    //for (let row = 0; row < nrows; row++) {
    //    for (let col = 0; col < 10; col++) {
    //        let cx = 25 + 8*col*targetradius;
    //        let cy = 0.2*h + row*(0.75*h)/nrows;
    //        namedata[id].cx = cx;
    //        namedata[id].cy = cy;
    //        //console.log("id = " + id + ", cx = " + cx.toFixed(3) + ", cy = " + cy.toFixed(3));
    //        id++;
    //        if (id == namedata.length)
    //            break
    //    }
    //    if (id == namedata.length)
    //        break
    //}
}

if (wscaler != 1.0) {
    for (let i = 0; i < namedata.length; i++) {
        namedata[i].cx *= wscaler;
    }
}

if (hscaler != 1.0) {
    for (let i = 0; i < namedata.length; i++) {
        namedata[i].cy *= hscaler;
    }
}

if (randomize_label_positions)
    defaultCoordinates();

// Select DIV element already created (see above) to hold SVG
var plot_div = d3.select("div#arbitrary");

// Create SVG element
var plot_svg = plot_div.append("svg")
    .attr("width", w)
    .attr("height", h);

function saveCoordinates() {
    console.log("Note: wscaler and hscaler should both be set to 1.0 if these data are used");
    
    // Find maximum length of first names and last names
    let max_first = 0;
    let max_last = 0;
    for (let i = 0; i < namedata.length; i++) {
        if (namedata[i].first.length > max_first)
            max_first = namedata[i].first.length;
        if (namedata[i].last.length > max_last)
            max_last = namedata[i].last.length;
    }                
    max_first += 5;
    max_last += 5;
    
    var s = "var namedata = [\n";
    for (i = 0; i < namedata.length; i++) {
        let idstr      = namedata[i].id.toFixed(0);
        let firststr   = "\"" + namedata[i].first + "\"";
        let laststr    = "\"" + namedata[i].last + "\"";
        let hidestr    = namedata[i].hide ? "true" : "false";
        let cxstr      = namedata[i].cx.toFixed(1);
        let cystr      = namedata[i].cy.toFixed(1);
        let xoffsetstr = namedata[i].xoffset.toFixed(1);
        s += "  {" + "\"id\":" + idstr.padEnd(5, " ") + ", \"first\":" + firststr.padEnd(max_first, " ") + ", \"last\":" + laststr.padEnd(max_last, " ") + ", \"hide\":" + hidestr.padEnd(10, " ") + ", \"cx\":" + cxstr.padEnd(10, " ") + ", \"cy\":" + cystr.padEnd(10, " ") + ", \"xoffset\":" + xoffsetstr.padEnd(10, " ") + "}";
        if (i < namedata.length - 1)
            s += ",\n";
        else
            s += "\n";
    }
    s += "];\n";
    console.log(s);
}

function toggleLabels() {
    if (!allow_toggle)
        return; 
    if (showing_labels) {
        //console.log("turning off labels");
        d3.selectAll("text.label").style("visibility", "hidden");
        d3.selectAll("circle.target").style("visibility", "hidden");
        showing_labels = false;
    }
    else {
        //console.log("turning on labels");
        d3.selectAll("text.label").style("visibility", function(d) {return d.hide ? "hidden" : "visible";});
        d3.selectAll("circle.target").style("visibility", function(d) {return d.hide ? "hidden" : "visible";});
        showing_labels = true;
    }
}

// Create drag behavior
var drag = d3.drag()
    .on("start", function(d) {
        d3.event.sourceEvent.stopPropagation();
        d3.select(this).classed("dragging", true);
    })
    .on("drag", function(d) {
        var cx = d3.event.x;
        var cy = d3.event.y;
        var id = parseInt(d3.select(this).attr("id"));
        namedata[id].cx = cx;
        namedata[id].cy = cy;
        d3.select(this)
            .attr("cx", cx)
            .attr("cy", cy);
        d3.select("text#person"+id)
            .attr("x", cx + d.xoffset)
            .attr("y", cy - label_spacer);
    })
    .on("end", function(d) {
        var cx = d3.event.x;
        var cy = d3.event.y;
        console.log("cx = " + cx + ", cy = " + cy);
        var id = parseInt(d3.select(this).attr("id"));
        namedata[id].cx = cx;
        namedata[id].cy = cy;
        d3.select(this).attr("cx", cx).attr("cy", cy);
        d3.select("text#person"+id).attr("x", cx + d.xoffset).attr("y", cy - label_spacer);
    });
    
// Listen and react to keystrokes
function keyDown() {
    //console.log("key was pressed: " + d3.event.keyCode);
    if (d3.event.keyCode == 83) {
        // 83 is the "s" key
        saveCoordinates();
    } 
    else if (d3.event.keyCode == 84) {
        // 84 is the "t" key
        toggleLabels();
    }
}
d3.select("body")
    .on("keydown", keyDown);

plot_svg.append("image")
    .attr("xlink:href", function(d) {return image_file_path;})
    .attr("x", 0)
    .attr("y", 0)
    .attr("width", w)
    .attr("height", h);
    
// Create rect outlining entire area of SVG
plot_svg.append("rect")
    .attr("x", 0)
    .attr("y", 0)
    .attr("width", w)
    .attr("height", h)
    .attr("fill", "none")
    .attr("stroke", "orange")
    .attr("stroke-width", 15)
    .style("visibility", "hidden");
    
var targets = plot_svg.selectAll("circle.target")
    .data(namedata)
    .enter()
    .append("circle")
    .attr("id", function(d) {return d.id;})
    .attr("class", "target")
    .attr("cx", function(d) {return d.cx;})
    .attr("cy", function(d) {return d.cy;})
    .attr("r", targetradius)
    .attr("fill", production ? targethiddencolor : targetvisiblecolor)
    .attr("stroke", "none")
    //.style("visibility", function(d) {console.log(namedata[d.id].last + (d.hide ? " (hidden)" : " (shown)")); return d.hide ? "hidden" : "visible";})
    .style("visibility", function(d) {return d.hide ? "hidden" : "visible";})
    .on("mouseover", handleMouseOver)
    .on("mouseout", handleMouseOut);
    
if (editable)                
    plot_svg.selectAll("circle.target").call(drag);
    
var labels = plot_svg.selectAll("text.label")
    .data(namedata)
    .enter()
    .append("text")
    .attr("id", function(d,i) {return "person" + d.id;})
    .attr("class", "label")
    .attr("x", function(d,i) {return namedata[i].cx + namedata[i].xoffset;})
    .attr("y", function(d,i) {return namedata[i].cy - label_spacer;})
    .attr("fill", "white")
    .style("text-anchor", "middle")
    .style("pointer-events", "none")   // don't intercept drag events
    .attr("font-family", "Verdana")
    .attr("font-size", labelsize)
    .style("visibility", function(d) {return (production || d.hide) ? "hidden" : "visible";})
    .text(function(d) {return d.first + " " + d.last;});

function handleMouseOver(d, i) { 
    let id = parseInt(d3.select(this).attr("id"));
    d3.select(this).attr("fill", targetvisiblecolor).style("visibility", d.hide ? "hidden" : "visible");
    d3.select("text#person" + id).style("visibility", function(d) {return d.hide ? "hidden" : "visible";});
}

function handleMouseOut(d, i) {
    let id = parseInt(d3.select(this).attr("id"));
    d3.select(this).attr("fill", production ? targethiddencolor : targetvisiblecolor)
        .style("visibility", d.hide ? "hidden" : "visible");
    d3.select("text#person" + id).style("visibility", (production || d.hide) ? "hidden" : "visible");
}
</script>

Go to [group photos index](/other/) page.

