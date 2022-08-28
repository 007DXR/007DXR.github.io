let _width = $(window).width();
let _height = $(window).height();
let width = 0.9 * _width;
let height = 0.9 * _height;
chart_svg = d3.select("#container")
              .append("svg");
function showNewsList (data, startDate, endDate, keyArray) {
	// console.log(startDate);
	// console.log(endDate);
	// console.log(keyArray);
	var showNews = [];
	var unshowNews = [];
	var selectNews = [];
	var newsNum;
	var Name = ["Homeland Illumination","Kronos Star","The World","Abila Post","The Abila Post","International Times"];
	for (var i = 0; i<data.length; i++) {
		var dataDate = new Date(data[i].Date.replace("/", "-").replace("/", "-"));
		ans=0;
		for(var j = 0; j<Name.length;j++){
			if (data[i].Media==Name[j])ans=1;
		}
		if (dataDate >= startDate && dataDate <= endDate&&ans==1) {
			selectNews.push(data[i]);
		}
	}
	for (var i = 0; i<keyArray.length; i++) {
		newsNum = 0;
		for (var j = 0; j < selectNews.length; j++) {
			if (selectNews[j].Words.indexOf(keyArray[i]) > -1) {
				showNews.push(selectNews[j]);
				newsNum += 1;
			}
			else {
				unshowNews.unshift(selectNews[j]);
			}
		}
		selectNews = showNews;
		showNews = [];
	}
	var newsList = document.getElementById('showlist');
	newsList.innerHTML="";
	for (i in selectNews) {
		article = selectNews[i];
		html = document.createElement('li');
		html.setAttribute('class','my_fav_list_li');
		elea = document.createElement('p');
		elea.setAttribute('class', 'my_fav_list_p');
		if(article['Time']!=-1 && article['Time']!="")elea.innerText =article['Time']+'-'+article['Content'];
		else elea.innerText = article['Title'];
		elea.data = article;
		elea.onclick = function(){showContent(this)};
		html.appendChild(elea);
		newsList.appendChild(html);
	}
	var listTitle = document.getElementsByClassName("fav_list_title_h3")[0];
	listTitle.onclick = function(){showKeywords(startDate, endDate, keyArray)};
}

function showContent (obj) {
	var objStr = "Media: "+obj.data.Media;
	objStr += "\n"+"Title: "+obj.data.Title;
	objStr += "\n"+"Date: "+obj.data.Date;
	objStr += "\n"+"Time: "+obj.data.Time;
	objStr += "\n"+"Content: "+obj.data.Content;
	$("#msg").remove();
	$('.con').remove();
	myalert(objStr);
}

function showKeywords (startDate, endDate, keywords) {
	alert("start: "+startDate.toLocaleString().split(" ")[0]+"\nend: "+endDate.toLocaleString().split(" ")[0]+"\nkeywords: "+keywords);
}

function myalert(e){
    var html="";
    	html+="<div class='con'>";
		html+="<div id='msg'>";
    	html+="<div class='info_message'>";
    	html+="<div class='alertTitle'>Detailed News</div>";
    	html+="<p class='detail_message'>"+e+"</p>";
    	html+="</div><div id='alertCancel'>Cancel</div></div></div>"
    $('body').append(html);
	// console.log(html);
    $('#alertCancel').click(function(){
    	$("#msg").remove();
    	$('.con').remove();
    })
}