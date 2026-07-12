// ==========================
// LOADING ANIMATION
// ==========================

window.addEventListener("load", () => {

    document.body.style.opacity = "1";

});

// ==========================
// SEARCH PRODUCT
// ==========================

const searchInput = document.querySelector(".search-box input");

if(searchInput){

    searchInput.addEventListener("keyup", function(){

        const keyword = this.value.toLowerCase();

        const cards = document.querySelectorAll(".product-card");

        cards.forEach(card=>{

            const title = card.querySelector("h4").innerText.toLowerCase();

            if(title.includes(keyword)){

                card.parentElement.style.display="block";

            }else{

                card.parentElement.style.display="none";

            }

        });

    });

}

// ==========================
// BUTTON CLICK EFFECT
// ==========================

const buttons=document.querySelectorAll(".btn");

buttons.forEach(btn=>{

    btn.addEventListener("click",()=>{

        btn.style.transform="scale(.96)";

        setTimeout(()=>{

            btn.style.transform="scale(1)";

        },150);

    });

});

// ==========================
// ICON HOVER
// ==========================

const icons=document.querySelectorAll(".icon-btn");

icons.forEach(icon=>{

    icon.addEventListener("mouseenter",()=>{

        icon.style.transform="rotate(10deg)";

    });

    icon.addEventListener("mouseleave",()=>{

        icon.style.transform="rotate(0deg)";

    });

});

// ==========================
// SMOOTH SCROLL
// ==========================

window.scroll({

    behavior:"smooth"

});