function emailNode(strartTime, endTime, strartDay, endDay)
// 先时间，再日期
{
    let boolLink = {}
    let boolNode = {}
    for (var i = 0; i < email_data.length; ++i) {
        let item = email_data[i]
        // console.log(item)
        if (strartDay <= item.day && item.day <= endDay)
            if (strartTime <= item.detailTime && item.detailTime <= endTime) {
                if (boolNode[item.From] == null)
                    boolNode[item.From] = 0
                if (boolNode[item.To] == null)
                    boolNode[item.To] = 0
                boolNode[item.From] += 1
                boolNode[item.To] += 1
                if (boolLink[item.From] == null) {
                    boolLink[item.From] = {}

                }
                if (boolLink[item.From][item.To] == null) {
                    boolLink[item.From][item.To] = 0;
                }
                boolLink[item.From][item.To] += 1
            }
    }
    console.log(boolLink)
    let graph_link = []
    let graph_node = []
    let tmp = []
    for (var i = 0; i < emailNode_data.length; ++i) {
        var node = emailNode_data[i]
        // sumNode+=(boolNode[node.name]!=null)
        if (boolNode[node.name])
            tmp.push(boolNode[node.name])
    }
    // 从小到大排序
    tmp.sort(function (a, b) {
        return a - b
    })
    let size = Math.min(tmp.length, 40)
    let midValue = tmp[tmp.length - size]
    for (var i = 0; i < emailNode_data.length; ++i) {
        var node = emailNode_data[i]
        if (boolNode[node.name] >= midValue) {
            node.value = boolNode[node.name]
            node.symbolSize = Math.sqrt(node.value / midValue) * 15
            graph_node.push(node)
            // console.log(node)
        } else boolNode[node.name] = null
        // console.log(node,boolNode[node.name])

    }
    for (let From in boolLink)
        if (From in boolNode) {
            let mx = 0
            for (let To in boolLink[From])
                if (To in boolNode)
                    mx = Math.max(mx, boolLink[From][To])
            mx = Math.sqrt(mx) 
            for (let To in boolLink[From])
                if ((To in boolNode) && boolLink[From][To] >= mx) {

                    item = {
                        "source": From,
                        "target": To,
                        "value": boolLink[From][To]
                    };
                    graph_link.push(item)
                }
        }

    return [graph_link, graph_node];
}

function compute_option(start_time, end_time, start_day, end_day) {
    let option = {
        xAxis: {
            data: [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
            name: '日期',
            type: 'category',
            splitLine: {
                show: false
            },
    
            axisLabel: {
                formatter: '1/{value}/2014'
            }
        },
        yAxis: {
            min: 0,
            max: 24 * 60,
            name: '时刻',
            type: 'value',
            splitLine: {
                show: false
            },
    
            axisLabel: {
    
                formatter: function (value) {
                    return parseInt(value / 60) + ':' + parseInt(value) % 60;
                }
            }
        },
        dataZoom: [
            {
                type: 'slider',
                xAxisIndex: 0,
                filterMode: 'none',
                labelFormatter: '1/{value}/2014'
            },
            {
                left: "0%",
                type: 'slider',
                yAxisIndex: 0,
                filterMode: 'none',
                labelFormatter: function (value) {
                    return parseInt(value / 60) + ':' + parseInt(value) % 60;
                }
            }
        ],
    
        "color": [
            "#c23531",
            "#2f4554",
            "#61a0a8",
            "#d48265",
            "#749f83",
            "#ca8622",
            "#bda29a",
            "#6e7074",
            "#546570",
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
        "series": [
            {
                "type": "graph",
                "layout": "force",
                // "symbolSize": 10,
                "circular": {
                    "rotateLabel": false
                },
                "force": {
                    "repulsion": 2000,
                    "edgeLength": [
                        5,
                        20
                    ],
                    "gravity": 2
                },
                "label": {
                    "show": true,
                    "position": "top",
                    "margin": 8
                },
                "lineStyle": {
                    "show": true,
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0.2,
                    "type": "solid"
                },
                "roam": true,
                "draggable": false,
                "focusNodeAdjacency": true,

                "categories": [
                    {
                        "name": "Administration"
                    },
                    {
                        "name": "Engineering"
                    },
                    {
                        "name": "Executive"
                    },
                    {
                        "name": "Facilities"
                    },
                    {
                        "name": "Information Technology"
                    },
                    {
                        "name": "Security"
                    }
                ],
                "edgeLabel": {
                    "show": false,
                    "position": "top",
                    "margin": 8,
            // formatter: '{value}/2014'

                },
                "edgeSymbol": [
                    null,
                    null
                ],

                "links": emailNode(start_time, end_time, start_day, end_day)[0],
                "data": emailNode(start_time, end_time, start_day, end_day)[1],
            }
        ],
        "legend": [
            {
                "data": [
                    "Administration",
                    "Engineering",
                    "Executive",
                    "Facilities",
                    "Information Technology",
                    "Security"
                ],
                "selected": {
                    "Administration": true,
                    "Engineering": true,
                    "Executive": true,
                    "Facilities": true,
                    "Information Technology": true,
                    "Security": true
                },
                "show": true,
                "padding": 5,
                "itemGap": 10,
                "itemWidth": 25,
                "itemHeight": 14
            }
        ],
        "tooltip": {
            "show": true,
            "trigger": "item",
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
            "padding": 5
        },
        "title": [
            {
                // "text": "Email \nRelationship",
                "padding": 5,
                "itemGap": 10
            }
        ]
    };
    return option;
}