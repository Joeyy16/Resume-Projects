/*
This code is creating a choropleth map, which is a map that uses color to encode data values. It uses the D3.js library to read in data from two files: COUNTY_FILE and EDUCATION_FILE. The data in EDUCATION_FILE represents the percentage of adults in each county with a bachelor's degree or higher, and the data in COUNTY_FILE is a TopoJSON file containing the geometry for each county in the United States.

The code first sets up a few constants and variables, including an SVG element, a tooltip element, and a color scale. It then creates a g element to hold a legend for the map and appends a series of rect elements to it, each representing a range of data values and colored accordingly.

Next, the code uses Promise.all to read in both data files asynchronously and passes them to the ready function when both have been loaded. In the ready function, the code appends a g element to the SVG and binds the data from EDUCATION_FILE to it. It then appends a path element to the g element for each county and sets its data-education attribute to the corresponding data value from EDUCATION_FILE. The fill attribute of each path element is set using the color scale, which maps data values to colors.

Finally, the code appends a g element to the SVG for the state boundaries and binds the data from COUNTY_FILE to it. It then appends a path element for each state and sets its d attribute using the path generator.

Overall, this code is creating a map of the United States that visualizes the percentage of adults in each county with a bachelor's degree or higher. The legend at the bottom allows the user to see the range of values represented by each color.
*/

const projectName = 'choropleth';

var body = d3.select('body');

var svg = d3.select('svg');

var tooltip = body
  .append('div')
  .attr('class', 'tooltip')
  .attr('id', 'tooltip')
  .style('opacity', 0);

var path = d3.geoPath();

var x = d3.scaleLinear().domain([2.6, 75.1]).rangeRound([600, 860]);

var color = d3
  .scaleThreshold()
  .domain(d3.range(2.6, 75.1, (75.1 - 2.6) / 8))
  .range(d3.schemeGreens[9]);

var g = svg
  .append('g')
  .attr('class', 'key')
  .attr('id', 'legend')
  .attr('transform', 'translate(0,40)');

g.selectAll('rect')
  .data(
    color.range().map(function (d) {
      d = color.invertExtent(d);
      if (d[0] === null) {
        d[0] = x.domain()[0];
      }
      if (d[1] === null) {
        d[1] = x.domain()[1];
      }
      return d;
    })
  )
  .enter()
  .append('rect')
  .attr('height', 8)
  .attr('x', function (d) {
    return x(d[0]);
  })
  .attr('width', function (d) {
    return d[0] && d[1] ? x(d[1]) - x(d[0]) : x(null);
  })
  .attr('fill', function (d) {
    return color(d[0]);
  });

g.append('text')
  .attr('class', 'caption')
  .attr('x', x.range()[0])
  .attr('y', -6)
  .attr('fill', '#000')
  .attr('text-anchor', 'start')
  .attr('font-weight', 'bold');

g.call(
  d3
    .axisBottom(x)
    .tickSize(13)
    .tickFormat(function (x) {
      return Math.round(x) + '%';
    })
    .tickValues(color.domain())
)
  .select('.domain')
  .remove();

const EDUCATION_FILE =
  'https://raw.githubusercontent.com/no-stack-dub-sack/testable-projects-fcc/master/src/data/choropleth_map/for_user_education.json';
const COUNTY_FILE =
  'https://raw.githubusercontent.com/no-stack-dub-sack/testable-projects-fcc/master/src/data/choropleth_map/counties.json';

Promise.all([d3.json(COUNTY_FILE), d3.json(EDUCATION_FILE)])
  .then(data => ready(data[0], data[1]))
  .catch(err => console.log(err));

function ready(us, education) {
  svg
    .append('g')
    .attr('class', 'counties')
    .selectAll('path')
    .data(topojson.feature(us, us.objects.counties).features)
    .enter()
    .append('path')
    .attr('class', 'county')
    .attr('data-fips', function (d) {
      return d.id;
    })
    .attr('data-education', function (d) {
      var result = education.filter(function (obj) {
        return obj.fips === d.id;
      });
      if (result[0]) {
        return result[0].bachelorsOrHigher;
      }
      
      console.log('could find data for: ', d.id);
      return 0;
    })
    .attr('fill', function (d) {
      var result = education.filter(function (obj) {
        return obj.fips === d.id;
      });
      if (result[0]) {
        return color(result[0].bachelorsOrHigher);
      }
     
      return color(0);
    })
    .attr('d', path)
    .on('mouseover', function (event, d) {
      tooltip.style('opacity', 0.9);
      tooltip
        .html(function () {
          var result = education.filter(function (obj) {
            return obj.fips === d.id;
          });
          if (result[0]) {
            return (
              result[0]['area_name'] +
              ', ' +
              result[0]['state'] +
              ': ' +
              result[0].bachelorsOrHigher +
              '%'
            );
          }
          
          return 0;
        })
        .attr('data-education', function () {
          var result = education.filter(function (obj) {
            return obj.fips === d.id;
          });
          if (result[0]) {
            return result[0].bachelorsOrHigher;
          }
          
          return 0;
        })
        .style('left', event.pageX + 10 + 'px')
        .style('top', event.pageY - 28 + 'px');
    })
    .on('mouseout', function () {
      tooltip.style('opacity', 0);
    });

  svg
    .append('path')
    .datum(
      topojson.mesh(us, us.objects.states, function (a, b) {
        return a !== b;
      })
    )
    .attr('class', 'states')
    .attr('d', path);
}
