// var myChart = echarts.init(document.getElementById('word_cloud'))


// var options = {
//     title: {
//         text: '词云图'
//     },
//     series: [{
//         type: 'wordCloud',
//         shape: 'circle',

//         left: 'center',
//         top: 'center',
//         width: '70%',
//         height: '80%',
//         right: null,
//         bottom: null,

//         sizeRange: [12, 60],

//         rotationRange: [-90, 90],
//         rotationStep: 45,
//         gridSize: 8,
//         drawOutOfBound: false,

//         textStyle: {
//             normal: {
//                 fontFamily: 'sans-serif',
//                 fontWeight: 'bold',
//                 color: function () {
//                     return 'rgb(' + [
//                         Math.round(Math.random() * 160),
//                         Math.round(Math.random() * 160),
//                         Math.round(Math.random() * 160)
//                     ].join(',') + ')';
//                 }
//             },
//             emphasis: {
//                 shadowBlur: 10,
//                 shadowColor: '#333'
//             }
//         },
//     }]
// }

function generate_wordcloud(start_year=1982, end_year=2014, num = 50)
{
    // console.log(data)
    let length = data.length
    let wordcloud_data = []
    let count_dict = {}
    for (i = 0; i < length; ++i){
        item = data[i]
        year = parseInt(item['Year'])
        dic = item['Count']
        if (year < start_year || year > end_year)
            continue
        for (var key in dic) {
            if (count_dict.hasOwnProperty(key)) {
                count_dict[key]+=dic[key]
            }
            else {
                count_dict[key] = dic[key]
            }
        }
    }
    // console.log(count_dict)
    let keys = Object.keys(count_dict).sort(function (a, b) { return count_dict[b] - count_dict[a];})
    let len = keys.length

    for (let i = 0; i < num; ++i){
        k = keys[i]
        wordcloud_data.push({'text': k, 'value': count_dict[k]})
    }
    return wordcloud_data;
}
