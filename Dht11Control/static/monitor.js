//获取网络信息
$(document).ready(function(){

	getInfoN();

	setInterval(function(){
		getInfoN();
		myChart.update();
	},1000)

	function getInfoN(){
		$.ajax({
			type: 'GET',
			url:$SCRIPT_ROOT + '/tmp_info',
			success:function(data){
				updateData(data.tmp, data.hum);
		}
		});
	};

	var momentList = new Array();
	for (var i=30; i>0; i--)
	{
		momentList[i-1] = moment().subtract(30-i, "seconds").format("HH:mm:ss");
	};
  
	var recvList = new Array(30);
	var sentList = new Array(30);

	function updateData(tmp, hum){
		recvList.shift();
		recvList.push(tmp);

		sentList.shift();
		sentList.push(hum);
	};

	var data = {
		labels: momentList,
		datasets: [
			{
				label: "温度",
				fill: false,
				pointColor: "rgba(220,220,220,1)",
				borderColor: "rgb(250,95,126)",
				data: recvList
			},
			{
				label: "湿度",
				fill: false,
				pointColor: "rgba(220,220,220,1)",
				borderColor: "rgb(72,134,255)",
				data: sentList
			}
		]
	};

	var options = {
		responsive: false,
		legend: {
			display: false			
		},
		scales: {
			xAxes: [{
				position: 'right',
				gridLines: {
					color: "rgba(0,0,0,0)",
				},
				type: 'time',
				time: {
					parser: "HH:mm:ss",
					unit: 'second',
					unitStepSize: 5,
					displayFormats: {
						'minute': 'HH:mm:ss', 
						'hour': 'HH:mm:ss', 
						min: moment(),
						max: moment().subtract(30, "seconds")    
					},
				},
			}],
			yAxes: [{
				gridLines: {
					drawBorder: false,
				},
				ticks: {
					beginAtZero: true,
					display: false,
				}	
			}]
		}
	};

	var netGraph =  document.getElementById("net-graph");
	var ngc = netGraph.getContext("2d");


// 初始化
	var myChart = new Chart(ngc, {
		type: 'line',
		data: data,
		options: options
	})
});


