var dataArray = [];
function draw_graph () {
  var user1 = dataArray.slice(-2)[0];
  var user2 = dataArray.slice(-1)[0];
  var chart = new CanvasJS.Chart('chartContainer',
    {
      title: {
        text: 'Members Comparison'
      },
      animationEnabled: true,
      legend: {
        cursor: 'pointer',
        itemclick: function (e) {
          if (typeof (e.dataSeries.visible) === 'undefined' || e.dataSeries.visible) {
            e.dataSeries.visible = false;
          } else {
            e.dataSeries.visible = true;
          }
          chart.render();
          }
      },
      axisY: {
        title: 'Value'
      },
      data: [
        {
          type: 'column',
          showInLegend: true,
          name: user1.uname,
          color: 'red',
          dataPoints: [
            { y: user1.work_hours, label: 'Work Hours' },
            { y: user1.height, label: 'Height' },
            { y: user1.freetime_hours, label: 'Free Time' },
            { y: user1.calories, label: 'Calories' }
            ]
        },
        {
          type: 'column',
          showInLegend: true,
          name: user2.uname,
          color: 'blue',
          dataPoints: [
            { y: user2.work_hours, label: 'Work hours' },
            { y: user2.height, label: 'Height' },
            { y: user2.freetime_hours, label: 'Free Time' },
            { y: user2.calories, label: 'Calories' }
          ]
        }
      ]
    });
 chart.render();
}
var checkedCheckboxes = []
$(document).on('change', '#member_row', function () {
  var row = $(this).closest('#member_row');
  var cbox = row.find('#selected_member');
  checkedCheckboxes.push(cbox)
  var atLeastTwoChecked = $('#selected_member:checked').length > 1;
  var three = $('#selected_member:checked').length > 2
  var uname = row.find('td').eq(1).text();
  if ($(cbox).prop('checked') == false) {
    for (var item in dataArray){
      data = dataArray[item];
      if(data.uname == uname) {
        dataArray.pop(item);
        break;
      }
    }
    } else {
      var data = $('#member_row').data('memberdata');
      var user_id = row.find('td:first').text();
      user_id = parseInt(user_id);
      user_data = data[user_id];
      udata = {'uname': uname, 'age': user_data.age, 'weight': user_data.weight, 'height':user_data.height};
      dataArray.push(udata);
    }
  if (atLeastTwoChecked) {
    $('.compare_button').removeClass('disabled');
    $('#msg').hide();
    $('#chartContainer').show();
    draw_graph()
  } else {
    $('.compare_button').addClass('disabled');
    $('#msg').show();
    $('#chartContainer').hide();
  }
  if (three) {
    firstCheck = checkedCheckboxes[0]
    firstCheck.attr('checked', false);
    checkedCheckboxes.splice(checkedCheckboxes.indexOf(firstCheck), 1)
  }
});
