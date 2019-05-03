$(document).ready(function() {
	var a = $('#vi');
	$.ajax({
		method: 'GET',
		url: "http://127.0.0.1:8000/api/viewposting/",
		type: "application/json",
		beforeSend: function(xhr) {
			xhr.setRequestHeader('Authorization', "Token " + window.localStorage['token']);
		},
		success: function(response) {
			console.log(response);
			a.append(`<div class="card">
						<div class="row">
							<div class="col-md-10">
								<div class="card-body">
									<h4 class="card-title" >${response.company.organ_name}</h4>
									<h4 class="card-title" >${response.role_name}</h4>
									<h4 class="card-title" >${response.location}</h4>
									<h4 class="card-title" >${response.skills_req}</h4>
									<h4 class="card-title" >${response.salary}</h4>
									<h4 class="card-title" >${response.apply_by}</h4>
									<h4 class="card-title" >${response.vacancy}</h4>
								</div>
							</div>
						</div>
					</div>`)
		}
	});
});