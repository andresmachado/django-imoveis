$(document).ready(function(){
  console.log('loaded')
	
  // CSRF headings for Django AJAX requests
  $(function() {


    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

});
  ////////////////////////////////////////////////////////
  // <--- End of Django header for AJAX requests ---- >//
  ///////////////////////////////////////////////////////
  
  // Functions for Django delete object

  var deleteObject = function (property_id) {
    // alert("Delete object id " + property_id + " is working!");
    if (confirm('Tem certeza que deseja excluir este anúncio?')==true){
      $.ajax({
        url: 'imoveis/excluir/',
        type: 'DELETE',
        data: { 'property_id': property_id },
        success: function(json) {
          $('#property-'+property_id).hide();
          alert(json['msg']);
        },
        error: function(xhr, errmsg, err) {
          // Show an error
          alert("Não foi possível concluir sua requisição, entre em contato com o administrador do sistema.")
          console.log(xhr.status + ":" + xhr.responseText);
        }
      });      
    } else {
      return false;
    }
  };

  var getAddress = function(cep){
  	var ApiUrl = "https://viacep.com.br/ws/";
    var docType = "/json/";
    var cep = cep;
    var fullUrl =  ApiUrl + cep + docType;
    
    $.ajax({
    	url: fullUrl,
      method: 'GET',
      success: function (address) {
      	var logradouro = address['logradouro'];
        var bairro = address['bairro'];
        var uf = address['uf'];
        var localidade = address['localidade'];
        
        $('#id_address').val(logradouro);
        $('#id_state').val(uf);
        $('#id_district').val(bairro);
        $('#id_city').val(localidade);
      },
      error: function () {
        alert("Oops, verifique seu CEP e tente novamente.")
      }
    })
  };
  
  $("#id_cep").on('blur', function(){
  	getAddress($(this).val());
  });

  $("#delete-property").on('click', 'a[id^=delete-property-]', function(event) {
    event.preventDefault();
    var property_id = $(this).attr('id').split('-')[2]
    deleteObject(property_id);
  })


})