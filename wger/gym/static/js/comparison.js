var dataArray = [];
var checkedCheckboxes = [];
function drawGraph() {
  var user1 = dataArray.slice(-2)[0];
  var user2 = dataArray.slice(-1)[0];
  /* eslint-disable no-undef */
  var chart = new CanvasJS.Chart('chartContainer',
  /* eslint-disable no-undef */
    {
      title: {
        text: 'Members Comparison'
      },
      animationEnabled: true,
      legend: {
        cursor: 'pointer',
        /* eslint-disable no-param-reassign*/
        itemclick: function (e) {
          if (typeof (e.dataSeries.visible) === 'undefined' || e.dataSeries.visible) {
            e.dataSeries.visible = false;
          } else {
            e.dataSeries.visible = true;
          }
        /* eslint-disable no-param-reassign*/
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
            { y: user1.age, label: 'Age' },
            { y: user1.height, label: 'Height' },
            { y: user1.freetime, label: 'Free Time' },
            { y: user1.calories, label: 'Calories x10' }
          ]
        },
        {
          type: 'column',
          showInLegend: true,
          name: user2.uname,
          color: 'blue',
          dataPoints: [
            { y: user2.age, label: 'Age' },
            { y: user2.height, label: 'Height' },
            { y: user2.freetime, label: 'Free Time /10' },
            { y: user2.calories, label: 'Calories x10' }
          ]
        }
      ]
    });
  chart.render();
}
$(document).on('change', '#member_row', function () {
  var row = $(this).closest('#member_row');
  var cbox = row.find('#selected_member');
  var atLeastTwoChecked = $('#selected_member:checked').length > 1;
  var uncheckAuser = $('#selected_member:checked').length > 2;
  var uname = row.find('td').eq(1).text();
  var data;
  var userId;
  var userData;
  var udata;
  var firstCheck;
  var item;
  checkedCheckboxes.push(cbox);

  if ($(cbox).prop('checked') === false) {
    /* eslint-disable no-restricted-syntax*/
    for (item in dataArray) {
      if (Object.prototype.hasOwnProperty.call(dataArray, item)) {
        data = dataArray[item];
        if (data.uname === uname) {
          dataArray.pop(item);
          break;
        }
      }
    }
    /* eslint-disable no-restricted-syntax*/
  } else {
    data = $('#member_row').data('memberdata');
    userId = row.find('td:first').text();
    userId = parseInt(userId, 10);
    userData = data[userId];
    udata = { uname: uname, age: userData.age, calories: userData.calories, height: userData.height, freetime: userData.freetime };
    dataArray.push(udata);
  }
  if (atLeastTwoChecked) {
    $('.compare_button').removeClass('disabled');
    $('#msg').hide();
    $('#chartContainer').show();
    drawGraph();
  } else {
    $('.compare_button').addClass('disabled');
    $('#msg').show();
    $('#chartContainer').hide();
  }
  if (uncheckAuser) {
    firstCheck = checkedCheckboxes[0];
    firstCheck.attr('checked', false);
    checkedCheckboxes.splice(checkedCheckboxes.indexOf(firstCheck), 1);
  }
});
