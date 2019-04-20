$(document).ready(function(){
		console.log("in");

	$('#login-btn').on('click',function(){
	console.log("Login");
	let username=$("#login-username").val();
	let password=$("#login-password").val();
	var data={};
	data["username"]=username;
	data["password"]=password;
	$.ajax({
		method:"POST",
		url:"http://127.0.0.1:8000/api-token-auth/",
		type:'application/json',
		data:data,
		success:function(response){
			console.log(response);
			window.localStorage['token']=response['token'];
			window.location.href="/sdashboard/";
		}
	});
	});
 $('#ss-btn').on('click',function(){
 	let firstname=$("ss-fname").val();
 	let lastname=$("ss-lastname").val();
	let username=$("#ss-username").val();
	let email=$("").val();
	let password=$("#ss-password").val();
	let user_type;
	var data={};
	data["first_name"]=firstname;
	data["last_name"]=lastname;
	 data["username"]=username;
	data["password"]=password;
	data["email"]=email;
	data["user_type"]=2;
	console.log(data);
	 $.ajax({
		 method:"POST",
		url:"http://127.0.0.1:8000/api/register/",
		type:'application/json',
		 data:data,
		 success:function(response){
			 console.log(response);
			 window.localStorage['token']=response['token'];
			 window.location.href="/sdashboard/";
		 }
	 });
	 });

});