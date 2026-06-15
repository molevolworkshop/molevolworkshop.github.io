---
layout: applet
title: Group Photo Key 2025
permalink: /group-photos/2025/
---
## Key to people in the 2025 group photo

Mouse-over faces to show names. Please contact [Paul Lewis](paul.lewis@uconn.edu) to report any errors.

<div id="arbitrary"></div>
<script type="text/javascript">
    // written by Paul O. Lewis 10-Aug-2019, last updated 30-May-2025
    
    let production = true; // set to false to work on labeling, true to post
    let randomize_label_positions = false;  // set to true to randomize label positions, false to leave cx,cy as is
    let editable       = production ? false : true; // can't reposition labels in production mode
    let showing_labels = production ? false : true; // labels hidden until moused-over in production mode
    let allow_toggle   = production ? false : true; // toggling between showing and hiding labels not allowed in production mode

    // Usage:
    
    // 1. Set image_file_path
    var image_file_path = "https://molevolworkshop.github.io/assets/img/group-photos/group-photo-2025b.png"
    
    // 2. Specify {"id":0, "first":xxx, "last":yyy, "hide":false, "cx":0, "cy":0} for each person, supplying xxx and yyy
var namedata = [
  {"id":0    , "first":"Mohammed"     , "last":"Ahmed"                 , "hide":false      , "cx":844.0     , "cy":164.0     , "xoffset":0.0       },
  {"id":1    , "first":"Elgin"        , "last":"Akin"                  , "hide":false      , "cx":890.0     , "cy":190.0     , "xoffset":0.0       },
  {"id":2    , "first":"Juan"         , "last":"Albornoz-Garzón"       , "hide":false      , "cx":561.0     , "cy":188.0     , "xoffset":0.0       },
  {"id":3    , "first":"Chinedum"     , "last":"Anajemba"              , "hide":false      , "cx":674.0     , "cy":193.0     , "xoffset":0.0       },
  {"id":4    , "first":"Mihaja"       , "last":"Andriamanohera"        , "hide":false      , "cx":755.5     , "cy":320.5     , "xoffset":0.0       },
  {"id":5    , "first":"Godwin"       , "last":"Ani"                   , "hide":false      , "cx":523.0     , "cy":160.0     , "xoffset":0.0       },
  {"id":6    , "first":"Kathe"        , "last":"Arango-Gomez"          , "hide":false      , "cx":612.0     , "cy":207.0     , "xoffset":0.0       },
  {"id":7    , "first":"Estefany"     , "last":"Argueta Herrera"       , "hide":false      , "cx":593.0     , "cy":217.0     , "xoffset":0.0       },
  {"id":8    , "first":"Sarah"        , "last":"Babaei"                , "hide":false      , "cx":441.0     , "cy":211.0     , "xoffset":0.0       },
  {"id":9    , "first":"Lexi"         , "last":"Baca"                  , "hide":false      , "cx":866.0     , "cy":207.0     , "xoffset":0.0       },
  {"id":10   , "first":"Vilas"        , "last":"Brown"                 , "hide":false      , "cx":309.0     , "cy":171.0     , "xoffset":0.0       },
  {"id":11   , "first":"Ana"          , "last":"Buiatte"               , "hide":false      , "cx":478.0     , "cy":194.0     , "xoffset":0.0       },
  {"id":12   , "first":"Julia"        , "last":"Canitz"                , "hide":false      , "cx":799.0     , "cy":204.0     , "xoffset":0.0       },
  {"id":13   , "first":"Raymond"      , "last":"Castillo"              , "hide":false      , "cx":326.9     , "cy":202.0     , "xoffset":0.0       },
  {"id":14   , "first":"Jimmy"        , "last":"Choi"                  , "hide":false      , "cx":378.0     , "cy":168.0     , "xoffset":0.0       },
  {"id":15   , "first":"Alexis"       , "last":"Culley"                , "hide":false      , "cx":239.0     , "cy":217.0     , "xoffset":0.0       },
  {"id":16   , "first":"Qi"           , "last":"Dai"                   , "hide":false      , "cx":917.0     , "cy":207.0     , "xoffset":0.0       },
  {"id":17   , "first":"Regan"        , "last":"Drennan"               , "hide":false      , "cx":204.0     , "cy":203.0     , "xoffset":0.0       },
  {"id":18   , "first":"Evan"         , "last":"Gorstein"              , "hide":false      , "cx":404.3     , "cy":194.7     , "xoffset":0.0       },
  {"id":19   , "first":"Anik"         , "last":"Grearson"              , "hide":false      , "cx":471.0     , "cy":222.0     , "xoffset":0.0       },
  {"id":20   , "first":"Ericka"       , "last":"Griggs"                , "hide":false      , "cx":202.0     , "cy":180.0     , "xoffset":0.0       },
  {"id":21   , "first":"Haogao"       , "last":"Gu"                    , "hide":false      , "cx":461.0     , "cy":165.0     , "xoffset":0.0       },
  {"id":22   , "first":"Owen"         , "last":"Hale"                  , "hide":false      , "cx":580.0     , "cy":167.0     , "xoffset":0.0       },
  {"id":23   , "first":"Tao"          , "last":"Hernandez Arellano"    , "hide":false      , "cx":796.0     , "cy":170.0     , "xoffset":0.0       },
  {"id":24   , "first":"Bonnie"       , "last":"Heung"                 , "hide":false      , "cx":648.7     , "cy":200.0     , "xoffset":0.0       },
  {"id":25   , "first":"Richard"      , "last":"Hunter"                , "hide":false      , "cx":154.0     , "cy":173.0     , "xoffset":0.0       },
  {"id":26   , "first":"Tori"         , "last":"Jones"                 , "hide":false      , "cx":520.0     , "cy":203.0     , "xoffset":0.0       },
  {"id":27   , "first":"Wonwoong"     , "last":"Kim"                   , "hide":false      , "cx":426.0     , "cy":176.0     , "xoffset":0.0       },
  {"id":28   , "first":"Dan"          , "last":"Land"                  , "hide":false      , "cx":838.0     , "cy":195.0     , "xoffset":0.0       },
  {"id":29   , "first":"Aaron"        , "last":"Lee"                   , "hide":false      , "cx":624.3     , "cy":184.7     , "xoffset":0.0       },
  {"id":30   , "first":"Abigail"      , "last":"Magland"               , "hide":false      , "cx":182.0     , "cy":214.0     , "xoffset":0.0       },
  {"id":31   , "first":"Raja"         , "last":"Narayana Sarma"        , "hide":false      , "cx":468.0     , "cy":320.5     , "xoffset":0.0       },
  {"id":32   , "first":"Thao"         , "last":"Nguyen"                , "hide":false      , "cx":780.0     , "cy":201.0     , "xoffset":0.0       },
  {"id":33   , "first":"Miguel"       , "last":"Pérez-Pérez"           , "hide":false      , "cx":722.0     , "cy":193.0     , "xoffset":0.0       },
  {"id":34   , "first":"Jo"           , "last":"Robertson"             , "hide":false      , "cx":280.0     , "cy":204.0     , "xoffset":0.0       },
  {"id":35   , "first":"Robert"       , "last":"Rolfe"                 , "hide":false      , "cx":251.0     , "cy":171.0     , "xoffset":0.0       },
  {"id":36   , "first":"Rebecka"      , "last":"Sepela"                , "hide":false      , "cx":419.0     , "cy":209.0     , "xoffset":0.0       },
  {"id":37   , "first":"Alex"         , "last":"Shafer"                , "hide":false      , "cx":241.0     , "cy":195.0     , "xoffset":0.0       },
  {"id":38   , "first":"Chiara"       , "last":"Smythies"              , "hide":false      , "cx":704.0     , "cy":204.0     , "xoffset":0.0       },
  {"id":39   , "first":"Rachel"       , "last":"Thayer"                , "hide":false      , "cx":538.0     , "cy":316.5     , "xoffset":0.0       },
  {"id":40   , "first":"Grace"        , "last":"Vaziri"                , "hide":false      , "cx":142.0     , "cy":211.0     , "xoffset":0.0       },
  {"id":41   , "first":"Nickole"      , "last":"Villabona"             , "hide":false      , "cx":607.0     , "cy":317.0     , "xoffset":0.0       },
  {"id":42   , "first":"Juan"         , "last":"Wan"                   , "hide":false      , "cx":528.0     , "cy":231.0     , "xoffset":0.0       },
  {"id":43   , "first":"Joe"          , "last":"Bielawski"             , "hide":false      , "cx":65.0      , "cy":195.0     , "xoffset":0.0       },
  {"id":44   , "first":"Tracy"        , "last":"Heath"                 , "hide":false      , "cx":87.0      , "cy":222.0     , "xoffset":0.0       },
  {"id":45   , "first":"John"         , "last":"Huelsenbeck"           , "hide":false      , "cx":125.0     , "cy":184.0     , "xoffset":0.0       },
  {"id":46   , "first":"Hanon"        , "last":"McShea"                , "hide":false      , "cx":179.0     , "cy":308.0     , "xoffset":0.0       },
  {"id":47   , "first":"Claudia"      , "last":"Solis-Lemus"           , "hide":false      , "cx":254.0     , "cy":309.0     , "xoffset":0.0       },
  {"id":48   , "first":"Bruno"        , "last":"do Rosario Petrucci"   , "hide":false      , "cx":370.0     , "cy":307.5     , "xoffset":0.0       },
  {"id":49   , "first":"Emily Jane"   , "last":"McTavish"              , "hide":false      , "cx":674.0     , "cy":304.0     , "xoffset":0.0       },
  {"id":50   , "first":"Peter"        , "last":"Beerli"                , "hide":false      , "cx":846.5     , "cy":295.5     , "xoffset":0.0       },
  {"id":51   , "first":"Paul"         , "last":"Lewis"                 , "hide":false      , "cx":639.0     , "cy":163.0     , "xoffset":0.0       },
  {"id":52   , "first":"Kevin"        , "last":"Kong"                  , "hide":false      , "cx":739.0     , "cy":171.0     , "xoffset":0.0       },
  {"id":53   , "first":"Jeremy"       , "last":"Brown"                 , "hide":false      , "cx":687.0     , "cy":171.0     , "xoffset":0.0       },
  {"id":54   , "first":"Lacey"        , "last":"Knowles"               , "hide":false      , "cx":751.0     , "cy":201.0     , "xoffset":0.0       },
  {"id":55   , "first":"David"        , "last":"Swofford"              , "hide":false      , "cx":898.0     , "cy":162.0     , "xoffset":0.0       },
  {"id":56   , "first":"Scott"        , "last":"Edwards"               , "hide":false      , "cx":938.0     , "cy":175.0     , "xoffset":0.0       },
  {"id":57   , "first":"Teejay"       , "last":"Adesina"               , "hide":false      , "cx":370.0     , "cy":205.0     , "xoffset":0.0       },
  {"id":58   , "first":"Mandev"       , "last":"Gill"                  , "hide":false      , "cx":349.0     , "cy":192.7     , "xoffset":0.0       },
  {"id":59   , "first":"Caitlin"      , "last":"Randall"               , "hide":false      , "cx":94.0      , "cy":277.0     , "xoffset":0.0       }
];

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
        .attr("fill", "black")
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

