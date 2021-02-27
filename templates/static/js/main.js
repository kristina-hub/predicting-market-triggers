$(document).ready(()=>{
	function handleErrors(response) {
		$('.spinner').toggleClass('d-none');
	    if (!response.ok) {
	        throw Error(response.statusText);
	    }
	    return response;
	}
	function fetchResult(opt , status){
		switch(opt){
		case 0:
			return `<li class="list-group-item d-flex justify-content-between bg-dark">
		    <span><img src="/static/assets/GN.png" style="height:30px;width:50px">
		    <span class="ml-1"> Global News feeds indicates ${status ? 'positive' : 'negative' }</span></span>
		    <span class="badge badge-primary badge-pill">100 news feeds</span>
		  </li>`
			break;
		case 1:
			return `<li class="list-group-item d-flex justify-content-between align-items-center bg-dark">
		    <span><i class="fab fa-twitter-square fa-2x mr-1"></i> 
		    <span class="ml-1">Twitter tweets indicates ${status ? 'positive' : 'negative' }</span></span>
		    <span class="badge badge-primary badge-pill">1000 tweets</span>
		  </li>`
			break;
		case 2:
			  return `<li class="list-group-item d-flex justify-content-between align-items-center bg-dark">
			    <span><i class="fab fa-facebook-square fa-2x mr-1"></i></i>
			    <span class="ml-1"> Facebook news indicates  ${status ? 'positive' : 'negative' }.</span></span>
			    <span class="badge badge-primary badge-pill">200 feeds</span>
			  </li>`
			break;
		case 3:  
		    return `<li class="list-group-item d-flex justify-content-between align-items-center bg-dark">
		    <span><i class="fab fa-reddit-square fa-2x  mr-1"></i>
		    <span class="ml-1"> Reddit news indicates ${status ? 'positive' : 'negative' }.</span></span>
		    <span class="badge badge-primary badge-pill">200 feeds</span>
		  </li>`
			break;
		}
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
		    	let stock = $('#stock-search').val()
		    	$('#stock-search').val('');
		    	let res = data.status;
		    	let isPositive = res.reduce((a, b) => a + b, 0);
		    	let template = ``;
		    	res.forEach((data , i)=>{
		    		template += fetchResult(i, data);
		    	})
		    	isPositive = isPositive/res.length
		    	let status =`<div class="alert alert-success" role="alert">
							  	Stock ${stock} : Market triggers indicate that you should buy ${!isPositive ? 'not' : ''} this stock
							  	</div> ${template}`
		    	$('.show-status').html(status);
		    })
		    .catch((error) =>{  
		    	$('.spinner').toggleClass('d-none');
		    	let status =`<div class="alert alert-error" role="alert">
				  	Something went wrong ! Please try again
				  	</div>`
		    		$('.show-status').html(status);
		    	console.log(error) 
		    });
	})
});