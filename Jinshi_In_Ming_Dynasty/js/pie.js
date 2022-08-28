



function compute_name(data,startyear, endyear) {

    name_data = {}
    for (var i = 0; i < data.length; ++i) {
        year = data[i].年份
        let name = data[i].姓名
        name = name[0]
        if (startyear <= year && year <= endyear) {
            if (name_data[name] == null) {
                name_data[name] = 0

            }

            name_data[name]++;
            // console.log(name+year)
        }
    }
    var indexs = Object.keys(name_data).sort(function (a, b) { return name_data[b] - name_data[a] });

    series_data = []
    var sum = 0
    for (var j in indexs) {
        let name = indexs[j]
        if (j > 10) {
            sum += name_data[name]
            continue
        }
        var x = { "value": name_data[name], "name": name }


        series_data.push(x)
    }
    // series_data.push({ "value": sum, "name": "其他" })
    console.log(series_data)
    return series_data
}
function compute_name_option(data,startyear, endyear) {
    var option = {
        title: {
            text: '姓氏',
            // subtext: '姓氏玫瑰图',
            left: 'center'
        },
        tooltip: {
            trigger: 'item',
            formatter: '{b} : {c}人(占{d}%)'
        },
        legend: {
            top: 'top',
            show: false
        },
        toolbox: {
            show: true,
            feature: {
                mark: { show: true },
                dataView: { show: true, readOnly: false },
                restore: { show: true },
                saveAsImage: { show: true }
            }
        },
        series: [
            {
                name: '姓氏',
                type: 'pie',
                radius: [10, 100],
                center: ['50%', '50%'],
                roseType: 'radius',
                label: {
                    show: true
                },
                emphasis: {
                    label: {
                        show: true
                    }
                },
                itemStyle: {
                    borderRadius: 110
                },
                data: compute_name(data,startyear, endyear)
            }
        ]
    };
    return option;
}
var pieChart = echarts.init(document.getElementById('pie_name'));
pieChart.setOption(compute_name_option(CBDBdata,startyear=1371, endyear=1610));
