var cat;
var url = window.location.search; //获取url中"?"符后的字串
if (url.indexOf("?") != -1) {  //判断是否有参数
	var str = url.substr(1); //从第一个字符开始 因为第0个是?号 获取所有除问号的所有符串
	strs = str.split("=");  //用等号进行分隔 （因为知道只有一个参数 所以直接用等号进分隔 如果有多个参数 要用&号分隔 再用等号进行分隔）
	cat = strs[1];     //直接弹出第一个参数 （如果有多个参数 还要进行循环的）
}

if (cat == "huasa") {
	$('#tujian-img').css("background-image", "url(image/huasa1.jpg)");
	$('#tujian-title').html('花洒');
	$('#furColor').html('三花');
	$('#sex').html('母');
	$('#health').html('健康');
	$('#ster').html('已绝育');
	$('#sterTime').html('2020-09-18');
	$('#character').html('怕人 安全距离1m以外');
	$('#looks').html('短毛三花 阴阳脸 白手套 后腿白');
}
if (cat == "jiaotang") {
	$('#tujian-img').css("background-image", "url(image/jiaotang1.jpg)");
	$('#tujian-title').html('焦糖');
	$('#furColor').html('玳瑁');
	$('#sex').html('母');
	$('#health').html('健康');
	$('#ster').html('已绝育');
	$('#sterTime').html('2016夏');
	$('#character').html('怕人 安全距离1m以外');
	$('#looks').html('黄黑相间 黄多 阴阳脸');
}
if (cat == "dawei") {
	$('#tujian-img').css("background-image", "url(image/dawei1.jpg)");
	$('#tujian-title').html('大威');
	$('#furColor').html('长毛三花');
	$('#sex').html('母');
	$('#health').html('健康');
	$('#ster').html('已绝育');
	$('#sterTime').html('2011-06-30');
	$('#character').html('薛定谔亲人');
	$('#looks').html('长毛三花 白肚皮白四肢 背部和尾巴黑黄分明的花色 绿眼睛 左耳耳缺');
}
if (cat == "shanhua") {
	$('#tujian-img').css("background-image", "url(image/shanhua1.jpg)");
	$('#tujian-title').html('山花');
	$('#furColor').html('三花');
	$('#sex').html('母');
	$('#health').html('健康');
	$('#ster').html('已绝育');
	$('#sterTime').html('2020-10-02');
	$('#character').html('怕人 安全距离1m以外');
	$('#looks').html('非常好看的三花 脸部和耳朵橘 左前腿黑狸 后前腿橘狸的花臂少女');
}
if (cat == "xiangbo") {
	$('#tujian-img').css("background-image", "url(image/xiangbo1.jpg)");
	$('#tujian-title').html('香波');
	$('#furColor').html('长毛橘白');
	$('#sex').html('公');
	$('#health').html('健康');
	$('#ster').html('已绝育');
	$('#sterTime').html('2021-01-02');
	$('#character').html('怕人 安全距离1m以外');
	$('#looks').html('长毛橘白 白多 橘尾巴 背上两大块橘');
}
if (cat == "jiangsiya") {
	$('#tujian-img').css("background-image", "url(image/jiangsiya1.jpg)");
	$('#tujian-title').html('姜丝鸭');
	$('#furColor').html('橘');
	$('#sex').html('公');
	$('#health').html('健康');
	$('#ster').html('已绝育');
	$('#sterTime').html('2019-10-11');
	$('#character').html('怕人 安全距离1m以内');
	$('#looks').html('表情很丧的胖橘');
}

