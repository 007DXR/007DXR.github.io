function filter_data(data, filter) {
    res = [];
    // console.log(data)
    for (var j in data) {
        var tag = true;
        var item=data[j]
        for (var i in filter.list) 
            if (filter.list[i]==item[filter.name])
                tag=0
            
        if (tag) {
            res.push(item)
        }
    }
    return res
}
function all_filter(){

    redata =filter_data(CBDBdata,huji_filter)
    redata =filter_data(redata,subject_filter)
    // redata =filter_data(redata,name_filter)
    // redata =filter_data(redata,huji_filter)
    return redata
}
function rebuild()
{
    console.log("rebuild")
    redata=all_filter()
    startyear =chart_subject.getModel().option.dataZoom[0].startValue;
    endyear = chart_subject.getModel().option.dataZoom[0].endValue;
    startyear=year_list[startyear]
    endyear=year_list[endyear]
console.log(startyear,endyear)
    option_huji.dataZoom[0].start = chart_subject.getModel().option.dataZoom[0].start;
    option_huji.dataZoom[0].end = chart_subject.getModel().option.dataZoom[0].end;
    option_huji.series=compute_huji(redata,startyear, endyear)
    chart_huji.setOption(option_huji)

    option_subject.series=compute_subject(redata,startyear, endyear)
    option_subject.dataZoom[0].start = chart_subject.getModel().option.dataZoom[0].start;
    option_subject.dataZoom[0].end = chart_subject.getModel().option.dataZoom[0].end;
    chart_subject.setOption(option_subject)
    // chart_subject.setOption({series:compute_subject(redata,startyear, endyear)});
    pieChart.setOption({series: [{
        data: compute_name(redata,startyear, endyear),
    }]});

    option_squarified.series[0].data=construct_si_data(redata,startyear, endyear)
    squarified_chart.setOption(option_squarified);
}
