//--------------------- header transform
var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.getElementById("navbar_alpha").style.top = "0";
  } else {
    document.getElementById("navbar_alpha").style.top = "-4em";
  }
  prevScrollpos = currentScrollPos;
}
//--------------------- -----------------
