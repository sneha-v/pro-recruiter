$(document).ready(function(){
	$('#su-btn').on('click',function(){
	let name=$("#name").val();
	let location=$("#loc").val();
	let whocanapp=$("#whocanapp").val();
	let skills=$("#skill").val();
	let salary=$("#Salary").val();
	let vacancy=$("#vacancy").val();
	let appliedby=$("#app-by").val();
	var data={};
	data["role_name"]=name;
	data["location"]=location;
	data["who_can_apply"]=whocanapp;
	data["skills_req"]=skills;
	data["salary"]=salary;
	data["vacancy"]=vacancy;
	data["apply_by"]=appliedby;
	$.ajax({
		method:"POST",
		url:"http//127.0.0.1:8000/api/addjob/",
		type:'application/json',
		data:data,
		success:function(response){
			console.log(response);
			window.localStorage['token']=response['token'];
			window.location.href="/viewjob/";
			 alert(response.alert);
		}
	});
	});
});