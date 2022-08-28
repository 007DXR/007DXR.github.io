function showResume(name) {
    for (let i in resume_data) {
        let person = resume_data[i]
        if (person.name == name) {
            let seriesList = resumeChart.getOption().series
            // let legendList=resumeChart.getOption().legend.data
            // console.log(resumeChart.getOption())
            seriesList.push(person)
            resumeChart.setOption({ series: seriesList })
            // legendList.push(name)
            // resumeChart.setOption({series:seriesList,legend:{data:legendList}})
        }

    }
}
function personCard(name) {
    d3.csv("data/EmployeeRecords.csv", function (csvdata) {

        // console.log(csvdata.FirstName+'.'+csvdata.LastName);
        if (csvdata.FirstName + '.' + csvdata.LastName == name) {
            let line = "<ul'>"
            for (let item in csvdata)
                if (csvdata[item]) {
                    line += "<li class='my_fav_list_li'>\
                    <div class='my_fav_list_p' >\
                    <div style='font-weight: bold;font-size:  15px;'>" + item + ' : ' + csvdata[item] +
                        '</div></div>\
                    </li>'
                }
            line += '</ul>'
            var html = "";
            html += "<div class='con'>";
            html += "<div id='msg'>";
            html += "<div class='info_message'>";

            html += "<div class='alertTitle'>Person Card</div>";
            html += "<div class='detail_message'>";
            html += line
            html += "</div><div id='alertCancel'>Cancel</div></div></div></div>"
            $('body').append(html);
        }
        $('#alertCancel').click(function () {
            $("#msg").remove();
            $('.con').remove();
        })
    });
    showResume(name)
}
function emailCard(data) {
    let line = '<h3>From ' + data.source + ' to ' + data.target + ':</h5><ul>'
    for (let item in email_data) {
        if (data.source == email_data[item].From && data.target == email_data[item].To) {
            line += "<li class='my_fav_list_li'>\
            <div class='my_fav_list_p' >\
            <div style='font-weight: bold;font-size:  15px;'>" + email_data[item].date + '</div>' + email_data[item].Subject +
                '</div>\
            </li>'
            // line += '<li>' + email_data[item].date + ' ' + email_data[item].Subject + '</li>'

        }
    }
    line += '</ul>'
    var html = "";
    html += "<div class='con'>";
    html += "<div id='msg'>";
    html += "<div class='info_message'>";

    html += "<div class='alertTitle'>Email Card</div>";
    html += "<div class='detail_message'>";
    html += line
    html += "</div><div id='alertCancel'>Cancel</div></div></div></div>"
    $('body').append(html);
    $('#alertCancel').click(function () {
        $("#msg").remove();
        $('.con').remove();
    })
    showResume(data.source)
    showResume(data.target)

}