if (cat == "dage") {
	$('#tujian-img').css("background-image", "url(image/dage1.jpg)");
	$('#tujian-title').html('大哥');
	$('#furColor').html('橘白');
	$('#sex').html('公');
	$('#health').html('健康');
	$('#ster').html('已绝育');
	$('#sterTime').html('2018-11-06');
	$('#character').html('亲人可抱');
	$('#looks').html('可爱的圆脸橘猫，白手套');
}
if (cat == "yimi") {
	$('#tujian-img').css("background-image", "url(image/yimi1.jpg)");
	$('#tujian-title').html('薏米');
	$('#furColor').html('长毛白');
	$('#sex').html('母');
	$('#health').html('健康');
	$('#ster').html('已绝育');
	$('#sterTime').html('2019-03-13');
	$('#character').html('怕人 安全距离1m以外');
	$('#looks').html('异瞳小白猫 蓝黄异瞳 右耳耳缺');
}
if (cat == "mianhuatang") {
	$('#tujian-img').css("background-image", "url(image/mianhuatang1.jpg)");
	$('#tujian-title').html('棉花糖');
	$('#furColor').html('白');
	$('#sex').html('公');
	$('#health').html('健康');
	$('#ster').html('已绝育');
	$('#sterTime').html('2012-03-23');
	$('#character').html('怕人 安全距离1m以外');
	$('#looks').html('又白又软好像棉花糖');
}
if (cat == "chayedan") {
	$('#tujian-img').css("background-image", "url(image/chayedan1.jpg)");
	$('#tujian-title').html('茶叶蛋');
	$('#furColor').html('黑');
	$('#sex').html('公');
	$('#health').html('健康');
	$('#ster').html('已绝育');
	$('#sterTime').html('2020-10-01');
	$('#character').html('吃东西时可以摸一下');
	$('#looks').html('短毛黑猫 黄眼睛');
}
if (cat == "yingjie") {
	$('#tujian-img').css("background-image", "url(image/yingjie1.jpg)");
	$('#tujian-title').html('英杰');
	$('#furColor').html('长毛奶牛');
	$('#sex').html('母');
	$('#health').html('健康');
	$('#ster').html('已绝育');
	$('#sterTime').html('2018夏');
	$('#character').html('薛定谔亲人');
	$('#looks').html('好看的长毛奶牛 白多 小胡子');
}
if (cat == "yifan") {
	$('#tujian-img').css("background-image", "url(image/yifan1.jpg)");
	$('#tujian-title').html('一帆');
	$('#furColor').html('奶牛');
	$('#sex').html('公');
	$('#health').html('健康');
	$('#ster').html('已绝育');
	$('#sterTime').html('2019-10-05');
	$('#character').html('薛定谔亲人');
	$('#looks').html('无情的警长');
}
if (cat == "chuzhu") {
	$('#tujian-img').css("background-image", "url(image/chuzhu1.jpg)");
	$('#tujian-title').html('出竹');
	$('#furColor').html('棕狸加白');
	$('#sex').html('公');
	$('#health').html('健康');
	$('#ster').html('已绝育');
	$('#sterTime').html('2017-04-24');
	$('#character').html('吃东西时可以一直摸');
	$('#looks').html('不太好分辨的混有黄色的狸纹 白围巾白手套');
}
if (cat == "zhumei") {
	$('#tujian-img').css("background-image", "url(image/zhumei1.jpg)");
	$('#tujian-title').html('竹妹');
	$('#furColor').html('棕狸加白');
	$('#sex').html('母');
	$('#health').html('健康');
	$('#ster').html('已绝育');
	$('#sterTime').html('2020-11-18');
	$('#character').html('怕人 安全距离1m以内');
	$('#looks').html('神似出竹的小脸狸花 总是一脸委屈');
}
// $('.tujian-right').animate({ height: 'toggle' }, 'fast');
$('.tujian-right').show();
// }
//);
// function showTujianRight(){
// 	$('.tujian-right').animate({height:'toggle'},'fast');
// }

$(function () {
	$(".cur").click(function () {
		$(".drop-right-content").hide();
		$(this).next().show();
	});
});
$(function () {
	$(".icon-heart").click(function () {
		$(this).css("fill","red");
		// $(this).next().show();
	});
});