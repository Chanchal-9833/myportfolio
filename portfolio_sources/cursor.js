var elem=document.querySelectorAll(".row")
var elemImage=document.querySelector(".row img")

elem.forEach(function(val){
    
    val.addEventListener("mouseenter",function(){
        val.childNodes[1].style.opacity=1
       
    });
    val.addEventListener("mousemove",function(dets){
        val.childNodes[1].style.left=dets.x+"px"
      
    });
    val.addEventListener("mouseleave",function(){
       val.childNodes[1].style.opacity=0
   });  
    
    
})
