var c=document.createElement("canvas");
var ctx=c.getContext("2d");
var img = document.getElementById("Image");
c.height=480;
c.width=640;
var workerCount = 0;
var data;
var ResultOfDecoding = document.getElementById("Result")

function receiveMessage(e) {
	if(e.data.success === "log") {
		console.log(e.data.result);
		return;
	}
	if(e.data.finished) {
		workerCount--;
		if(workerCount) {
			if(resultArray.length == 0) {
				DecodeWorker.postMessage({ImageData: data, Width: c.width, Height: c.height, cmd: "flip"});
			} else {
				workerCount--;
			}
		}
	}
	if(e.data.success){
		var tempArray = e.data.result;
		for(var i = 0; i < tempArray.length; i++) {
			if(resultArray.indexOf(tempArray[i]) == -1) {
				resultArray.push(tempArray[i]);
			}
		}
		ResultOfDecoding.innerHTML=resultArray.join("<br />");
	}
	if(workerCount == 0){
		if(resultArray.length === 0) {
			ResultOfDecoding.innerHTML="Decoding failed.";
		}else {
			ResultOfDecoding.innerHTML=resultArray.join("<br />");
		}
	}
}

var DecodeWorker = new Worker("/static/BarcodeReader/src/DecoderWorker.js");
DecodeWorker.onmessage = receiveMessage;
var resultArray = [];
var prev = document.getElementById("PreviousImage");
var next=document.getElementById("NextImage");
var decode = document.getElementById("Decode");
decode.addEventListener("click",Decode,false);
next.addEventListener("click",NextImage,false);
prev.addEventListener("click",PrevImage,false);
ImageCounter=0;
ImageList=["/static/BarcodeReader/sample/sample-milch.jpg"];
ImageList.reverse();
ImageList.slice().forEach( function(path) { new Image().src=path } );
function NextImage(){
	if(workerCount > 0) return;
	ResultOfDecoding.innerHTML='';
	resultArray = [];
	ImageList.push(img.src);
	img.src=ImageList.shift();
	ImageCounter++;
	ImageCounter = ImageCounter>ImageList.length ? 0 : ImageCounter;
}

function PrevImage(){
	if(workerCount > 0) return;
	ResultOfDecoding.innerHTML='';
	resultArray = [];
	ImageList.unshift(img.src);
	img.src=ImageList.pop();
	ImageCounter--;
	ImageCounter = ImageCounter<0 ? ImageList.length : ImageCounter;
}
function Decode() {
	if(workerCount > 0) return;
	workerCount = 2;
	ResultOfDecoding.innerHTML='';
	resultArray = [];
	ctx.drawImage(img,0,0,c.width,c.height);
	data = ctx.getImageData(0,0,c.width,c.height).data;
	DecodeWorker.postMessage({ImageData: data, Width: c.width, Height: c.height, cmd: "normal"});
}
