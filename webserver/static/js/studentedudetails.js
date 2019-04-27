$(document).ready(function(){
	$('#sub-btn').on('click',function(){
	let coname=$("#co-name").val();
	let name=$("#name").val();
	let age=$("#age").val();
	let tenthmarks=$("#ten").val();
	let pumarks=$("#pumarks").val();
	let degree=$("#degree").val();
	let coursename=$("#course").val();
	let aggregate=$("#aggregate").val();
	let aboutme=$("#abut-me").val();
	let skills=$("#skills").val();
	let resume=$("#resume").val();
	var data={};
	data["company_name"]=coname;
	data["stu_name"]=name;
	data["age"]=age;
	data["sslx_percent"]=tenthmarks;
	data["pu_percent"]=pumarks;
	data["degree"]=degree;
	data["course_name"]=coursename;
	data["aggregate"]=aggregate;
	data["about_me"]=aboutme;
	data["skills"]=skills;
	data["resume"]=resume;

	$.ajax({
		method:"POST",
		url:http:"//127.0.0.1:8000/api/applyjobs"
		type:'application/json',
		data:data,
		success:function(response){
			console.log(response);
			window.localStorage['token']=response['token'];
			window.location.href="/sdashboard/";
			 alert(response.alert);
		}
	});
	});