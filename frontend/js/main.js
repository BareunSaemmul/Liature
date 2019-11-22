$(window).load(function(){
	var sidebar = document.getElementById("sidebar")
	var sidebarToggleWrap = document.getElementById("sidebarToggleWrap");
	var container = document.getElementsByClassName("container")[0];

	sidebarToggle.addEventListener("click", () => {
		sidebarToggleWrap.classList.toggle("open-sidebar");
		sidebar.classList.toggle("open-sidebar");
		container.classList.toggle("open-sidebar");
	});

	var chatSendContent = document.getElementById('chatSendContent');
	var chatSendButton = document.getElementById('chatSendButton');

	chatSendButton.addEventListener('click', () => {
		if( chatSendContent.value == '' || chatSendContent.value == ' ') {
			return
		}
		var chatMsgWrap = document.createElement('div');
		var chatMsg2 = document.createElement('div');
		var chatContent = document.createTextNode(chatSendContent.value);
		var buf = chatSendContent.value;
		chatMsgWrap.classList.add('chat-msg-wrap');
		chatMsg2.classList.add('chat-msg2');

		chatMsg2.appendChild(chatContent);
		chatMsgWrap.appendChild(chatMsg2);

		document.getElementsByClassName('chat-box-msg')[0].appendChild(chatMsgWrap);
		
		document.getElementById('chatSendContent').value = '';
		///////////////////////////////////////////////////////////
		var result = Math.floor(Math.random() * 3) + 1;
		var resultMsg = Math.floor(Math.random() * 8);
		var msgList = [
			"부억에서 접시가 떨어져서 깨졌어요",
			"처음 지진을 겪어서 엄청 놀랐어요",
			"대박, 갑자기 흔들려",
			"지구가 이렇게 망하는 건가요",
			"우리나라에서 지진이?",
			"밖에서 차가 갑자기 흔들렸어",
			"영화보다가 지진나서 4D인 줄 알았어요",
			"지진 때문에 집에 금 갔어요",
		]
		setTimeout(function() {
			var chatMsgWrap = document.createElement('div');
			var chatMsg2 = document.createElement('div');
			if(buf == '지진 나서 놀랐어요') {
				var chatContent = document.createTextNode("그래도 약한 지진이라 다행이네요");
			} else if (buf == '다들 놀랐을텐데 힘내세요') {
				var chatContent = document.createTextNode("감사합니다");
			} else if (buf == '우리나라에서도 지진이 일어나다니') {
				var chatContent = document.createTextNode("아직 우리나라가 안전지대는 아닌가봐요");
			} else {
				var chatContent = document.createTextNode(msgList[resultMsg]);
			}

			chatMsgWrap.classList.add('chat-msg-wrap');
			chatMsg2.classList.add('chat-msg1');

			chatMsg2.appendChild(chatContent);
			chatMsgWrap.appendChild(chatMsg2);

			document.getElementsByClassName('chat-box-msg')[0].appendChild(chatMsgWrap);
			
			document.getElementById('chatSendContent').value = '';
		  }, result * 1000);
	});
	/*
	$("[data-toggle]").click(function() {
	  var toggle_el = $(this).data("toggle");
	  $(toggle_el).toggleClass("open-sidebar");
	});
	 $(".swipe-area").swipe({
		   swipeStatus:function(event, phase, direction, distance, duration, fingers){
				 if (phase=="move" && direction =="right") {
					   $(".container").addClass("open-sidebar");
					   return false;
				 }
				 if (phase=="move" && direction =="left") {
					   $(".container").removeClass("open-sidebar");
					   return false;
				 }
		   }
	 }); 
	 */
});