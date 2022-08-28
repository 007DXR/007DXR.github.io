
var huji5_data = ["民籍", "军籍",  "官籍", "匠籍", "灶籍",]
function compute_huji(data) {
  
    var huji_data = {}
    for (var i = 0; i < data.length; ++i) {
        year = data[i].年份
        huji = data[i].户籍      
        if (huji_data[huji] == null) {
            huji_data[huji] = {}

        }
        if (huji_data[huji][year] == null) {
            huji_data[huji][year] = 0
        }
        huji_data[huji][year]++;
    }
    series_data = []
    for (var j in huji5_data) {
        var huji = huji5_data[j]
        var x = { "type": "line", "name": huji }

        x.data = []

        for (var i = 0; i < year_list.length; ++i)
        {
            year = year_list[i]
            if (huji_data[huji])
                if (huji_data[huji][year])
                    x.data.push([i, huji_data[huji][year]])
                else x.data.push([i, 0])
            else x.data.push([i, 0])

        }
        series_data.push(x)
    }
    console.log(series_data)
    return series_data
}
function compute_huji_option(data,startyear, endyear) {

    var option_huji = {
        "animation": true,
        "animationThreshold": 2000,
        "animationDuration": 1000,
        "animationEasing": "cubicOut",
        "animationDelay": 0,
        "animationDurationUpdate": 300,
        "animationEasingUpdate": "cubicOut",
        "animationDelayUpdate": 0,
        "color": [
            "#c23531",
            "#2f4554",
            // "#61a0a8",
            // "#d48265",
            "#749f83",
            "#ca8622",
            // "#bda29a",
            // "#6e7074",
            // "#546570",
            "#c4ccd3",
            "#f05b72",
            "#ef5b9c",
            "#f47920",
            "#905a3d",
            "#fab27b",
            "#2a5caa",
            "#444693",
            "#726930",
            "#b2d235",
            "#6d8346",
            "#ac6767",
            "#1d953f",
            "#6950a1",
            "#918597"
        ],
        "series": compute_huji(data,startyear, endyear),
        "legend": [
            {

                "show": true,
                "padding": 5,
                "itemGap": 10,
                "itemWidth": 25,
                "itemHeight": 14
            }
        ],
        "tooltip": {
            "show": true,
            "trigger": "axis",
            "triggerOn": "mousemove|click",
            "axisPointer": {
                "type": "line"
            },
            "showContent": true,
            "alwaysShowContent": false,
            "showDelay": 0,
            "hideDelay": 100,
            "textStyle": {
                "fontSize": 14
            },
            "borderWidth": 0,
            "padding": 5,

        },
        toolbox: {
            show: true,
            feature: {
                mark: { show: true },
                dataView: { show: true, readOnly: false },
                magicType: { show: true, type: ['line', 'bar', 'stack', 'tiled'] },
                restore: { show: true },
                saveAsImage: { show: true }
            }
        },
        "xAxis": [
            {
                "name": "年份",
                "type": "category",
                "show": true,
                "scale": false,
                "nameLocation": "end",
                "nameGap": 15,
                "gridIndex": 0,
                "inverse": false,
                "offset": 0,
                "splitNumber": 5,
                "boundaryGap": false,
                "minInterval": 0,
                "splitLine": {
                    "show": false,
                    "lineStyle": {
                        "show": true,
                        "width": 1,
                        "opacity": 1,
                        "curveness": 0,
                        "type": "solid"
                    }
                },
                "data": year_list
            }
        ],
        "yAxis": [
            {
                "name": "进士数量",
                "type": "value",
                "show": true,
                "scale": false,
                "nameLocation": "end",
                "nameGap": 15,
                "gridIndex": 0,
                "axisTick": {
                    "show": true,
                    "alignWithLabel": false,
                    "inside": false
                },
                "inverse": false,
                "offset": 0,
                "splitNumber": 5,
                "minInterval": 0,
                "splitLine": {
                    "show": true,
                    "lineStyle": {
                        "show": true,
                        "width": 1,
                        "opacity": 1,
                        "curveness": 0,
                        "type": "solid"
                    }
                }
            }
        ],
        "title": [
            {
                "text": "户籍",
                "padding": 5,
                "itemGap": 10
            }
        ],
        "dataZoom": [
            {
                "show": false,
                "type": "slider",
                "realtime": true,
                "start": 0,
                "end": 100,
                "orient": "horizontal",
                "zoomLock": false,
                "filterMode": "filter"
            },
        ]
    }
    return option_huji;
};

var chart_huji = echarts.init(
    document.getElementById('huji'), 'white', { renderer: 'canvas' });
var option_huji= compute_huji_option(CBDBdata,startyear=1371, endyear=1610)
chart_huji.setOption(option_huji);

var huji_filter={}
huji_filter.name='户籍'
huji_filter.list=[]
chart_huji.on('legendselectchanged', function (params) {
    let name = params.name;
    if (!(huji_filter.list.includes(name))) {
        huji_filter.list.push(name);
    } else {
        huji_filter.list.forEach(function (item, index, arr) {
            if (item == name)
                arr.splice(index, 1);
        })
    }
    rebuild()
})