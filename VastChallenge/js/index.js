let flag = 0;
let newspapers = 'all';
newsnames = [
  'nytimes',
  'latimes',
  'wsj',
]
let x_attr = 'Time';
let y_attr = 'Number of news';
function change_news(){
  newspapers = document.getElementById("selectnews").value;
  if(newspapers != 'all') newspapers = Array(newspapers)
  // refreshthegraph();
}
$(function() {

  // Initiate Slider
  $('#slider-range').slider({
    range: true,
    min: 1982,
    max: 2014,
    step: 1,
    values: [1982, 2014]
  });
  // Move the range wrapper into the generated divs
  $('.ui-slider-range').html('<div class="range-wrapper"><div class="range"></div></div>');

  // Apply initial values to the range container
  // $('.range').html('<span class="range-value">' + $('#slider-range').slider("values", 0).toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,") + '</span><span class="range-divider"></span><span class="range-value">' + $("#slider-range").slider("values", 1).toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,") + '</span>');

  // Show the gears on press of the handles
  $('.ui-slider-handle, .ui-slider-range').on('mousedown', function() {
    $('.gear-large').addClass('active');
  });

  // document.getElementById('start_date').value = '1980-01-01'
  // document.getElementById('end_date').value = '2000-12-31'

  // Hide the gears when the mouse is released
  // Done on document just incase the user hovers off of the handle
  $(document).on('mouseup', function() {
    if ($('.gear-large').hasClass('active')) {
      $('.gear-large').removeClass('active');
    }
  });


  // Rotate the gears
  var gearOneAngle = 0,
    gearTwoAngle = 0,
    rangeWidth = $('.ui-slider-range').css('width');

  $('.gear-one').css('transform', 'rotate(' + gearOneAngle + 'deg)');
  $('.gear-two').css('transform', 'rotate(' + gearTwoAngle + 'deg)');
  // $('#xwm').remove()
  $('#slider-range').slider({
    slide: function(event, ui) {

      // Update the range container values upon sliding

      // $('.range').html('<span class="range-value">' + ui.values[0].toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,") + '</span><span class="range-divider"></span><span class="range-value">' + ui.values[1].toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,") + '</span>');

      // Get old value
      var previousVal = parseInt($(this).data('value'));
      

      // Save new value
      $(this).data({
        'value': parseInt(ui.value)
      });

      // Figure out which handle is being used
      if (ui.values[0] == ui.value) {

        // Left handle
        if (previousVal > parseInt(ui.value)) {
          // value decreased
          gearOneAngle -= 7;
          $('.gear-one').css('transform', 'rotate(' + gearOneAngle + 'deg)');
        } else {
          // value increased
          gearOneAngle += 7;
          $('.gear-one').css('transform', 'rotate(' + gearOneAngle + 'deg)');
        }
        tmp = document.getElementById('start_date').value;
        tmpls = tmp.split('-')
        tmpls[0] = (ui.values[0]).toString();
        document.getElementById('start_date').value = tmpls.join('-')
        

      } else {

        // Right handle
        if (previousVal > parseInt(ui.value)) {
          // value decreased
          gearOneAngle -= 7;
          $('.gear-two').css('transform', 'rotate(' + gearOneAngle + 'deg)');
        } else {
          // value increased
          gearOneAngle += 7;
          $('.gear-two').css('transform', 'rotate(' + gearOneAngle + 'deg)');
        }

        tmp = document.getElementById('end_date').value;
        tmpls = tmp.split('-')
        tmpls[0] = (ui.values[1]).toString();
        document.getElementById('end_date').value = tmpls.join('-')

      }
      refreshthegraph();
    }
  });

  // Prevent the range container from moving the slider
  $('.range, .range-alert').on('mousedown', function(event) {
    event.stopPropagation();
  });
  refreshthegraph()
});
function get_time_range(){
  st_date = document.getElementById('start_date').value;
  ed_date = document.getElementById('end_date').value;
  tmp = st_date.split('-').map(x => Number(x));
  st_year = tmp[0];
  st_month = tmp[1];
  st_date = tmp[2];
  tmp = ed_date.split('-').map(x => Number(x));
  ed_year = tmp[0];
  ed_month = tmp[1];
  ed_date = tmp[2];
  return {
    'st_year': st_year,
    'st_month': st_month,
    'st_date': st_date,
    'ed_year': ed_year,
    'ed_month': ed_month,
    'ed_date': ed_date
  };
}

function refreshthegraph(flag = false) {
  if (!flag) {
    d3.select('#container_cloud').selectAll('svg > *').remove();
    alltime = get_time_range();
    cloud_data = generate_wordcloud(alltime.st_year, alltime.ed_year)
    draw_main_cloud()
  }
  tmp = d3.selectAll('.word-selected')._groups[0];
  var words = [];
  for(let i=0;i<tmp.length;i++){
    words.push(tmp[i]['textContent'])
  }
  // console.log(1)
  // console.log(words)
  if (words.length==0) {
	  // console.log(1)
 //    for(let i=0;i<cloud_data.length; ++i)
	// {
	// 	// console.log(i)
	// 	words.push(cloud_data[i]['text'])
	// }
  }
  console.log(words)
  // console.log((1))
  alltime = get_time_range();
  // console.log(alltime)
  // console.log(words)
  // console.log(alltime['st_year'])
  let start_year = alltime['st_year'].toString() + '-' + alltime['st_month'].toString() + '-' + alltime['st_date'].toString()
  let end_year = alltime['ed_year'].toString() + '-' + alltime['ed_month'].toString() + '-' + alltime['ed_date'].toString()
  $('#slider-range').slider({
    range: true,
    min: 1982,
    max: 2014,
    step: 1,
    values: [alltime['st_year'], alltime['ed_year']]
  });
  // $('.range').html('<span class="range-value">' + $('#slider-range').slider("values", 0).toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,") + '</span><span class="range-divider"></span><span class="range-value">' + $("#slider-range").slider("values", 1).toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,") + '</span>');
  console.log(start_year)
  console.log(end_year)
  showNewsList(data_, new Date(start_year), new Date(end_year), words);
  linechart(data_, new Date(start_year), new Date(end_year), words);
}
