$(document).ready(()=>{
	function handleErrors(response) {
		$('.spinner').toggleClass('d-none');
	    if (!response.ok) {
	        throw Error(response.statusText);
	    }
	    return response;
	}
	
	$('#submit').on('click', ()=>{
		$('.show-status').html('');
		var $inputs = $('#searchForm :input');
	    var data = {};
	    $inputs.each(function() {
	    	if(this.name){
	    		data[this.name] = $(this).val();
	    	}
	    });
	    if(!data['stock']){
	    	return;
	    }
		$('.spinner').toggleClass('d-none');
		fetch("/search", {
		    method: 'POST', // *GET, POST, PUT, DELETE, etc.
		    mode: 'cors', // no-cors, *cors, same-origin
		    cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
		    credentials: 'same-origin', // include, *same-origin, omit
		    headers: {
		      'Content-Type': 'application/json'
		      // 'Content-Type': 'application/x-www-form-urlencoded',
		    },
		    redirect: 'follow', // manual, *follow, error
		    referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
		    body: JSON.stringify(data) // body data type must match "Content-Type" header
		  }).then(handleErrors)
		  	.then(response=>{ return response.json(); })
		    .then((data) => {
		    	console.log("ok", data);
		    	$('#stock-search').val('');
		    	let res = data.status;
		    	let isPositive = res.reduce((a, b) => a + b, 0)
		    	isPositive = isPositive/res.length
		    	let status = "";
		    	if(isPositive){
		    		status = `<div class="alert alert-success" role="alert">
							  	Market triggers indicate that you should buy this stock
								</div>`
		    	} else {
		    		status = `<div class="alert alert-danger" role="alert">
							  Market triggers indicate that you should not buy this stock
							</div>`
		    	}
		    	$('.show-status').html(status);
		    })
		    .catch((error) =>{  
		    	$('.spinner').toggleClass('d-none');
		    	console.log(error) 
		    });
	})
});