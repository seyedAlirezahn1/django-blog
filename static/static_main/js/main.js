const measseg = document.getElementById("toast");
const btn = document.getElementById("nav_button");

btn.addEventListener("click",()=>{
  measseg.classList.add("show");
  setTimeout(() => {
    measseg.classList.remove("show");
  }, 3000);
})