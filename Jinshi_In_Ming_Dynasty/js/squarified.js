
var squarified_chart = echarts.init(document.getElementById('squarified'));

const formatUtil = echarts.format;
function getLevelOption() {
    return [
        {
            itemStyle: {
                borderWidth: 0,
                gapWidth: 5
            }
        },
        {
            itemStyle: {
                gapWidth: 1
            }
        },
        {
            colorSaturation: [0.35, 0.5],
            itemStyle: {
                gapWidth: 1,
                borderColorSaturation: 0.6
            }
        }
    ];
}
function compute_squrified_option(data,startyear , endyear) {
    var option = {
        title: {
            text: '籍贯',
            left: 'center'
        },
        tooltip: {
            formatter: function (info) {
                var value = info.value;
                var treePathInfo = info.treePathInfo;
                var treePath = [];
                for (var i = 1; i < treePathInfo.length; i++) {
                    treePath.push(treePathInfo[i].name);
                }
                return [
                    '<div class="tooltip-title">' +
                    formatUtil.encodeHTML(treePath.join('/')) +
                    '</div>',
                    '共' + formatUtil.addCommas(value) + '人'
                ].join('');
            }
        },
        series: [
            {
                name: '进士籍贯',
                type: 'treemap',
                visibleMin: 3000,
                label: {
                    show: true,
                    formatter: '{b}'
                },
                itemStyle: {
                    borderColor: '#fff'
                },
                levels: getLevelOption(),
                data: construct_si_data(data,startyear, endyear)
            }
        ]
    }
    return option;
}
function construct_xian_data(data_list) {
    var xian_data = [];
    var xian_dict = {};
    for (var id = 0; id < data_list.length; ++id) {
        var item = data_list[id];
        xian = item['县'];
        if (xian in xian_dict) {
            xian_data[xian_dict[xian]]['value'] += 1;
        } else {
            xian_dict[xian] = xian_data.length;
            xian_data.push({
                "name": xian,
                "value": 1
            })
        }
    }
    return xian_data;
}

function construct_fu_data(data_list) {
    var fu_data = []
    var fu_dict = {}
    for (var id = 0; id < data_list.length; ++id) {
        var item = data_list[id];
        var fu = item['府'];
        if (fu in fu_dict) {
            fu_data[fu_dict[fu]]['children'].push(item);
        } else {
            fu_dict[fu] = fu_data.length;
            fu_data.push({
                "name": fu,
                "children": [item]
            })
        }
    }
    for (var id = 0; id < fu_data.length; ++id) {
        fu_data[id]['children'] = construct_xian_data(fu_data[id]['children'])
    }
    return fu_data;
}

function construct_si_data(data_list,startyear, endyear) {
    var squarified_data = []
    var si_dict = {}
    for (var id in data_list) {
        var item = data_list[id];
        var si = item['司'];
        var year = data_list[id].年份

        if (startyear <= year && year <= endyear) {

            if (si in si_dict) {
                squarified_data[si_dict[si]]['children'].push(item)
            } else {
                si_dict[si] = squarified_data.length;
                squarified_data.push({
                    "name": si,
                    "children": [item]
                })
            }
        }
    }
    for (var i = 0; i < squarified_data.length; ++i) {
        squarified_data[i]['children'] = construct_fu_data(squarified_data[i]['children']);
    }
    return squarified_data;
}
var option_squarified=compute_squrified_option(CBDBdata,startyear=1371, endyear=1610)
squarified_chart.setOption(option_squarified);
