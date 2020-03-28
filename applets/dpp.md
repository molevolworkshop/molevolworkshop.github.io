---
layout: applet
title: Dirichlet Process Priors
author: Paul O. Lewis
permalink: /applets/dpp/
---
## Dirichlet Process Prior applet
Written by Paul O. Lewis (27-Mar-2020)

A description of this applet is provided below the plot.

<div id="arbitrary" style="display:inline-block"></div>
<div id="controls" style="display:inline-block; vertical-align:top;"></div>
<script type="text/javascript">
    // written by Paul O. Lewis 27-Mar-2020
    // See https://developer.mozilla.org/en-US/docs/Web/SVG/Element
    // See https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute

    const lot = new Random(1234);
    
    // width and height of svg
    const w          = 600;
    const h          = 600;
    const labelw     =  90;
    const xhist      = 100;
    const whist      = 300;
    const xgzero     = 425;
    const wgzero     = 150;
    const hgzero     = 150;
    const ngzerobins = 30;
    const xinfo      = 500;
    const infopad    = 50;
    
    const color_alloc_hist = "navy";
    
    let alpha        = 2;      // concentration parameter
    let alphamin     = 0.1
    
    let maxflips     = 2000;   // maximum number of coinflips allowed
    
    let prior_a      = 2;      // G0 is Beta(prior_a, prior_b)
    let prior_b      = 2;
                
    const iteration_milisecs = 10;
    let iterating = false;
    
    let configurations = [
        {partition:"ABCD",    sets:[[0,1,2,3]]},
        {partition:"ABC|D",   sets:[[0,1,2],[3]]},
        {partition:"ABD|C",   sets:[[0,1,3],[2]]},
        {partition:"AB|CD",   sets:[[0,1],[2,3]]},
        {partition:"AB|C|D",  sets:[[0,1],[2],[3]]},
        {partition:"ACD|B",   sets:[[0,2,3],[1]]},
        {partition:"AC|BD",   sets:[[0,2],[1,3]]},
        {partition:"AC|B|D",  sets:[[0,2],[1],[3]]},
        {partition:"AD|BC",   sets:[[0,3],[1,2]]},
        {partition:"A|BCD",   sets:[[0],[1,2,3]]},
        {partition:"A|BC|D",  sets:[[0],[1,2],[3]]},
        {partition:"AD|B|C",  sets:[[0,3],[1],[2]]},
        {partition:"A|BD|C",  sets:[[0],[1,3],[2]]},
        {partition:"A|B|CD",  sets:[[0],[1],[2,3]]},
        {partition:"A|B|C|D", sets:[[0],[1],[2],[3]]}
    ];
    
    let longest = 0;
    for (let i = 0; i < 15; i++)
        if (configurations[i].partition.length > longest)
            longest = configurations[i].partition.length;
            
    // ########################################################################
    // ############################### scales  ################################
    // ########################################################################

    const xinfoscale = d3.scaleLinear()
        .domain([0,1])
        .range([xinfo,w]);
        
    const yinfoscale = d3.scaleBand()
        .domain(d3.range(30))
        .range([infopad,h-infopad]);

    const xgzeroscale = d3.scaleBand()
        .domain(d3.range(ngzerobins))
        .range([xgzero,xgzero+wgzero]);

    const ygzeroscale = d3.scaleLinear()
        .domain([0,1])
        .range([575,425]);
        
    const xconfigscale = d3.scaleLinear()
        .domain([0,1])
        .range([0,labelw]);

    const yconfigscale = d3.scaleBand()
        .domain(d3.range(15))
        .range([0,h])
        .padding(0.2);
        
    // ########################################################################
    // ################################ svg  ##################################
    // ########################################################################

    // Select DIV element already created (see above) to hold SVG
    const plot_div = d3.select("div#arbitrary");

    // Create SVG element
    const plot_svg = plot_div.append("svg")
        .attr("width", w)
        .attr("height", h);

    // Create rect outlining entire area of SVG
    plot_svg.append("rect")
        .attr("x", 0)
        .attr("y", 0)
        .attr("width", w)
        .attr("height", h)
        .attr("fill", "lavender");
        
    // Create box showing allocation histogram extent
    plot_svg.append("rect")
        .attr("id", "alloc")
        .attr("x", xhist)
        .attr("y", 0)
        .attr("width", whist)
        .attr("height", h)
        .attr("fill", "none")
        .attr("stroke", "purple")
        .style("visibility", "hidden");
    
    // Create line serving as base of allocation histogram
    plot_svg.append("line")
        .attr("id", "alloc")
        .attr("x1", xhist)
        .attr("y1", 0)
        .attr("x2", xhist)
        .attr("y2", h)
        .attr("fill", "none")
        .attr("stroke", "purple")
        .style("visibility", "visible");
    
    // Create box showing G0 histogram extent
    plot_svg.append("rect")
        .attr("id", "gzero")
        .attr("x", xgzero)
        .attr("y", ygzeroscale(1))
        .attr("width", wgzero)
        .attr("height", hgzero)
        .attr("fill", "none")
        .attr("stroke", "purple")
        .style("visibility", "visible");
    
    // Create vertical line showing where xinfo lies
    plot_svg.append("line")
        .attr("x1", xinfo)
        .attr("y1", 0)
        .attr("x2", xinfo)
        .attr("y2", h)
        .attr("stroke", "orange")
        .style("visibility", "hidden");
    
    // ########################################################################
    // ########################### configurations  ############################
    // ########################################################################

    // Returns the x coordinate of the upper left corner of a configuration box
    function configBoxX(d,i) {
        let textw = 10*d.partition.length;
        return labelw - textw;
    }

    // Returns the y coordinate of the upper left corner of a configuration box
    function configBoxY(d,i) {
        return yconfigscale(i);
    }

    // Returns the width of a configuration box associated with d
    function configBoxW(d,i) {
        return 10*d.partition.length;
    }

    // Returns the height of a configuration box
    function configBoxH(d,i) {
        return yconfigscale.bandwidth();
    }

    // Returns the x coordinate of the center the text string displayed in
    // a configuration box associated with d
    function configTextX(d,i) {
        let textw = 10*d.partition.length;
        return labelw - textw/2;
    }

    // Returns the y coordinate of the lower left corner of the text string
    // displayed in a configuration box associated with d
    function configTextY(d,i) {
        return yconfigscale(i) + (yconfigscale.bandwidth()/2 + 6) + "px";
    }

    // Create rounded rects showing configuration
    plot_svg.selectAll("rect.config")
        .data(configurations)
        .enter()
        .append("rect")
        .attr("class", "config")
        .attr("x", function(d,i) {return configBoxX(d,i);})
        .attr("y", function(d,i) {return configBoxY(d,i);})
        .attr("rx", "10")
        .attr("width", function(d,i) {return configBoxW(d,i);})
        .attr("height", function(d,i) {return configBoxH(d,i);})
        .attr("stroke", "purple")
        .attr("fill", "none");

    // Create text elements showing configuration
    plot_svg.selectAll("text.config")
        .data(configurations)
        .enter()
        .append("text")
        .attr("class", "config")
        .attr("x", function(d,i) {return configTextX(d,i);})
        .attr("y", function(d,i) {return configTextY(d,i);})
        .attr("font-family", "Courier")
        .attr("font-size", "14px")
        .style("text-anchor", "middle")
        .text(function(d) {return d.partition;});
        
    // ###################################################################
    // ########################### coin info  ############################
    // ###################################################################
    let coininfo = [
        {name:"A", y:0, n:0, p:0.5},
        {name:"B", y:0, n:0, p:0.5},
        {name:"C", y:0, n:0, p:0.5},
        {name:"D", y:0, n:0, p:0.5}
    ];
    plot_svg.append("text")
        .attr("id", "alphalabel")
        .attr("x", xinfo)
        .attr("y", yinfoscale(20))
        .attr("font-family", "Verdana")
        .attr("font-size", "14px")
        .style("text-anchor", "end")
        .text("alpha = ");
        
    plot_svg.append("text")
        .attr("id", "alphavalue")
        .attr("x", xinfo + 3)
        .attr("y", yinfoscale(20))
        .attr("font-family", "Verdana")
        .attr("font-size", "14px")
        .style("text-anchor", "begin")
        .text(alpha.toFixed(1));
        
    plot_svg.selectAll("text.coinlabel")
        .data(coininfo)
        .enter()
        .append("text")
        .attr("class", "coinlabel")
        .attr("x", xinfo)
        .attr("y", function(d,i) {return yinfoscale(5*i);})
        .attr("font-family", "Verdana")
        .attr("font-size", "14px")
        .style("text-anchor", "end")
        .text(function(d) {return "coin " + d.name + ":";});
        
    plot_svg.selectAll("text.plabel")
        .data(coininfo)
        .enter()
        .append("text")
        .attr("class", "plabel")
        .attr("x", xinfo)
        .attr("y", function(d,i) {return yinfoscale(5*i+1);})
        .attr("font-family", "Verdana")
        .attr("font-size", "14px")
        .style("text-anchor", "end")
        .text("p = ");
        
    plot_svg.selectAll("text.pvalue")
        .data(coininfo)
        .enter()
        .append("text")
        .attr("class", "pvalue")
        .attr("x", xinfo + 3)
        .attr("y", function(d,i) {return yinfoscale(5*i+1);})
        .attr("font-family", "Verdana")
        .attr("font-size", "14px")
        .style("text-anchor", "begin")
        .text(function(d) {return d.p.toFixed(2);});

    plot_svg.selectAll("text.ylabel")
        .data(coininfo)
        .enter()
        .append("text")
        .attr("class", "ylabel")
        .attr("x", xinfo)
        .attr("y", function(d,i) {return yinfoscale(5*i+2);})
        .attr("font-family", "Verdana")
        .attr("font-size", "14px")
        .style("text-anchor", "end")
        .text("y = ");
        
    plot_svg.selectAll("text.yvalue")
        .data(coininfo)
        .enter()
        .append("text")
        .attr("class", "yvalue")
        .attr("x", xinfo + 3)
        .attr("y", function(d,i) {return yinfoscale(5*i+2);})
        .attr("font-family", "Verdana")
        .attr("font-size", "14px")
        .style("text-anchor", "begin")
        .text(function(d) {return d.y;});

    plot_svg.selectAll("text.nlabel")
        .data(coininfo)
        .enter()
        .append("text")
        .attr("class", "nlabel")
        .attr("x", xinfo)
        .attr("y", function(d,i) {return yinfoscale(5*i+3);})
        .attr("font-family", "Verdana")
        .attr("font-size", "14px")
        .style("text-anchor", "end")
        .text("n = ");

    plot_svg.selectAll("text.nvalue")
        .data(coininfo)
        .enter()
        .append("text")
        .attr("class", "nvalue")
        .attr("x", xinfo + 3)
        .attr("y", function(d,i) {return yinfoscale(5*i+3);})
        .attr("font-family", "Verdana")
        .attr("font-size", "14px")
        .style("text-anchor", "begin")
        .text(function(d) {return d.n;});

    function updateInfo() {
        plot_svg.select("text#alphavalue")
            .text(alpha.toFixed(1));
        plot_svg.selectAll("text.pvalue")
            .data(coininfo)
            .text(function(d) {return d.p.toFixed(2);});
        plot_svg.selectAll("text.yvalue")
            .data(coininfo)
            .text(function(d) {return d.y;});
        plot_svg.selectAll("text.nvalue")
            .data(coininfo)
            .text(function(d) {return d.n;});
    }
    
    // ##############################################################
    // ########################### MCMC #############################
    // ##############################################################
    
    let gzero_counts = [];
    let gzero_uppers = [];
    let g0incr = 1.0/ngzerobins;
    let upper = 0.0;
    for (let i = 0; i < ngzerobins; i++) {
        gzero_counts.push(0);
        upper += g0incr;
        gzero_uppers.push(upper);
    }
    
    const config_k     = [1,2,2,2,3,2,2,3,2,2,3,3,3,3,4];
    const config_nfact = [6,2,2,1,1,2,1,1,1,2,1,1,1,1,1];
    let config_prob    = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
    
    function drawFromG0() {
        let a = lot.gamma(prior_a,1);
        let b = lot.gamma(prior_b,1);
        return a/(a+b);
    }
    
    function binGZero(g0) {
        for (let i = 0; i < ngzerobins; i++) {
            if (g0 < gzero_uppers[i]) {
                gzero_counts[i]++;
                break;
            }
        }
    }
    
    function resetGZeroCounts() {
        for (let i = 0; i < ngzerobins; i++) {
            gzero_counts[i] = 0;
        }
    }
    
    // Begin with all four coins in one group
    let phi = [];
    let g0 = drawFromG0();
    binGZero(g0);
    phi.push(g0);
    let allocation = [0,0,0,0]; 

    let total_count = 1;
    let config_counts  = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0];

    function recalcConfigProbs(a) {
        let denom = a*(a+1)*(a+2)*(a+3);
        for (let i = 0; i < 15; i++) {
            config_prob[i] = Math.pow(a,config_k[i])*config_nfact[i]/denom;
        }
    }
    recalcConfigProbs(alpha);
    
    function drawFromPrior() {
        total_count++;
        let cumpr = 0.0;
        let u = lot.uniform(0,1);
        for (let i = 0; i < 15; i++) {
            cumpr += config_prob[i];
            if (u < cumpr) {
                config_counts[i]++;
                break;
            }
        }
    }
    
    plot_svg.selectAll("rect.allochist")
        .data(config_counts)
        .enter()
        .append("rect")
        .attr("class", "allochist")
        .attr("x", xhist)
        .attr("y", function(d,i) {return yconfigscale(i);})
        .attr("width", function(d) {return whist*d/total_count;})
        .attr("height", yconfigscale.bandwidth())
        .attr("fill", function(d) {return "rgb(0, 0, " + calcColor(d, total_count) + ")";});

    function calcColor(d, maxd) {
        return (Math.floor(255.0*d/maxd));
    }
    
    function updateAllocationHistogram() {
        plot_svg.selectAll("rect.allochist")
            .data(config_counts)
            .attr("width", function(d) {return whist*d/total_count;})
            .attr("fill", function(d) {return "rgb(0, 0, " + calcColor(d, total_count) + ")";});
    }
    
    plot_svg.selectAll("rect.gzerohist")
        .data(gzero_counts)
        .enter()
        .append("rect")
        .attr("class", "gzerohist")
        .attr("x", function(d,i) {return xgzeroscale(i);})
        .attr("y", ygzeroscale(0))
        .attr("width", xgzeroscale.bandwidth())
        .attr("height", 0);

    function updateGZeroHistogram() {
        let maxcount = Math.max(...gzero_counts);
        if (maxcount > 0 ) {
            plot_svg.selectAll("rect.gzerohist")
                .data(gzero_counts)
                .attr("y", function(d) {return ygzeroscale(0) - 0.8*hgzero*d/maxcount;})
                .attr("height", function(d) {return 0.8*hgzero*d/maxcount;})
                .attr("fill", function(d) {return "rgb(" + calcColor(d, maxcount) + ", 0, 0)";});
        }
        else {
            plot_svg.selectAll("rect.gzerohist")
                .attr("y", ygzeroscale(0))
                .attr("height", 0);
        }
    }
    
    function isSingleton(i) {
        if (i != 0 && allocation[i] == allocation[0])
            return false;
        if (i != 1 && allocation[i] == allocation[1])
            return false;
        if (i != 2 && allocation[i] == allocation[2])
            return false;
        if (i != 3 && allocation[i] == allocation[3])
            return false;
        return true;
    }
    
    function logLikelihood(y, n, p) {
        let logLike = 0.0;
        logLike += log_gamma(n+1);
        logLike -= log_gamma(y+1);
        logLike -= log_gamma(n-y+1);
        logLike += y*Math.log(p);
        logLike += (n-y)*Math.log(1-p);
        return logLike;
    }

    function calcAllocProbs(i, is_singleton) {
        // Initialize probabilities used to choose a new category for coin i
        let probs = [];
        for (let j = 0; j < phi.length; j++) {
            probs.push(0);
        }
        
        // Set numerator for existing categories
        for (let j = 0; j < 4; j++) {
            if (i != j) {
                probs[allocation[j]]++;
            }
        } 

        // Set numerator for auxilliary categories
        if (is_singleton) {
            probs[allocation[i]] = alpha/3;
            for (let j = phi.length - 2; j < phi.length; j++) {
                probs[j] = alpha/3;
            }
        }
        else {
            for (let j = phi.length - 3; j < phi.length; j++) {
                probs[j] = alpha/3;
            }
        }
        
        // Multiply by coin i likelihood
        let denom = [];
        for (let j = 0; j < phi.length; j++) {
            let logNumer = Math.log(probs[j]);
            if (coininfo[i].n > 0) {
                logNumer += logLikelihood(coininfo[i].y, coininfo[i].n, phi[j]);
            }
            probs[j] = logNumer;
            denom.push(logNumer);
        }
        
        // Normalize
        let log_max = Math.max(...denom);
        let sum_of_ratios = 0.0;
        for (let j = 0; j < phi.length; j++) {
            sum_of_ratios += Math.exp(probs[j] - log_max);
        }
        let log_denom = log_max + Math.log(sum_of_ratios);
        for (let j = 0; j < phi.length; j++) {
            probs[j] = Math.exp(probs[j] - log_denom);
        }
        
        return probs;
    }
    
    function notAllocated(j) {
        // Returns true if no allocation entry equals i
        if (allocation[0] == j)
            return false;
        if (allocation[1] == j)
            return false;
        if (allocation[2] == j)
            return false;
        if (allocation[3] == j)
            return false;
        return true;
    }
    
    function shiftAllocIndicesLeft(j) {
        // Subtract 1 from all allocation entries > j
        for (let i = 0; i < allocation.length; i++) {
            if (allocation[i] > j)
                allocation[i]--;
        }
    }
    
    function chooseCategory(i, probs, is_singleton, cat0) {
        // Choose category randomly using probabilities in probs
        let cat = -1;
        let cum = 0.0;
        let u = lot.uniform(0,1);
        for (let k = 0; k < probs.length; k++) {
            cum += probs[k];
            if (u <= cum) {
                cat = k;
                break;
            }
        }
        
        // Report error if failed to choose category
        if (cat < 0) {
            console.log("***** ERROR: could not choose category ***** u = " + u.toFixed(5));
            for (let j = 0; j < probs.length; j++) {
                console.log("  probs[" + j + "] = " + probs[j].toFixed(5));
            }
        }
        
        // Record phi value if cat indexes one of the new proposed ones
        let aux_start = phi.length - (is_singleton ? 2 : 3);
        if (cat >= aux_start) {
            binGZero(phi[cat]);
        }
        
        allocation[i] = cat;
        for (let j = phi.length-1; j >= 0; j--) {
            if (notAllocated(j)) {
                shiftAllocIndicesLeft(j);
                phi.splice(j,1);
            }
        } 
    }
    
    function debugShowAllocProbs(probs, is_singleton) {
        console.log(" ");
        console.log("probs");
        let start = phi.length - (is_singleton ? 2 : 3);
        let cumprob = 0.0;
        for (let j = 0; j < start; j++) {
            cumprob += probs[j];
            console.log("   " + j + "  " + phi[j].toFixed(5) + " " + probs[j].toFixed(5) + "  " + cumprob);
        }
        for (let j = start; j < phi.length; j++) {
            cumprob += probs[j];
            console.log(" * " + j + "  " + phi[j].toFixed(5) + " " + probs[j].toFixed(5) + "  " + cumprob);
        }
    }
    
    function debugShowPhi() {
        console.log(" ");
        console.log("phi");
        for (let j = 0; j < phi.length; j++) {
            console.log("   " + j + "  " + phi[j].toFixed(5));
        }
    }
    
    function debugShowAllocation() {
        console.log(" ");
        console.log("allocation");
        for (let j = 0; j < allocation.length; j++) {
            console.log("   " + j + "  " + allocation[j]);
        }
    }
    
    function updateCounts() {
        total_count++;
        if (phi.length == 4)
            config_counts[14]++;
        else if (phi.length == 3) {
            if (allocation[0] == allocation[1])
                config_counts[4]++;
            else if (allocation[0] == allocation[2])
                config_counts[7]++;
            else if (allocation[1] == allocation[2])
                config_counts[10]++;
            else if (allocation[0] == allocation[3])
                config_counts[11]++;
            else if (allocation[1] == allocation[3])
                config_counts[12]++;
            else if (allocation[2] == allocation[3])
                config_counts[13]++;
        }
        else if (phi.length == 2) {
            if (allocation[0] == allocation[1] && allocation[1] == allocation[2])
                config_counts[1]++;
            else if (allocation[0] == allocation[1] && allocation[1] == allocation[3])
                config_counts[2]++;
            else if (allocation[0] == allocation[1] && allocation[2] == allocation[3])
                config_counts[3]++;
            else if (allocation[0] == allocation[2] && allocation[2] == allocation[3])
                config_counts[5]++;
            else if (allocation[0] == allocation[2] && allocation[1] == allocation[3])
                config_counts[6]++;
            else if (allocation[0] == allocation[3] && allocation[1] == allocation[2])
                config_counts[8]++;
            else if (allocation[1] == allocation[2] && allocation[2] == allocation[3])
                config_counts[9]++;
        }
        else
            config_counts[0]++;
    }
    
    function updateAllocationVector() {
        for (let i = 0; i < 4; i++) {
            let is_singleton = isSingleton(i);
                                
            // update group to which coin i is a member
            if (is_singleton) {
                // coin i is in its own group
                phi.push(drawFromG0());
                phi.push(drawFromG0());
            } 
            else {
                // coin i is in the same group as at least one other coin
                phi.push(drawFromG0());
                phi.push(drawFromG0());
                phi.push(drawFromG0());
            }
            let probs = calcAllocProbs(i, is_singleton);
            chooseCategory(i, probs, is_singleton, allocation[i]);
            updateCounts();
        }                
    }
                                        
    function restartMCMC() {
        phi = [];
        phi.push(drawFromG0());
        allocation = [0,0,0,0]; 
        total_count = 1;
        config_counts  = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
        resetGZeroCounts();
        updateAllocationHistogram();
        updateGZeroHistogram();
        updateInfo();
    }
                
    function resetCoins() {
        coininfo[0].y = 0;
        coininfo[0].n = 0;
        coininfo[1].y = 0;
        coininfo[1].n = 0;
        coininfo[2].y = 0;
        coininfo[2].n = 0;
        coininfo[3].y = 0;
        coininfo[3].n = 0;
        restartMCMC();
    }
                
    function nextIteration() {
        updateAllocationVector();
        updateGZeroHistogram();
        updateAllocationHistogram();
    }
    
    function startOrStop() {
        if (iterating)
            iterating = false;
        else {
            iterating = true;
            var timer = setInterval(function() {
                if (iterating)
                    nextIteration();
                else
                    clearInterval(timer);
            }, iteration_milisecs);
        }
    }
    startOrStop();
    
    function flipAllCoins(number_of_flips) {
        for (let j = 0; j < 4; j++) {
            // Flip coin j number_of_flips times
            let p = coininfo[j].p;
            for (let i = 0; i < number_of_flips; i++) {
                coininfo[j].n++;
                let u = lot.uniform(0,1);
                if (u < p)
                    coininfo[j].y++;
            }
        }
        restartMCMC();
    }
    
    function modifyAlpha(incr) {
        // alpha  10*alpha     a   incr = +1     incr = -1 
        // -----------------------------------------------
        //     2        20    20   30/10 = 3   10/10 =   1
        //  1.01      10.1    10   20/10 = 2    9/10 = 0.9
        //     1        10    10   20/10 = 2    9/10 = 0.9
        //  0.99       9.9    10   20/10 = 2    9/10 = 0.9
        //   0.9         9     9   10/10 = 1    8/10 = 0.8
        // -----------------------------------------------
        var a = Math.round(10*alpha);
        if (incr > 0) {
            a += (a < 10 ? 1 : 10);
        }
        else {
            a -= (a > 10 ? 10 : 1);
        }
        alpha = a/10;
        if (alpha < alphamin)
            alpha = alphamin;
        restartMCMC();
    }

    // Listen and react to keystrokes
    // key      code  key code  key code  key code  key code
    // -------------  --------  --------  --------  --------
    // tab         9    0   48    ~  192    a   65    n   78
    // return     13    1   49    ;  186    b   66    o   79
    // shift      16    2   50    =  187    c   67    p   80
    // control    17    3   51    ,  188    d   68    q   81
    // option     18    4   52    -  189    e   69    r   82
    // command    91    5   53    .  190    f   70    s   83
    // space      32    6   54    /  191    g   71    t   84
    // leftarrow  37    7   55    \  220    h   72    u   85
    // uparrow    38    8   56    [  219    i   73    v   86
    // rightarrow 39    9   57    ]  221    j   74    w   87
    // downarrow  40              '  222    k   75    x   88
    //                                      l   76    y   89
    //                                      m   77    z   90
    function keyDown() {
        if (d3.event.keyCode == 83) {
            // 83 is the "s" key
            startOrStop();
        }
        else if (d3.event.keyCode == 77) {
            // 77 is the "m" key
            restartMCMC();
        }
        else if (d3.event.keyCode == 38) {
            // 38 is the "up arrow" key
            modifyAlpha(1);
        }
        else if (d3.event.keyCode == 40) {
            // 40 is the "down arrow" key
            modifyAlpha(-1);
        }
        else if (d3.event.keyCode == 70) {
            // 70 is the "f" key
            flipAllCoins(100);
        }
        else if (d3.event.keyCode == 82) {
            // 82 is the "r" key
            resetCoins();
            resetGZeroCounts();
        }
    }
    d3.select("body")
        .on("keydown", keyDown);
        
    let pchoices = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9];
    let pindex = 4; // index of value selected at start

    var addButton = function(panel, label, onfunc) {
        var control_div = panel.append("div").append("div")
            .attr("class", "control");
        control_div.append("input")
            .attr("value",label)
            .attr("type", "button")
            .on("click", onfunc);
        }

    function addDropdown(panel, id, label, choices, selected_index, onfunc) {
        var control_div = panel.append("div").append("div")
            .attr("class", "control");
        control_div.append("select")
            .attr("id", id)
            .on("change", onfunc)
            .selectAll("option")
            .data(choices)
            .enter()
            .append("option")
            .text(function(d) {return d.toFixed(1);});
        d3.select("select#" + id).property("selectedIndex", selected_index);
        control_div.append("label")
            .html("&nbsp;" + label);
        }

    function createControlsPanel() {
        var controls_div = d3.select("div#controls");

        // Create drop-down lists within controls_div to allow changing the 
        // true proportion of heads for each of the four coins
        addDropdown(controls_div, "dropdownA", "true fraction heads for coin A", pchoices, pindex, function() {
            var selected_index = d3.select(this).property('selectedIndex');
            coininfo[0].p = pchoices[selected_index];
            let nflips = coininfo[0].n;
            resetCoins();
            flipAllCoins(nflips);
            resetGZeroCounts();
        });
        addDropdown(controls_div, "dropdownB", "true fraction heads for coin B", pchoices, pindex, function() {
            var selected_index = d3.select(this).property('selectedIndex');
            coininfo[1].p = pchoices[selected_index];
            let nflips = coininfo[1].n;
            resetCoins();
            flipAllCoins(nflips);
            resetGZeroCounts();
        });
        addDropdown(controls_div, "dropdownC", "true fraction heads for coin C", pchoices, pindex, function() {
            var selected_index = d3.select(this).property('selectedIndex');
            coininfo[2].p = pchoices[selected_index];
            let nflips = coininfo[2].n;
            resetCoins();
            flipAllCoins(nflips);
            resetGZeroCounts();
        });
        addDropdown(controls_div, "dropdownD", "true fraction heads for coin D", pchoices, pindex, function() {
            var selected_index = d3.select(this).property('selectedIndex');
            coininfo[3].p = pchoices[selected_index];
            let nflips = coininfo[03].n;
            resetCoins();
            flipAllCoins(nflips);
            resetGZeroCounts();
        });
        addButton(controls_div, "Flip all coins 100 times (f key)", function() {
            flipAllCoins(100);
        });
        addButton(controls_div, "Reset all coins to zero flips (r key)", function() {
            resetCoins();
            resetGZeroCounts();
        });
        addButton(controls_div, "Increase alpha (up arrow key)", function() {
            modifyAlpha(1);
        });
        addButton(controls_div, "Decrease alpha (down arrow key", function() {
            modifyAlpha(-1);
        });
        addButton(controls_div, "Restart MCMC (m key)", function() {
            restartMCMC();
        });
        addButton(controls_div, "Start/stop MCMC (s key)", function() {
            startOrStop();
        });
    }                
    createControlsPanel();
