$(document).ready(function() {
	$('#login-btn').on('click', function() {
		let username = $("#login-username").val();
		let password = $("#login-password").val();
		var data = {};
		data["username"] = username;
		data["password"] = password;
		$.ajax({
			method: "POST",
			url: "http://127.0.0.1:8000/api-token-auth/",
			type: 'application/json',
			data: data,
			success: function(response) {
				console.log(response);

				window.localStorage['token'] = response['token'];


				$.ajax({
					method: "POST",
					url: "http://127.0.0.1:8000/api/tokenauth/",
					data: response,
					type: 'application/json',
					success: function(response) {
						if (response.choice == "RECRUITER") {
							window.location.href = "/addjobs/";
						} else if (response.choice == "STUDENT") {
							window.location.href = "/sdashboard/";

						}
					}

				});

			}
		});
	});
});
$('#ss-btn').on('click', function() {
	let firstname = $("#ss-fname").val();
	let lastname = $("#ss-lname").val();
	let username = $("#ss-username").val();
	let email = $("#ss-email").val();
	let password = $("#ss-password").val();
	var data = {};
	data["first_name"] = firstname;
	data["last_name"] = lastname;
	data["username"] = username;
	data["password"] = password;
	data["email"] = email;
	data["user_type"] = 2;
	console.log(data);
	$.ajax({
		method: "POST",
		url: "http://127.0.0.1:8000/api/register/",
		type: 'application/json',
		data: data,
		success: function(response) {
			alert(response.alert);
			$("#SSignupModal").modal('hide');
			$("#LoginModal").modal('show');
		}
	});
});

$('#rs-btn').on('click', function() {
	let firstname = $("#rs-fname").val();
	let lastname = $("#rs-lname").val();
	let username = $("#rs-username").val();
	let email = $("#rs-email").val();
	let organisation = $("#rs-org").val();
	let about = $("#rs-ab").val();
	let password = $("#rs-password").val();
	var data = {};
	data["first_name"] = firstname;
	data["last_name"] = lastname;
	data["username"] = username;
	data["password"] = password;
	data["email"] = email;
	data["user_type"] = 1;
	console.log(data);
	$.ajax({
		method: "POST",
		url: "http://127.0.0.1:8000/api/register/",
		type: 'application/json',
		data: data,
		success: function(response) {
			alert(response.alert);
			$("#RSignupModal").modal('hide');
			$("#LoginModal").modal('show');


		}
	});
});