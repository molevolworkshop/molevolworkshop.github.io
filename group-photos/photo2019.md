---
layout: applet
title: Group Photo Key 2019
permalink: /group-photos/2019/
---
## Key to people in the 2019 group photo

Mouse over faces to show names. Return to [group photos index](/group-photos/) page.

<div id="arbitrary"></div>
<script type="text/javascript">
    // written by Paul O. Lewis 10-Aug-2019

    // Usage:
    
    // 1. Set image_file_path
    var image_file_path = "https://molevol.mbl.edu/images/f/f9/Group-photo-2019-cropped.png"
    
    // 2. Uncomment namedata object below and comment out later redefinition of namedata
    /*var namedata = [                                                                // Slack names
        {"id":0,  "hide":false, "first":"Sandra", "last":"Almanza"},
        {"id":1,  "hide":false, "first":"Thais", "last":"Almeida"},
        {"id":2,  "hide":false, "first":"Lucia", "last":"Alvares"},
        {"id":3,  "hide":true, "first":"Silvia", "last":"Andrade Justi"},           // Silvinhajusti (YES)
        {"id":4,  "hide":false, "first":"Babak", "last":"Babakinejad"},
        {"id":5,  "hide":false, "first":"Stephen", "last":"Baca"},
        {"id":6,  "hide":false, "first":"Marlise", "last":"Bartholomei-Santos"},
        {"id":7,  "hide":false, "first":"Robert", "last":"Boria"},
        {"id":8,  "hide":false, "first":"Lisa", "last":"Byrne"},
        {"id":9,  "hide":false, "first":"Feng", "last":"Cai"},
        {"id":10, "hide":false, "first":"Daniel", "last":"Castaneda Mogollon"},
        {"id":11, "hide":false, "first":"Susette Sami", "last":"Castaneda Rico"},
        {"id":12, "hide":false, "first":"Daniel", "last":"Cowan-Turner"},
        {"id":13, "hide":false, "first":"Damian", "last":"Dudka"},
        {"id":14, "hide":true, "first":"Elisabeth", "last":"Forrestel"},            // ejforrestel
        {"id":15, "hide":false, "first":"Eva", "last":"Fortea"},
        {"id":16, "hide":false, "first":"Leandro", "last":"Giacomin"},
        {"id":17, "hide":false, "first":"Connie", "last":"Gibas"},
        {"id":18, "hide":true, "first":"Karn", "last":"Imwattana"},                 // Karn Imwattana (YES)
        {"id":19, "hide":false, "first":"Fernanda", "last":"Iruegas Bocardo"},
        {"id":20, "hide":false, "first":"Conrad", "last":"Izydorczyk"},
        {"id":21, "hide":false, "first":"Gregory", "last":"Jongsma"},
        {"id":22, "hide":false, "first":"Veda", "last":"Khadka"},
        {"id":23, "hide":false, "first":"Tara", "last":"Khodaei"},     // was "first":"Marzieh", "last":"Khodaei Gheshlagh"
        {"id":24, "hide":false, "first":"Kip", "last":"Lacy"},
        {"id":25, "hide":false, "first":"Emma", "last":"Larkin-Gero"},
        {"id":26, "hide":true, "first":"Alexander", "last":"Lewanski"},             // Alewansk
        {"id":27, "hide":false, "first":"Duckhyun", "last":"Lhee"},
        {"id":28, "hide":false, "first":"Jenna", "last":"Lin"},
        {"id":29, "hide":false, "first":"Paulo", "last":"Manrique Valverde"},
        {"id":30, "hide":false, "first":"Evan", "last":"Mee"},
        {"id":31, "hide":false, "first":"Spencer", "last":"Monckton"},
        {"id":32, "hide":false, "first":"Sarah", "last":"Nadeau"},
        {"id":33, "hide":false, "first":"Nicole", "last":"Nakata"},
        {"id":34, "hide":false, "first":"Joanne", "last":"Odden"},
        {"id":35, "hide":false, "first":"Ekaterina", "last":"Osipova"},
        {"id":36, "hide":false, "first":"Elisa", "last":"Paiva"},
        {"id":37, "hide":false, "first":"Andressa", "last":"Paladini"},
        {"id":38, "hide":false, "first":"Cooper", "last":"Park"},
        {"id":39, "hide":true, "first":"Chris", "last":"Parsons"},                  // Chris Parsons
        {"id":40, "hide":false, "first":"Swellan", "last":"Pinto"},
        {"id":41, "hide":false, "first":"Jackie", "last":"Purdue"},
        {"id":42, "hide":false, "first":"Anthony", "last":"Rivera Barreto"},
        {"id":43, "hide":false,  "first":"Marjan", "last":"Sadeghi"},
        {"id":44, "hide":false, "first":"Omid", "last":"Saleh Ziabari"},
        {"id":45, "hide":true, "first":"jkMichelle", "last":"Shero"},               // Michelle Shero
        {"id":46, "hide":false, "first":"Kum", "last":"Shim"},
        {"id":47, "hide":false, "first":"Bikash", "last":"Shrestha"},
        {"id":48, "hide":false, "first":"Erik", "last":"Tamre"},
        {"id":49, "hide":false, "first":"Shreya", "last":"Vichare"},
        {"id":50, "hide":false, "first":"Quimi", "last":"Vidaurre Montoya"},
        {"id":51, "hide":false, "first":"Brian", "last":"Waldron"},
        {"id":52, "hide":false, "first":"Nathanael", "last":"Walker-Hale"},
        {"id":53, "hide":true, "first":"Emily", "last":"Watts"},                    // Emily Watts (YES)
        {"id":54, "hide":false, "first":"Alaina", "last":"Weinheimer"},
        {"id":55, "hide":false, "first":"Jonathan", "last":"Wells"},
        {"id":56, "hide":false, "first":"Eranga", "last":"Wettewa"},
        {"id":57, "hide":false, "first":"Nayantara", "last":"Wijayanandana"},
        {"id":58, "hide":false, "first":"Kuangyi", "last":"Xu"},
        {"id":59, "hide":false, "first":"Ying", "last":"Yan"},
        {"id":60, "hide":false, "first":"Peter", "last":"Beerli"},
        {"id":61, "hide":false, "first":"Joe", "last":"Bielawski"},
        {"id":62, "hide":true, "first":"Belinda", "last":"Chang"},                  //  (YES)
        {"id":63, "hide":true, "first":"Scott", "last":"Edwards"},                  // Scott Edwards
        {"id":64, "hide":false,  "first":"Laura", "last":"Eme"},
        {"id":65, "hide":false, "first":"Tracy", "last":"Heath"},
        {"id":66, "hide":false, "first":"Mark", "last":"Holder"},
        {"id":67, "hide":true, "first":"John", "last":"Huelsenbeck"},               // John Huelsenbeck
        {"id":68, "hide":true, "first":"Emilia", "last":"Huerta-Sanchez"},          // Emilia (YES)
        {"id":69, "hide":true, "first":"Lacey", "last":"Knowles"},                  // Lacey Knowles
        {"id":70, "hide":false, "first":"Laura", "last":"Kubatko"},
        {"id":71, "hide":false, "first":"Michael", "last":"Landis"},
        {"id":72, "hide":false, "first":"Paul", "last":"Lewis"},
        {"id":73, "hide":false, "first":"Emily Jane", "last":"McTavish"},
        {"id":74, "hide":true, "first":"Minh", "last":"Bui"},                       // not here
        {"id":75, "hide":true, "first":"Claudia", "last":"Solis-Lemus"},            // Claudia Solis-Lemus (YES)
        {"id":76, "hide":false, "first":"David", "last":"Swofford"},
        {"id":77, "hide":false, "first":"Anne", "last":"Yoder"},
        {"id":78, "hide":false, "first":"Deise", "last":"Gonçalves"},
        {"id":79, "hide":false, "first":"Walker", "last":"Pett"},
        {"id":80, "hide":false, "first":"Áki", "last":"Jarl Láruson"},
        {"id":81, "hide":false, "first":"George", "last":"Tiley"},
        {"id":82, "hide":false, "first":"Marlene", "last":"Abouassii"}
    ];*/
    
    // 3. Set production=false, editable=true, showing_labels=true, and allow_toggle=true
    var production     = true;
    var editable       = false;
    var showing_labels = true;
    var allow_toggle   = false;
    
    // 4. Position labels over faces
    
    // 5. Press the 's' key to save label coordinates to the console
    
    // 6. Copy the label coordinates below to define namedata and comment out previous definition of namedata above
    var namedata = [{"id":0, "first":"Sandra", "last":"Almanza", "hide":false, "cx":823.75, "cy":223.75},{"id":1, "first":"Thais", "last":"Almeida", "hide":false, "cx":291.25, "cy":293.75},{"id":2, "first":"Lucia", "last":"Alvares", "hide":false, "cx":680, "cy":203.75},{"id":3, "first":"Silvia", "last":"Andrade Justi", "hide":true, "cx":845, "cy":401.25},{"id":4, "first":"Babak", "last":"Babakinejad", "hide":false, "cx":323.75, "cy":155},{"id":5, "first":"Stephen", "last":"Baca", "hide":false, "cx":487.5, "cy":153.75},{"id":6, "first":"Marlise", "last":"Bartholomei-Santos", "hide":false, "cx":757.5, "cy":208.75},{"id":7, "first":"Robert", "last":"Boria", "hide":false, "cx":286.25, "cy":223.75},{"id":8, "first":"Lisa", "last":"Byrne", "hide":false, "cx":613.75, "cy":190},{"id":9, "first":"Feng", "last":"Cai", "hide":false, "cx":380, "cy":148.75},{"id":10, "first":"Daniel", "last":"Castaneda Mogollon", "hide":false, "cx":735, "cy":223.75},{"id":11, "first":"Susette Sami", "last":"Castaneda Rico", "hide":false, "cx":437.5, "cy":232.5},{"id":12, "first":"Daniel", "last":"Cowan-Turner", "hide":false, "cx":871.25, "cy":205},{"id":13, "first":"Damian", "last":"Dudka", "hide":false, "cx":267.5, "cy":162.5},{"id":14, "first":"Elisabeth", "last":"Forrestel", "hide":true, "cx":235, "cy":462.5},{"id":15, "first":"Eva", "last":"Fortea", "hide":false, "cx":855, "cy":317.5},{"id":16, "first":"Leandro", "last":"Giacomin", "hide":false, "cx":225, "cy":205},{"id":17, "first":"Connie", "last":"Gibas", "hide":false, "cx":585, "cy":248.75},{"id":18, "first":"Karn", "last":"Imwattana", "hide":true, "cx":537.5, "cy":465},{"id":19, "first":"Fernanda", "last":"Iruegas Bocardo", "hide":false, "cx":491.25, "cy":232.5},{"id":20, "first":"Conrad", "last":"Izydorczyk", "hide":false, "cx":778.75, "cy":220},{"id":21, "first":"Gregory", "last":"Jongsma", "hide":false, "cx":63.75, "cy":163.75},{"id":22, "first":"Veda", "last":"Khadka", "hide":false, "cx":460, "cy":213.75},{"id":23, "first":"Tara", "last":"Khodaei", "hide":false, "cx":330, "cy":241.25},{"id":24, "first":"Kip", "last":"Lacy", "hide":false, "cx":123.75, "cy":161.25},{"id":25, "first":"Emma", "last":"Larkin-Gero", "hide":false, "cx":928.75, "cy":232.5},{"id":26, "first":"Alexander", "last":"Lewanski", "hide":true, "cx":613.75, "cy":466.25},{"id":27, "first":"Duckhyun", "last":"Lhee", "hide":false, "cx":831.25, "cy":183.75},{"id":28, "first":"Jenna", "last":"Lin", "hide":false, "cx":402.5, "cy":226.25},{"id":29, "first":"Paulo", "last":"Manrique Valverde", "hide":false, "cx":892.5, "cy":196.25},{"id":30, "first":"Evan", "last":"Mee", "hide":false, "cx":588.75, "cy":187.5},{"id":31, "first":"Spencer", "last":"Monckton", "hide":false, "cx":637.5, "cy":201.25},{"id":32, "first":"Sarah", "last":"Nadeau", "hide":false, "cx":586.25, "cy":221.25},{"id":33, "first":"Nicole", "last":"Nakata", "hide":false, "cx":640, "cy":306.25},{"id":34, "first":"Joanne", "last":"Odden", "hide":false, "cx":751.25, "cy":301.25},{"id":35, "first":"Ekaterina", "last":"Osipova", "hide":false, "cx":705, "cy":220},{"id":36, "first":"Elisa", "last":"Paiva", "hide":false, "cx":326.25, "cy":217.5},{"id":37, "first":"Andressa", "last":"Paladini", "hide":false, "cx":622.5, "cy":223.75},{"id":38, "first":"Cooper", "last":"Park", "hide":false, "cx":463.75, "cy":191.25},{"id":39, "first":"Chris", "last":"Parsons", "hide":true, "cx":475, "cy":466.25},{"id":40, "first":"Swellan", "last":"Pinto", "hide":false, "cx":675, "cy":222.5},{"id":41, "first":"Jackie", "last":"Purdue", "hide":false, "cx":531.25, "cy":208.75},{"id":42, "first":"Anthony", "last":"Rivera Barreto", "hide":false, "cx":845, "cy":207.5},{"id":43, "first":"Marjan", "last":"Sadeghi", "hide":false, "cx":305, "cy":220},{"id":44, "first":"Omid", "last":"Saleh Ziabari", "hide":false, "cx":195, "cy":151.25},{"id":45, "first":"jkMichelle", "last":"Shero", "hide":true, "cx":153.75, "cy":465},{"id":46, "first":"Kum", "last":"Shim", "hide":false, "cx":700, "cy":327.5},{"id":47, "first":"Bikash", "last":"Shrestha", "hide":false, "cx":911.25, "cy":208.75},{"id":48, "first":"Erik", "last":"Tamre", "hide":false, "cx":561.25, "cy":201.25},{"id":49, "first":"Shreya", "last":"Vichare", "hide":false, "cx":368.75, "cy":227.5},{"id":50, "first":"Quimi", "last":"Vidaurre Montoya", "hide":false, "cx":946.25, "cy":208.75},{"id":51, "first":"Brian", "last":"Waldron", "hide":false, "cx":320, "cy":201.25},{"id":52, "first":"Nathanael", "last":"Walker-Hale", "hide":false, "cx":493.75, "cy":198.75},{"id":53, "first":"Emily", "last":"Watts", "hide":true, "cx":62.5, "cy":465},{"id":54, "first":"Alaina", "last":"Weinheimer", "hide":false, "cx":787.5, "cy":303.75},{"id":55, "first":"Jonathan", "last":"Wells", "hide":false, "cx":388.75, "cy":192.5},{"id":56, "first":"Eranga", "last":"Wettewa", "hide":false, "cx":915, "cy":300},{"id":57, "first":"Nayantara", "last":"Wijayanandana", "hide":false, "cx":880, "cy":232.5},{"id":58, "first":"Kuangyi", "last":"Xu", "hide":false, "cx":667.5, "cy":188.75},{"id":59, "first":"Ying", "last":"Yan", "hide":false, "cx":261.25, "cy":211.25},{"id":60, "first":"Peter", "last":"Beerli", "hide":false, "cx":810, "cy":206.25},{"id":61, "first":"Joe", "last":"Bielawski", "hide":false, "cx":198.75, "cy":217.5},{"id":62, "first":"Belinda", "last":"Chang", "hide":true, "cx":806.25, "cy":382.5},{"id":63, "first":"Scott", "last":"Edwards", "hide":true, "cx":941.25, "cy":385},{"id":64, "first":"Laura", "last":"Eme", "hide":false, "cx":252.5, "cy":235},{"id":65, "first":"Tracy", "last":"Heath", "hide":false, "cx":546.25, "cy":227.5},{"id":66, "first":"Mark", "last":"Holder", "hide":false, "cx":496.25, "cy":295},{"id":67, "first":"John", "last":"Huelsenbeck", "hide":true, "cx":912.5, "cy":461.25},{"id":68, "first":"Emilia", "last":"Huerta-Sanchez", "hide":true, "cx":836.25, "cy":495},{"id":69, "first":"Lacey", "last":"Knowles", "hide":true, "cx":933.75, "cy":431.25},{"id":70, "first":"Laura", "last":"Kubatko", "hide":false, "cx":653.75, "cy":202.5},{"id":71, "first":"Michael", "last":"Landis", "hide":false, "cx":746.25, "cy":187.5},{"id":72, "first":"Paul", "last":"Lewis", "hide":false, "cx":405, "cy":295},{"id":73, "first":"Emily Jane", "last":"McTavish", "hide":false, "cx":773.75, "cy":190},{"id":74, "first":"Minh", "last":"Bui", "hide":true, "cx":825, "cy":448.75},{"id":75, "first":"Claudia", "last":"Solis-Lemus", "hide":true, "cx":942.5, "cy":480},{"id":76, "first":"David", "last":"Swofford", "hide":false, "cx":525, "cy":151.25},{"id":77, "first":"Anne", "last":"Yoder", "hide":false, "cx":440, "cy":163.75},{"id":78, "first":"Deise", "last":"Gonçalves", "hide":false, "cx":335, "cy":300},{"id":79, "first":"Walker", "last":"Pett", "hide":false, "cx":718.75, "cy":192.5},{"id":80, "first":"Áki", "last":"Jarl Láruson", "hide":false, "cx":361.25, "cy":196.25},{"id":81, "first":"George", "last":"Tiley", "hide":false, "cx":412.5, "cy":192.5},{"id":82, "first":"Marlene", "last":"Abouassii", "hide":false, "cx":677.5, "cy":248.75}];
    
    // 7. Set production=true, editable=false, and allow_toggle=false
    
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
        let id = 0;
        for (let row = 0; row < 100; row++) {
            for (let col = 0; col < 10; col++) {
                let cx = 25 + 8*col*targetradius;
                let cy = 50;
                namedata[id].cx = cx;
                namedata[id].cy = cy;
                id++;
                if (id == namedata.length)
                    break
            }
            if (id == namedata.length)
                break
        }
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
    //defaultCoordinates();
    
    // Select DIV element already created (see above) to hold SVG
    var plot_div = d3.select("div#arbitrary");

    // Create SVG element
    var plot_svg = plot_div.append("svg")
        .attr("width", w)
        .attr("height", h);
    
    function saveCoordinates() {
        console.log("Note: wscaler and hscaler should both be set to 1.0 if these data are used");
        var s = "var namedata = [";
        for (let i = 0; i < namedata.length; i++) {
            s += "{" + "\"id\":" + namedata[i].id + ", \"first\":\"" + namedata[i].first + "\", \"last\":\"" + namedata[i].last + "\", \"hide\":" + namedata[i].hide + ", \"cx\":" + namedata[i].cx + ", \"cy\":" + namedata[i].cy + "}";
            if (i < namedata.length - 1)
                s += ",";
        }
        s += "];";
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
            d3.select(this).attr("cx", cx).attr("cy", cy);
            d3.select("text#person"+id).attr("x", cx).attr("y", cy - label_spacer);
        })
        .on("end", function(d) {
            var cx = d3.event.x;
            var cy = d3.event.y;
            var id = parseInt(d3.select(this).attr("id"));
            namedata[id].cx = cx;
            namedata[id].cy = cy;
            d3.select(this).attr("cx", cx).attr("cy", cy);
            d3.select("text#person"+id).attr("x", cx).attr("y", cy - label_spacer);
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
        .attr("x", function(d,i) {return namedata[i].cx;})
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
