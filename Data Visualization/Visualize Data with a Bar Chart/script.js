
/*
This code is written in JavaScript, a programming language that is commonly used to create interactive elements on websites.

The code begins by defining several variables:

projectName is a constant that holds the value 'bar-chart'.
width and height are variables that hold the width and height of the bar chart, respectively.
barWidth is a variable that holds the width of each bar in the chart, calculated by dividing the width by 275.
tooltip is a variable that holds a reference to a div element that will be used as a tooltip to display additional information when the user hovers over a bar in the chart.
overlay is a variable that holds a reference to a div element that will be used to display a transparent layer over the chart when the user hovers over a bar.
svgContainer is a variable that holds a reference to an svg element, which stands for Scalable Vector Graphics. This element will be used to hold the bar chart.
The code then uses the d3 library to retrieve data from a JSON file at a specified URL and parse it as a JavaScript object. This data contains information about the Gross Domestic Product (GDP) of the United States.

The code then uses the d3 library to create and customize an x and y axis for the bar chart, using scales to map the data values to the appropriate positions on the chart.

Finally, the code uses the d3 library to create and customize the bars of the bar chart, using data from the JSON file to set the position, width, height, and other attributes of each bar. The code also includes event listeners to display the tooltip and overlay when the user hovers over a bar.
*/

const projectName = 'bar-chart';

var width = 800,
  height = 400,
  barWidth = width / 275;

var tooltip = d3
  .select('.visHolder')
  .append('div')
  .attr('id', 'tooltip')
  .style('opacity', 0);

var overlay = d3
  .select('.visHolder')
  .append('div')
  .attr('class', 'overlay')
  .style('opacity', 0);

var svgContainer = d3
  .select('.visHolder')
  .append('svg')
  .attr('width', width + 100)
  .attr('height', height + 60);

d3.json(
  'https://raw.githubusercontent.com/freeCodeCamp/ProjectReferenceData/master/GDP-data.json'
)
  .then(data => {
    svgContainer
      .append('text')
      .attr('transform', 'rotate(-90)')
      .attr('x', -200)
      .attr('y', 80)
      .text('Gross Domestic Product');

    svgContainer
      .append('text')
      .attr('x', width / 2 + 120)
      .attr('y', height + 50)
      .text('More Information: http://www.bea.gov/national/pdf/nipaguid.pdf')
      .attr('class', 'info');

    var years = data.data.map(function (item) {
      var quarter;
      var temp = item[0].substring(5, 7);

      if (temp === '01') {
        quarter = 'Q1';
      } else if (temp === '04') {
        quarter = 'Q2';
      } else if (temp === '07') {
        quarter = 'Q3';
      } else if (temp === '10') {
        quarter = 'Q4';
      }

      return item[0].substring(0, 4) + ' ' + quarter;
    });

    var yearsDate = data.data.map(function (item) {
      return new Date(item[0]);
    });

    var xMax = new Date(d3.max(yearsDate));
    xMax.setMonth(xMax.getMonth() + 3);
    var xScale = d3
      .scaleTime()
      .domain([d3.min(yearsDate), xMax])
      .range([0, width]);

    var xAxis = d3.axisBottom().scale(xScale);

    svgContainer
      .append('g')
      .call(xAxis)
      .attr('id', 'x-axis')
      .attr('transform', 'translate(60, 400)');

    var GDP = data.data.map(function (item) {
      return item[1];
    });

    var scaledGDP = [];

    var gdpMax = d3.max(GDP);

    var linearScale = d3.scaleLinear().domain([0, gdpMax]).range([0, height]);

    scaledGDP = GDP.map(function (item) {
      return linearScale(item);
    });

    var yAxisScale = d3.scaleLinear().domain([0, gdpMax]).range([height, 0]);

    var yAxis = d3.axisLeft(yAxisScale);

    svgContainer
      .append('g')
      .call(yAxis)
      .attr('id', 'y-axis')
      .attr('transform', 'translate(60, 0)');

    d3.select('svg')
      .selectAll('rect')
      .data(scaledGDP)
      .enter()
      .append('rect')
      .attr('data-date', function (d, i) {
        return data.data[i][0];
      })
      .attr('data-gdp', function (d, i) {
        return data.data[i][1];
      })
      .attr('class', 'bar')
      .attr('x', function (d, i) {
        return xScale(yearsDate[i]);
      })
      .attr('y', function (d) {
        return height - d;
      })
      .attr('width', barWidth)
      .attr('height', function (d) {
        return d;
      })
      .attr('index', (d, i) => i)
      .style('fill', '#33adff')
      .attr('transform', 'translate(60, 0)')
      .on('mouseover', function (event, d) {
        
        var i = this.getAttribute('index');

        overlay
          .transition()
          .duration(0)
          .style('height', d + 'px')
          .style('width', barWidth + 'px')
          .style('opacity', 0.9)
          .style('left', i * barWidth + 0 + 'px')
          .style('top', height - d + 'px')
          .style('transform', 'translateX(60px)');
        tooltip.transition().duration(200).style('opacity', 0.9);
        tooltip
          .html(
            years[i] +
              '<br>' +
              '$' +
              GDP[i].toFixed(1).replace(/(\d)(?=(\d{3})+\.)/g, '$1,') +
              ' Billion'
          )
          .attr('data-date', data.data[i][0])
          .style('left', i * barWidth + 30 + 'px')
          .style('top', height - 100 + 'px')
          .style('transform', 'translateX(60px)');
      })
      .on('mouseout', function () {
        tooltip.transition().duration(200).style('opacity', 0);
        overlay.transition().duration(200).style('opacity', 0);
      });
  })
  .catch(e => console.log(e));
