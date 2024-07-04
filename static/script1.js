
let menuicon= document.querySelector(".menu-icon")
let sidebar= document.querySelector(".side-bar")
let largecontainer= document.querySelector(".container")

menuicon.onclick= function(){
    sidebar.classList.toggle("small-sidebar")
    largecontainer.classList.toggle("large-container")
}
document.addEventListener('DOMContentLoaded',function(){
    console.log('hi');
    var form=document.getElementsByClassName('search_form');
    var url=document.getElementsByClassName('search');
    form.addEventListener('submit',function(event){
        console.log('hi');
        event.preventDefault();
        var u=url.value;
        form.action=u;
        //window.alert(document.getElementsByClassName('search').value);
        form.submit();
    }
)
})
console.log('hi');
