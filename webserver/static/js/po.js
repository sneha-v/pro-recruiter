$(document).ready(function(){
	var postingsdiv = $("#postings");
	$.ajax({
		method: 'GET',
		url: "http://127.0.0.1:8000/api/allposting/",
		success: function(response) {
			console.log(response);

			for (let posting of response) {
				console.log(posting);
				postingsdiv.append(`
						<div class="card">
						<div class="row">
						<div class="col-md-9">
						<div class="card-body">
						<h4 class="card-title" >${posting.role_name}</h4>
						<h5 class="card-title" >${posting.company.organ_name}</h5>
						<h6 class="card-title" >Remuneration: ₹ ${posting.salary}</h6>
						</div></div>
						<div class="col-md-3">
						<br />
													<h6 class="card-title" >Location: ${posting.location}</h6>
													<div class="text-center">
            										<input type="submit" class = "btn btn-success" value="Apply" style="text-align: center;">
          											</div>

						</div>
						
						</div>
						</div>
						<br />
							`)
			}
		},
		beforeSend: function(xhr) {
			xhr.setRequestHeader('Authorization', "Token " + window.localStorage['token']);
		}
	});
});