</script>
<br/>

## Description
Imagine you have 4 coins (A, B, C, and D) that have potentially different propensities for coming up heads on any given flip (you can set the true propensities for each coin using the drop-down controls). This applet demonstrates how you can use a Dirichlet Process Prior (DPP) to automatically cluster coins into groups. 

If all 4 coins have p = 0.5 and you flip them a sufficient number of times, the ABCD (all in one group) configuration should have the highest posterior probability. 

If coins A and B have p = 0.2 and coins C and D have p = 0.8, then (given sufficient flips) the configuration AB\|CD should have the highest probability. 

The concentration parameter alpha determines how much clustering is encouraged by the prior: small values of alpha lead to fewer groups, while large values of alpha encourage placing each coin in its own group.

Run the applet without data (all coins have n = 0) to see the prior (e.g. try changing alpha while n = 0). Now flip the coins a few hundred times to see the effect of information being added via the likelihood.

The small histogram in the lower right corner shows the distribution of p, the propensity to land heads on any given flip. This distribution is Beta(2,2) in the prior, but note how information in the data can easily make it bimodal or multimodal.

Notes: 
* If nothing seems to happen when you press the shortcut keys, click on the lavender plot box so that the app has the keyboard focus
* Hold down the shift key while using the arrow keys to modify alpha so that the browser does not scroll at the same time

## Acknowledgements

This applet makes use of [d3js](https://d3js.org/) and the lgamma function from [John D. Cook](https://www.johndcook.com/blog/stand_alone_code/).
Please see the 
[GitHub site](https://github.com/molevolworkshop/molevolworkshop.github.io/tree/master/assets/js) 
for details about licensing.

## Licence

Creative Commons Attribution 4.0 International.
License (CC BY 4.0). To view a copy of this license, visit
[http://creativecommons.org/licenses/by/4.0/](http://creativecommons.org/licenses/by/4.0/) or send a letter to Creative Commons, 559
Nathan Abbott Way, Stanford, California 94305, USA.
