var elmnt = document.getElementsByClassName('pup');
var opa =1
var pup = document.getElementsByClassName('pup');
$(window).scroll(function(){
    
    var y = $('.grad2').offset().top;
    
    for (var i = 0; i < pup.length; i++) {
    
    var ps = pup[i].scrollHeight;
    
if (pup[i].offsetTop < y+(ps/15000)){
    var  temp = window.getComputedStyle(pup[i]).getPropertyValue("opacity");

$(pup[i]).css("opacity", temp - .08 );

if (temp < 0) {temp = 0}

  }

  else if (pup[i].offsetTop > y+(ps/15000)) {
    var  temp = window.getComputedStyle(pup[i]).getPropertyValue("opacity");
    if (temp < 1) {
    

    $(pup[i]).css("opacity", temp - (-.08 )); 
    
    }

    }

}
  
});