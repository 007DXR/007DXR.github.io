
var chartDom = document.getElementById('resume');
var resumeChart = echarts.init(chartDom);
var option = {
  tooltip: {
    trigger: 'axis',
    axisPointer: {
      type: 'shadow'
    }
  },
  legend: {
    // data: []
  },
  toolbox: {
    // show: false,
    orient: 'vertical',
    left: 'right',
    top: 'center',
    feature: {
      mark: { show: true },
      dataView: { show: true, readOnly: false },
      //   magicType: { show: true, type: ['line', 'bar', 'stack'] },
      restore: { show: true },
      saveAsImage: { show: true }
    }
  },
  xAxis: [
    {
      type: 'category',
      axisTick: { show: false },
      data: ['1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013',]
    }
  ],
  yAxis: [
    {
      type: 'category',
      data: [
        'else', 'Kronos Armed\nForces', 'Kronos\nGASTech', 'Tethys Defense\nForces', 'Tethys\nLtd.', 'Abila Community\nCollege'
      ]
    }
  ],
  series: [{
    "name": "Rachel.Pantanal",
    "type": "line",
    "data": [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        2
    ]
},{
  "name": "Isia.Vann",
  "type": "line",
  "data": [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      5,
      5,
      1,
      1,
      2,
      2,
      2,
      2,
      2,
      2,
      2
  ]
},{
  "name": "Stenig.Fusil",
  "type": "line",
  "data": [
      0,
      0,
      0,
      0,
      0,
      0,
      4,
      4,
      4,
      4,
      4,
      4,
      4,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2
  ]
},]
};
resumeChart.setOption(option);
