function filter_data(data, filter) {
    res = [];
    // console.log(filter["年份"])
    for (item in data) {
        var tag = true;
        for (var key in filter) {
            if (key == "年份") {
                let year = filter[key];
                if (year.length == 0) {
                    if (data[item][key] != year[0]) {
                        tag = false;
                        break;
                    }
                } else {
                    if (data[item][key] < year[0] || data[item][key] > year[1]) {
                        tag = false;
                        break;
                    }
                }
            } else {
                if (!(filter[key].includes(data[item][key]))) {
                    tag = false;
                    break;
                }
            }
        }
        if (tag) {
            res.push(data[item])
        }
    }
    return res
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

function construct_si_data(data_list) {
    var squarified_data = []
    var si_dict = {}
    for (var id in data_list) {
        var item = data_list[id];
        var si = item['司'];
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
    for (var i = 0; i < squarified_data.length; ++i) {
        squarified_data[i]['children'] = construct_fu_data(squarified_data[i]['children']);
    }
    return squarified_data;
}

function construct_pie_data(data_list, flag) {
    let pie_data = [];
    let name_dict = {};
    let legend;
    if (flag == "户籍") {
        legend = ["民籍", "军籍", "监籍", "官籍", "匠籍", "灶籍", "站籍"];
    }
    if (flag == "科目") {
        legend = ["诗经", "书经", "易经", "礼记", "春秋"];
    }
    for (var i = 0; i < legend.length; ++i) {
        let name = legend[i];
        name_dict[name] = pie_data.length;
        pie_data.push({
            'name': name,
            'value': ''
        });
    }
    for (var i = 0; i < data_list.length; ++i) {
        let item = data_list[i][flag];
        if (pie_data[name_dict[item]]['value'] == '')
            pie_data[name_dict[item]]['value'] = 1;
        else
            pie_data[name_dict[item]]['value'] += 1;
    }
    return pie_data;
}

function construct_dataset(data_list, flag) {
    let dataset = [];
    let year_dict = {};
    let legend;
    if (flag == "户籍") {
        legend = ["年份","民籍", "军籍", "监籍", "官籍", "匠籍", "灶籍", "站籍"];
    }
    if (flag == "科目") {
        legend = ["年份","诗经", "书经", "易经", "礼记", "春秋"];
    }
    let attr_dict = {};
    for (let i = 0; i < legend.length; ++i)
        attr_dict[legend[i]] = i;
    for (let i = 0; i < data_list.length; ++i){
        let year = data_list[i]['年份'];
        let attr = data_list[i][flag];
        if (!(year in year_dict)) {
            year_dict[year] = dataset.length;
            dataset.push([]);
            dataset[year_dict[year]].push(year);
            for (let i = 0; i < legend.length; ++i)
                dataset[year_dict[year]].push(0);
            dataset[year_dict[year]][attr_dict[attr]] += 1;
        }
        else {
            dataset[year_dict[year]][attr_dict[attr]] += 1;
        }
    }
    dataset.sort();
    dataset.unshift(legend);
    console.log(dataset)
    return dataset;
}