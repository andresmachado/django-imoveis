$(document).ready(function(){
  console.log('loaded')
	
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
})