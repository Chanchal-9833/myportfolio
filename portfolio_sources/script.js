var identity=document.querySelector("h3")
var btn=document.querySelector("#add")

var val=0
add.addEventListener("click",function(){
    if (val==0){
        identity.innerHTML="Friend"
        identity.style.color="green"
        add.innerHTML="Remove"
        
        val=1
    }
    else{
        identity.innerHTML="Stranger"
        identity.style.color="red"
        add.innerHTML="Add Friend"
        val=0
    }
})