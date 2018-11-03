function gas_get() {
    var myChart = echarts.init(document.getElementById('container'));
    $.get('http://localhost:8000/index/api/device/?english=Gas', function(data, status) {

          var xdata = [];
          var xvalue = [];
          var i;
          for (i=0; i<data.length; i++) {
            xdata.push(data[i][0]);
            if (data[i][1] == 'Alarm!')
              xvalue.push(1);
            else
              xvalue.push(0);
          }

          var option = {
          title: {
            left: 'center',
            text: '烟雾状态曲线',
          },
          toolbox: {
            feature: {
              dataZoom: {
                  yAxisIndex: 'none'
              },
              restore: {},
              saveAsImage: {}
            }
          },
          legend: {
            data: ['烟雾状态'],
          },
          xAxis: {
            type: 'category',
            data: xdata,
          },
          yAxis: {
            type: 'value',
            boundaryGap: [0, '100%']
          },
          series: [{
            name: '状态',
            type: 'line',
            data: xvalue,
          }],
          };

          myChart.setOption(option);
          });
}
function pir_get() {

          var myChart_pir = echarts.init(document.getElementById("container_pir"));
          $.get('http://localhost:8000/index/api/device/?english=Pir', function(data, status) {

          var xdata = [];
          var xvalue = [];
          var i;
          for (i=0; i<data.length; i++) {
            xdata.push(data[i][0]);
            if (data[i][1] == 'Alarm!')
              xvalue.push(1);
            else
              xvalue.push(0);
          }

          var option = {
          title: {
            left: 'center',
            text: '人体感应曲线',
          },
          toolbox: {
            feature: {
              dataZoom: {
                  yAxisIndex: 'none'
              },
              restore: {},
              saveAsImage: {}
            }
          },
          legend: {
            data: ['人体感应'],
          },
          xAxis: {
            type: 'category',
            data: xdata,
          },
          yAxis: {
            type: 'value',
            boundaryGap: [0, '100%']
          },
          series: [{
            name: '状态',
            type: 'line',
            data: xvalue,
          }],
          };

          myChart_pir.setOption(option);
          });
}