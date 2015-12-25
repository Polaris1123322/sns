// JavaScript Document
var tq_width;
var tq_height;
var tqhtml;  //弹窗的全部内容
var sw;    //弹窗参数
//浏览器的宽高
wh();
function wh() {
	tq_width=$(window).width(); 
	tq_height=$(window).height(); 
}
function wintq_q() {
	$('#wintq').css({'left':(tq_width/2)-$('#wintq').width()/2+'px','top':(tq_height/2)-($('#wintq').height()/2+50)+'px'});
	$('#zbody').css({'width':tq_width+'px','height':tq_height+'px'});
}
function zbody() {
	$('body').append('<div id="zbody"></div>');
	wintq_q();
}
//弹窗函数
function wintq(text,sw,setOut,url) {
	$('#wintq').remove();
	//1代表成功,2代表提示,3代表失败
	if (sw==1) {
		tqhtml='<div id="wintq"><div class="tqLeft"></div><div class="tqCenter">'+text+'</div><div class="tqRight"></div></div>';
	}else if (sw==2) {
		tqhtml='<div id="wintq"><div class="tqLeft2"></div><div class="tqCenter">'+text+'</div><div class="tqRight"></div></div>';
	}else if (sw==3) {
		tqhtml='<div id="wintq"><div class="tqLeft3"></div><div class="tqCenter">'+text+'</div><div class="tqRight"></div></div>';
	}
	$('body').append(tqhtml);
	wintq_q();
	$('#wintq').hide();
	$('#wintq').fadeIn('fast');
	setTimeout(function() {
		$('#wintq').fadeOut('fast',function() {
			$('#wintq').remove();
			//判断是否有地址跳转
			if (url!='') {
				location.href=url;
			}
		});
	},setOut);
}

$(window).resize(function() {
	wh();
	wintq_q();
});
//关闭重新加载
function popclose() {
	$('#iframe_pop .pop_close').click(function() {
		window.location.reload();
	});
}