function myFunction() {

    var membersList = document.getElementById("members");


    console.log(membersList.style.maxHeight);
    if (membersList.style.maxHeight === '0px') {
        membersList.style.maxHeight = '1000px';
        
    } else {
        membersList.style.maxHeight = '0px';
}
}
document.getElementById('membersButton').onclick = myFunction;