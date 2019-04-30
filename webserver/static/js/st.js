$(document).ready(function() {
	var a = $('#applied');
	$.ajax({
		method: 'GET',
		url: "http://127.0.0.1:8000/api/sdashboard/",
		type: "application/json",
		success: function(response) {
			console.log(response);

			for (let applied of response) {
				console.log(applied.company.company);
				a.append(`
						<div class="card">
						<div class="row">
						<div class="col-md-7">
						<div class="card-body">
						<h4 class="card-title" >${applied.company.company.organ_name}</h4>
						<h5 class="card-title" >${applied.company.role_name}</h5>
						<h6 class="card-title" >Remuneration: ₹ ${applied.company.salary}</h6>
						</div></div>
						<div class="col-md-5">
						<br />
							${getApplicationStatus(applied.status)}
						</div>
						
						</div>
						</div>
							`)
			}
		},
		beforeSend: function(xhr) {
			xhr.setRequestHeader('Authorization', "Token " + window.localStorage['token']);
		}
	});
});

function getApplicationStatus(status) {
	if (status == 'r') {
		return `<button style="float:right" class="btn btn-xs btn-danger">Rejected</button>`
	} else if (status == 'a') {
		return `<button style="float:right" class="btn btn-xs btn-primary">Applied</button>`

	} else if (status == 'c') {
		return `<button style="float:right" class="btn btn-xs btn-warning">Call For Interview</button>`

	} else if (status == 's') {
		return `<button style="float:right" class="btn btn-xs btn-secondary">Shortlisted</button>`

	} else if (status == 'p') {
		return `<button style="float:right" class="btn btn-xs btn-success">Accepted</button>`

	}
}