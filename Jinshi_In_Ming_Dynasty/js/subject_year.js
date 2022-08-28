var subject5_data = ["诗经", "书经", "易经", "礼记", "春秋"]
function compute_subject(data,startyear, endyear) {
 
    var subject_data = {}
    for (var i = 0; i < data.length; ++i) {
        year = data[i].年份
        subject = data[i].科目
        // if (startyear <= year && year <= endyear) {
            if (subject_data[subject] == null) {
                subject_data[subject] = {}

            }
            if (subject_data[subject][year] == null) {
                subject_data[subject][year] = 0
            }
            subject_data[subject][year]++;
            // console.log(subject+year)
        // }
    }
    series_data = []
    for (var j in subject5_data) {
        var subject = subject5_data[j]
        var x = { "type": "bar", "name": subject,"stack": "0","data":[] }

        for (var i = 0; i < year_list.length; ++i) {
            year = year_list[i]
            if (subject_data[subject])
                if (subject_data[subject][year])
                    x.data.push([i,subject_data[subject][year]])
                else x.data.push([i, 0])
            else x.data.push([i, 0])
        }
        series_data.push(x)
    }
    console.log(series_data)
    return series_data
}
function compute_subject_option(data,startyear, endyear) {
    var option_subject = {
        "animation": true,
        "animationThreshold": 2000,
        "animationDuration": 1000,
        "animationEasing": "cubicOut",
        "animationDelay": 0,
        "animationDurationUpdate": 300,
        "animationEasingUpdate": "cubicOut",
        "animationDelayUpdate": 0,
        "color": [
            
            "#ca8622",
            "#bda29a",
            "#6e7074",
            // "#546570",
            // "#c4ccd3",
            // "#f05b72",
            // "#ef5b9c",
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
            "#918597",
            "#c23531",
            "#2f4554",
            "#61a0a8",
            "#d48265",
            "#749f83",
        ],
        "series": compute_subject(data,startyear, endyear),
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
                "data": year_list
                // year_list.filter(function (year) {
                //     return startyear <= year && year <= endyear;
                // }),
            },
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
                "text": "科目",
                "padding": 5,
                "itemGap": 10
            }
        ],
        "dataZoom": [
            {
                "show": true,
                "type": "slider",
                "realtime": true,
                "start": 0,
                "end": 100,
                "orient": "horizontal",
                "zoomLock": false,
                "filterMode": "filter"
            },
        ]
    };
    return option_subject;
}
var chart_subject = echarts.init(
    document.getElementById('subject'), 'white', { renderer: 'canvas' });
var option_subject=compute_subject_option(CBDBdata,startyear=1371, endyear=1610);
chart_subject.setOption(option_subject);

var startyear=1371
var endyear=1610
chart_subject.on('datazoom', function (params) {
    rebuild()
    var obj = document.getElementById('title_year');
        obj.innerHTML = "公元"+Math.floor(startyear)+"至"+Math.floor(endyear)+"年"
    console.log(params)

});
var subject_filter={}
subject_filter.name='科目'
subject_filter.list=[]
chart_subject.on('legendselectchanged', function (params) {
    let name = params.name;
    console.log("legendselectchanged")
    if (!(subject_filter.list.includes(name))) {
        subject_filter.list.push(name);
    } else {
        subject_filter.list.forEach(function (item, index, arr) {
            if (item == name)
                arr.splice(index, 1);
        })
    }
    rebuild()
})