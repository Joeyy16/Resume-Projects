/*
This code creates a scatter plot with data from a JSON file. The plot compares the performance of professional cycling athletes in different years.

The code first sets up the dimensions of the plot, including the margins. It then creates scales for the x-axis (year), y-axis (time in minutes), and color of the dots. The scales are used to map the data values to the corresponding positions on the plot.

Next, the code sets up the x-axis and y-axis and adds them to the plot with the corresponding labels.

Then, the code loads the JSON data and formats it by parsing the time data into Date objects. It also sets the domain of the x and y scales using the min and max values of the year and time data, respectively.

The code then creates circles (dots) for each data point, positioning them according to the x and y scales and adding the corresponding data attributes. It also adds a tooltip to the plot, which will display additional information about the data point when the user hovers over a dot.

Finally, the code adds a legend to the plot, using the color scale to assign the appropriate color to each dot based on the doping allegations of the athlete.
*/

var projectName = 'scatter-plot';

var url =
  'https://raw.githubusercontent.com/freeCodeCamp/ProjectReferenceData/master/cyclist-data.json';
var margin = {
    top: 100,
    right: 20,
    bottom: 30,
    left: 60
  },
  width = 920 - margin.left - margin.right,
  height = 630 - margin.top - margin.bottom;

var x = d3.scaleLinear().range([0, width]);

var y = d3.scaleTime().range([0, height]);

var color = d3.scaleOrdinal(d3.schemeCategory10);

var timeFormat = d3.timeFormat('%M:%S');
var xAxis = d3.axisBottom(x).tickFormat(d3.format('d'));

var yAxis = d3.axisLeft(y).tickFormat(timeFormat);

var div = d3
  .select('body')
  .append('div')
  .attr('class', 'tooltip')
  .attr('id', 'tooltip')
  .style('opacity', 0);

var svg = d3
  .select('body')
  .append('svg')
  .attr('width', width + margin.left + margin.right)
  .attr('height', height + margin.top + margin.bottom)
  .attr('class', 'graph')
  .append('g')
  .attr('transform', 'translate(' + margin.left + ',' + margin.top + ')');

d3.json(url)
  .then(data => {
    data.forEach(function (d) {
      d.Place = +d.Place;
      var parsedTime = d.Time.split(':');
      d.Time = new Date(1970, 0, 1, 0, parsedTime[0], parsedTime[1]);
    });

    x.domain([
      d3.min(data, function (d) {
        return d.Year - 1;
      }),
      d3.max(data, function (d) {
        return d.Year + 1;
      })
    ]);
    y.domain(
      d3.extent(data, function (d) {
        return d.Time;
      })
    );

    svg
      .append('g')
      .attr('class', 'x axis')
      .attr('id', 'x-axis')
      .attr('transform', 'translate(0,' + height + ')')
      .call(xAxis)
      .append('text')
      .attr('class', 'x-axis-label')
      .attr('x', width)
      .attr('y', -6)
      .style('text-anchor', 'end')
      .text('Year');

    svg
      .append('g')
      .attr('class', 'y axis')
      .attr('id', 'y-axis')
      .call(yAxis)
      .append('text')
      .attr('class', 'label')
      .attr('transform', 'rotate(-90)')
      .attr('y', 6)
      .attr('dy', '.71em')
      .style('text-anchor', 'end')
      .text('Best Time (minutes)');

    svg
      .append('text')
      .attr('transform', 'rotate(-90)')
      .attr('x', -160)
      .attr('y', -44)
      .style('font-size', 18)
      .text('Time in Minutes');

    svg
      .selectAll('.dot')
      .data(data)
      .enter()
      .append('circle')
      .attr('class', 'dot')
      .attr('r', 6)
      .attr('cx', function (d) {
        return x(d.Year);
      })
      .attr('cy', function (d) {
        return y(d.Time);
      })
      .attr('data-xvalue', function (d) {
        return d.Year;
      })
      .attr('data-yvalue', function (d) {
        return d.Time.toISOString();
      })
      .style('fill', function (d) {
        return color(d.Doping !== '');
      })
      .on('mouseover', function (event, d) {
        div.style('opacity', 0.9);
        div.attr('data-year', d.Year);
        div
          .html(
            d.Name +
              ': ' +
              d.Nationality +
              '<br/>' +
              'Year: ' +
              d.Year +
              ', Time: ' +
              timeFormat(d.Time) +
              (d.Doping ? '<br/><br/>' + d.Doping : '')
          )
          .style('left', event.pageX + 'px')
          .style('top', event.pageY - 28 + 'px');
      })
      .on('mouseout', function () {
        div.style('opacity', 0);
      });


    svg
      .append('text')
      .attr('id', 'title')
      .attr('x', width / 2)
      .attr('y', 0 - margin.top / 2)
      .attr('text-anchor', 'middle')
      .style('font-size', '30px')
      .text('Doping in Professional Bicycle Racing');

    svg
      .append('text')
      .attr('x', width / 2)
      .attr('y', 0 - margin.top / 2 + 25)
      .attr('text-anchor', 'middle')
      .style('font-size', '20px')
      .text("35 Fastest times up Alpe d'Huez");

    var legendContainer = svg.append('g').attr('id', 'legend');

    var legend = legendContainer
      .selectAll('#legend')
      .data(color.domain())
      .enter()
      .append('g')
      .attr('class', 'legend-label')
      .attr('transform', function (d, i) {
        return 'translate(0,' + (height / 2 - i * 20) + ')';
      });

    legend
      .append('rect')
      .attr('x', width - 18)
      .attr('width', 18)
      .attr('height', 18)
      .style('fill', color);

    legend
      .append('text')
      .attr('x', width - 24)
      .attr('y', 9)
      .attr('dy', '.35em')
      .style('text-anchor', 'end')
      .text(function (d) {
        if (d) {
          return 'Riders with doping allegations';
        } else {
          return 'No doping allegations';
        }
      });
  })
  .catch(err => console.log(err));
