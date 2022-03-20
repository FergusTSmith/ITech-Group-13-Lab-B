<script type="text/javascript">
	function GI(id) {
		return document.getElementById(id);
	}
	function infen(var1) {
		var fentip = new Array("", "waste time", "waste time more", "dislike", "dislike", "normal", "normal", "normal", "like", "like", "fantacy");
		if (var1 > 0) {
			GI("pfno").innerHTML = var1 + "scores ";
			GI("pftip").innerHTML = fentip[var1];
			GI("currentrating").style.display = "none";
		}
		else {
			GI("pfno").innerHTML = "";
			GI("pftip").innerHTML = "";
			GI("currentrating").style.display = "block";
		}
	}

	var http_request = false;
	function makeRequest(url, functionName, httpType, sendData) {
		http_request = false;
		if (!httpType) httpType = "POST";
		if (window.XMLHttpRequest) { // Non-IE...
			http_request = new XMLHttpRequest();
			if (http_request.overrideMimeType) {
				http_request.overrideMimeType('text/plain');
			}
		} else if (window.ActiveXObject) { // IE
			try {
				http_request = new ActiveXObject("Msxml2.XMLHTTP");
			} catch (e) {
				try {
					http_request = new ActiveXObject("Microsoft.XMLHTTP");
				} catch (e) { }
			}
		}
		if (!http_request) {
			alert('failed');
			return false;
		}
		var changefunc = "http_request.onreadystatechange = " + functionName;
		eval(changefunc);
		//http_request.onreadystatechange = alertContents;
		http_request.open(httpType, url, true);
		http_request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
		http_request.send(sendData);
	}
	function getReturnedText() {
		if (http_request.readyState == 4) {
			if (http_request.status == 200) {
				var messagereturn = http_request.responseText;
				return messagereturn;
			} else {
				alert('requests wrong');
			}
		}
	}
	function EchoReturnedText() {
		if (http_request.readyState == 4) {
			if (http_request.status == 200) {
				var messagereturn = http_request.responseText;
				if (messagereturn != 'isfail') {
					var r;
					r = messagereturn.split('|');
					if (r.length != 1) {
						if (r[0] == "8") {
							alert("success,tks!")
							GI("pfshi").innerHTML = r[1];
							GI("pfge").innerHTML = r[2];
							GI("pfren").innerHTML = r[3];
							GI("currentrating").style.width = r[4] + "px";
						}
					}
					else {
						if (messagereturn == "1") {
							alert("already done")
						}
						else if (messagereturn == "2") {
							alert("failed,try later")
						}
						else if (messagereturn == "3") {
							alert("short time limitted")
						}
						else {
							alert(messagereturn);
						}
						//document.getElementById('ajaxarea').innerHTML=messagereturn;
					}
				}
			} else {
				alert('wrong');
			}
		}
	}
</script>