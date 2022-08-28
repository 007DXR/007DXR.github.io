function pad(num, n) {
	var len = num.toString().length;
	while (len < n) {
		num = "0" + num;
		len++;
	}
	return num;
}

function linechart(data, startDate, endDate, keyArray) {

	var linedata = [];
	for (var i = 1982; i <= 2014; i++) {
		let num = 0
		// let tot = 0
		for (var j = 0; j < data.length; j++) {
			var dataDate = new Date(data[j].Date.replace("/", "-").replace("/", "-"));
			// console.log(dataDate);
			if (dataDate.getFullYear() == i) {
				// num++;
				let flag = true
				for (let k in keyArray)
					if (data[j].Words.indexOf(keyArray[k]) == -1) {
						// num++;
						flag = false
						break
					}
				num += flag
			}
		}

		// if (tot == 0) tot = 1;
		linedata.push(num);
	}
	console.log(linedata);
	line_series = {
		type: 'line',
		data: linedata,
		smooth: true
	}
	lineChart.setOption({
		series: [line_series]
	});

}
var chartDom = document.getElementById('linechart');
var lineChart = echarts.init(chartDom);
var option = {
	tooltip: {
		trigger: 'axis',
		axisPointer: {
			type: 'shadow'
		}
	},
	legend: {},

	xAxis: [{
		// show:false
		name: '年份',
		type: 'category',
		axisTick: {
			show: false
		},
		data: [1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996,
			1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011,
			2012, 2013, 2014,
		]
	}],
	yAxis: [{
		name: '报道数',
		type: 'value',

	}],
	series: []
};
lineChart.setOption(option);
