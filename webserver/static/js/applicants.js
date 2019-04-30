$(document).ready(function() {
	var a = $('#applicants');
	$.ajax({
		method: 'GET',
		url: "http://127.0.0.1:8000/api/viewposting/?",
		type: "application/json",
		success: function(response) {
			// console.log(response);
				a.append(`
						<div class="card">
						<div class="row">
						<div class="col-md-10">
						<div class="card-body">
						<h4 class="card-title" >${applicants.stu_name}</h4>
						<h4 class="card-title" >${applicants.degree_name}</h4>
						
						


						</div></div></div></div>
						
							`)
			}
		beforeSend: function(xhr) {
			xhr.setRequestHeader('Authorization', "Token " + window.localStorage['token']);
		}
	});