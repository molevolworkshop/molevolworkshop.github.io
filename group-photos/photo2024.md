---
layout: applet
title: Group Photo Key 2024
permalink: /group-photos/2024/
---
## Key to people in the 2024 group photo

Mouse-over faces to show names. Please contact [Paul Lewis](paul.lewis@uconn.edu) to report any errors.

<div id="arbitrary"></div>
<script type="text/javascript">
    // written by Paul O. Lewis 10-Aug-2019, last updated 29-May-2024
    
    let production = true; // set to false to work on labeling, true to post
    let randomize_label_positions = false;  // set to true to randomize label positions, false to leave cx,cy as is
    let editable       = production ? false : true; // can't reposition labels in production mode
    let showing_labels = production ? false : true; // labels hidden until moused-over in production mode
    let allow_toggle   = production ? false : true; // toggling between showing and hiding labels not allowed in production mode

    // Usage:
    
    // 1. Set image_file_path
    var image_file_path = "https://molevolworkshop.github.io/assets/img/group-photos/group-photo-2024.jpg"
    
    // 2. Specify {"id":0, "first":xxx, "last":yyy, "hide":false, "cx":0, "cy":0} for each person, supplying xxx and yyy
    var namedata = [
      {"id":0    , "first":"Kevin"       , "last":"Kong"                  , "hide":false     , "cx":352.3     , "cy":240.0     , "xoffset":0.0       },
      {"id":1    , "first":"Analisa"     , "last":"Milkey"                , "hide":false     , "cx":562.5     , "cy":253.5     , "xoffset":0.0       },
      {"id":2    , "first":"Teejay"      , "last":"Adesina"               , "hide":false     , "cx":616.3     , "cy":309.7     , "xoffset":0.0       },
      {"id":3    , "first":"Bruno"       , "last":"do Rosario Petrucci"   , "hide":false     , "cx":494.5     , "cy":245.0     , "xoffset":0.0       },
      {"id":4    , "first":"Blake"       , "last":"Fauskee"               , "hide":false     , "cx":751.0     , "cy":206.0     , "xoffset":0.0       },
      {"id":5    , "first":"Camryn"      , "last":"Ford"                  , "hide":false     , "cx":337.0     , "cy":219.5     , "xoffset":0.0       },
      {"id":6    , "first":"Mengjin"     , "last":"Zhang"                 , "hide":true      , "cx":210.9     , "cy":38.0      , "xoffset":0.0       },
      {"id":7    , "first":"Eva"         , "last":"Stewart"               , "hide":false     , "cx":382.8     , "cy":221.5     , "xoffset":0.0       },
      {"id":8    , "first":"Neha"        , "last":"Tiwari"                , "hide":false     , "cx":653.3     , "cy":251.5     , "xoffset":0.0       },
      {"id":9    , "first":"Mahdi"       , "last":"Safarpour"             , "hide":true      , "cx":196.9     , "cy":84.0      , "xoffset":0.0       },
      {"id":10   , "first":"Lindsay"     , "last":"Reedy"                 , "hide":false     , "cx":590.6     , "cy":212.0     , "xoffset":0.0       },
      {"id":11   , "first":"Raquel"      , "last":"Pizzardo"              , "hide":false     , "cx":610.0     , "cy":253.7     , "xoffset":0.0       },
      {"id":12   , "first":"Erin"        , "last":"Barnett"               , "hide":false     , "cx":457.0     , "cy":245.0     , "xoffset":0.0       },
      {"id":13   , "first":"Tasia"       , "last":"Bos"                   , "hide":false     , "cx":839.0     , "cy":267.5     , "xoffset":0.0       },
      {"id":14   , "first":"Nicholas"    , "last":"Hubbard"               , "hide":false     , "cx":543.0     , "cy":244.0     , "xoffset":0.0       },
      {"id":15   , "first":"Ivana"       , "last":"Barnes"                , "hide":false     , "cx":685.5     , "cy":329.5     , "xoffset":0.0       },
      {"id":16   , "first":"Lynn"        , "last":"Gu"                    , "hide":false     , "cx":358.0     , "cy":314.0     , "xoffset":0.0       },
      {"id":17   , "first":"Caitlin"     , "last":"Tribelhorn"            , "hide":false     , "cx":545.4     , "cy":356.8     , "xoffset":0.0       },
      {"id":18   , "first":"Meng"        , "last":"Liu"                   , "hide":false     , "cx":741.0     , "cy":265.7     , "xoffset":0.0       },
      {"id":19   , "first":"Hanna"       , "last":"Makowski"              , "hide":false     , "cx":742.5     , "cy":319.5     , "xoffset":0.0       },
      {"id":20   , "first":"Maya"        , "last":"Woolfolk"              , "hide":false     , "cx":414.0     , "cy":321.5     , "xoffset":0.0       },
      {"id":21   , "first":"Josue"       , "last":"Duque"                 , "hide":false     , "cx":706.7     , "cy":239.0     , "xoffset":0.0       },
      {"id":22   , "first":"Phil"        , "last":"Shirk"                 , "hide":false     , "cx":146.0     , "cy":208.7     , "xoffset":0.0       },
      {"id":23   , "first":"Valeria"     , "last":"Ensenta Rivera"        , "hide":false     , "cx":462.0     , "cy":324.0     , "xoffset":0.0       },
      {"id":24   , "first":"Jason"       , "last":"Gallant"               , "hide":false     , "cx":195.0     , "cy":214.7     , "xoffset":0.0       },
      {"id":25   , "first":"Jhan"        , "last":"Salazar"               , "hide":false     , "cx":217.0     , "cy":358.0     , "xoffset":0.0       },
      {"id":26   , "first":"Kathryn"     , "last":"Dickson"               , "hide":false     , "cx":517.7     , "cy":255.0     , "xoffset":0.0       },
      {"id":27   , "first":"Judy"        , "last":"Malas"                 , "hide":false     , "cx":900.5     , "cy":232.0     , "xoffset":0.0       },
      {"id":28   , "first":"Hannah"      , "last":"Verdonk"               , "hide":false     , "cx":493.0     , "cy":213.0     , "xoffset":0.0       },
      {"id":29   , "first":"Claudia"     , "last":"Vaga"                  , "hide":false     , "cx":692.7     , "cy":261.0     , "xoffset":0.0       },
      {"id":30   , "first":"Siena"       , "last":"McKim"                 , "hide":false     , "cx":616.7     , "cy":355.3     , "xoffset":0.0       },
      {"id":31   , "first":"Helen"       , "last":"Stott"                 , "hide":false     , "cx":687.7     , "cy":357.0     , "xoffset":0.0       },
      {"id":32   , "first":"Luke"        , "last":"McCartin"              , "hide":false     , "cx":760.5     , "cy":251.5     , "xoffset":0.0       },
      {"id":33   , "first":"Cody"        , "last":"McCoy"                 , "hide":false     , "cx":291.0     , "cy":219.3     , "xoffset":0.0       },
      {"id":34   , "first":"Samantha"    , "last":"Miranda"               , "hide":false     , "cx":300.5     , "cy":320.0     , "xoffset":0.0       },
      {"id":35   , "first":"Lei"         , "last":"Yang"                  , "hide":false     , "cx":585.5     , "cy":248.3     , "xoffset":0.0       },
      {"id":36   , "first":"Manu"        , "last":"Montoya-Giraldo"       , "hide":false     , "cx":420.0     , "cy":355.0     , "xoffset":0.0       },
      {"id":37   , "first":"Sigournie"   , "last":"Brock"                 , "hide":false     , "cx":490.7     , "cy":359.3     , "xoffset":0.0       },
      {"id":38   , "first":"Monica"      , "last":"Arniella"              , "hide":false     , "cx":848.5     , "cy":227.0     , "xoffset":0.0       },
      {"id":39   , "first":"Anushka"     , "last":"Katikaneni"            , "hide":false     , "cx":810.5     , "cy":243.0     , "xoffset":0.0       },
      {"id":40   , "first":"Vicens"      , "last":"Vila-Coury"            , "hide":false     , "cx":868.0     , "cy":246.5     , "xoffset":0.0       },
      {"id":41   , "first":"Joseph"      , "last":"Kleinkopf"             , "hide":false     , "cx":311.3     , "cy":238.3     , "xoffset":0.0       },
      {"id":42   , "first":"Xinyang"     , "last":"Huang"                 , "hide":false     , "cx":245.5     , "cy":209.0     , "xoffset":0.0       },
      {"id":43   , "first":"Alanna"      , "last":"Fulkerson"             , "hide":false     , "cx":164.0     , "cy":257.7     , "xoffset":0.0       },
      {"id":44   , "first":"Peter"       , "last":"Campbell"              , "hide":false     , "cx":917.3     , "cy":249.0     , "xoffset":0.0       },
      {"id":45   , "first":"Axl"         , "last":"Cepeda"                , "hide":false     , "cx":101.0     , "cy":254.7     , "xoffset":0.0       },
      {"id":46   , "first":"Luke"        , "last":"Arnce"                 , "hide":false     , "cx":637.3     , "cy":209.5     , "xoffset":0.0       },
      {"id":47   , "first":"Nadir"       , "last":"Dbouk"                 , "hide":false     , "cx":451.0     , "cy":212.0     , "xoffset":0.0       },
      {"id":48   , "first":"Rishabh"     , "last":"Kapoor"                , "hide":false     , "cx":904.0     , "cy":315.0     , "xoffset":0.0       },
      {"id":49   , "first":"Jake"        , "last":"Gorneau"               , "hide":false     , "cx":541.5     , "cy":205.0     , "xoffset":0.0       },
      {"id":50   , "first":"Yuanyuan"    , "last":"Ji"                    , "hide":false     , "cx":788.0     , "cy":257.8     , "xoffset":0.0       },
      {"id":51   , "first":"Wendy"       , "last":"Applequist"            , "hide":false     , "cx":631.0     , "cy":241.5     , "xoffset":0.0       },
      {"id":52   , "first":"Mandev"      , "last":"Gill"                  , "hide":false     , "cx":670.3     , "cy":231.0     , "xoffset":0.0       },
      {"id":53   , "first":"David"       , "last":"Swofford"              , "hide":false     , "cx":131.7     , "cy":243.8     , "xoffset":0.0       },
      {"id":54   , "first":"Laura"       , "last":"Kubatko"               , "hide":false     , "cx":796.5     , "cy":220.0     , "xoffset":0.0       },
      {"id":55   , "first":"Megan"       , "last":"Smith"                 , "hide":false     , "cx":278.0     , "cy":257.5     , "xoffset":0.0       },
      {"id":56   , "first":"Peter"       , "last":"Beerli"                , "hide":false     , "cx":189.0     , "cy":249.7     , "xoffset":0.0       },
      {"id":57   , "first":"Lacey"       , "last":"Knowles"               , "hide":false     , "cx":212.0     , "cy":254.7     , "xoffset":0.0       },
      {"id":58   , "first":"Jeremy"      , "last":"Brown"                 , "hide":false     , "cx":697.3     , "cy":211.8     , "xoffset":0.0       },
      {"id":59   , "first":"Scott"       , "last":"Edwards"               , "hide":false     , "cx":249.0     , "cy":229.5     , "xoffset":0.0       },
      {"id":60   , "first":"John"        , "last":"Huelsenbeck"           , "hide":false     , "cx":412.0     , "cy":228.0     , "xoffset":0.0       },
      {"id":61   , "first":"Claudia"     , "last":"Solís-Lemus"           , "hide":false     , "cx":362.5     , "cy":353.0     , "xoffset":0.0       },
      {"id":62   , "first":"Tracy"       , "last":"Heath"                 , "hide":false     , "cx":290.0     , "cy":361.0     , "xoffset":0.0       },
      {"id":63   , "first":"Paul"        , "last":"Lewis"                 , "hide":false     , "cx":131.1     , "cy":357.0     , "xoffset":0.0       },
      {"id":64   , "first":"Joe"         , "last":"Bielawski"             , "hide":false     , "cx":62.0      , "cy":246.7     , "xoffset":0.0       },
      {"id":65   , "first":"Belinda"     , "last":"Chang"                 , "hide":true      , "cx":0.0       , "cy":0.0       , "xoffset":0.0       },
      {"id":66   , "first":"Emily"       , "last":"Jane Mctavish"         , "hide":true      , "cx":0.0       , "cy":0.0       , "xoffset":0.0       },
      {"id":67   , "first":"Corrie"      , "last":"Moreau"                , "hide":true      , "cx":0.0       , "cy":0.0       , "xoffset":0.0       }
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

