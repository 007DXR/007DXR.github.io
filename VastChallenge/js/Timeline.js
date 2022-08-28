

// var timelineChart = echarts.init(document.getElementById('timeline'));
var relationChart = echarts.init(document.getElementById('relation'));
// timelineChart.setOption({

//     xAxis: {
//         data: [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
//         name: '日期',
//         type: 'category',
//         splitLine: {
//             show: false
//         },

//         axisLabel: {
//             formatter: '1/{value}/2014'
//         }
//     },
//     yAxis: {
//         min: 0,
//         max: 24 * 60,
//         name: '时刻',
//         type: 'value',
//         splitLine: {
//             show: false
//         },

//         axisLabel: {

//             formatter: function (value) {
//                 return parseInt(value / 60) + ':' + parseInt(value) % 60;
//             }
//         }
//     },
//     dataZoom: [
//         {
//             type: 'slider',
//             xAxisIndex: 0,
//             filterMode: 'none',
//             labelFormatter: '1/{value}/2014'
//         },
//         {
//             left: "0%",
//             type: 'slider',
//             yAxisIndex: 0,
//             filterMode: 'none',
//             labelFormatter: function (value) {
//                 return parseInt(value / 60) + ':' + parseInt(value) % 60;
//             }
//         }
//     ],

// });

relationChart.setOption(compute_option( 0, 1440,6, 17,))
console.log(relationChart.getOption())
relationChart.on("dataZoom", function (data) {
    let x = relationChart.getOption().dataZoom[0]
    let y = relationChart.getOption().dataZoom[1]
    let graph=emailNode(Math.floor(y.startValue), Math.floor(y.endValue),x.startValue + 6, x.endValue + 6, )
    relationChart.setOption({"series": [{"links":graph[0],"data":graph[1]}]})

})
relationChart.on("click", function (data) {
    console.log("click",data.data.name)
    console.log("click",data)
    if (data.dataType=="edge")
    emailCard(data.data)
    else personCard(data.data.name)
})

