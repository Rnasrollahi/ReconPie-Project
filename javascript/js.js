const header=document.querySelector("#span");
const caption=document.querySelector("#caption");
const b=document.querySelector("body");
header.addEventListener("click",add);
function add(){
    if(caption.style.opacity=="0"){
        caption.style.opacity="1";

    }
    else{
        caption.style.opacity="0";

    }
    
}
