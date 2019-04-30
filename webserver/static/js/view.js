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
			// console.log(response);

			// for(let vi of response) {
			// console.log(vi.company);

			a.append(`
						<div class="card">
						<div class="row">
						<div class="col-md-10">
						<div class="card-body">
						<h4 class="card-title" >${vi.company.organ_name}</h4>
						<h4 class="card-title" >${vi.role_name}</h4>
						<h4 class="card-title" >${vi.location}</h4>
						<h4 class="card-title" >${vi.skills_req}</h4>
						<h4 class="card-title" >${vi.salary}</h4>
						<h4 class="card-title" >${vi.apply_by}</h4>
						<h4 class="card-title" >${vi.vacancy}</h4>
						</div></div>
						
						</div>
						</div>
							`)
		}
	});
});