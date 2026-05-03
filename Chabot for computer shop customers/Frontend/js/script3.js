const preloader = document.querySelector(".preloader");
const darkMode = document.getElementById('dark');
document.getElementById('dark').checked = JSON.parse(localStorage.getItem("sharedBool2"));
changemode();

//shared variable
const nav = document.getElementById('nav-toggle');
nav.addEventListener("click", () => {

    let boolVar = document.getElementById('nav-toggle').checked;
    localStorage.setItem("sharedBool1", JSON.stringify(boolVar));


});

//loading
window.addEventListener("load", () => {
    menuCheckbox();
    document.getElementById('nav-toggle').checked = JSON.parse(localStorage.getItem("sharedBool1"));
    //setTimeout(() => {
    //preloader.style.display = "none";} , 1000);
    preloader.style.animation = "fade-out 0.5s cubic-bezier(0.550, 0.085, 0.680, 0.530) 0.75s both";
    preloader.addEventListener('animationend', () => {
        // Once the animation ends, hide the preloader
        preloader.style.display = 'none'; // Alternatively, you can remove the element with preloader.remove();
    });

});

//menu
function menuCheckbox() {
    if (window.innerWidth < 868) {
        document.getElementById('nav-toggle').checked = true;
    }
}


//remove blur
const removeblur = document.getElementById('dashboard');
removeblur.addEventListener("click", () => {
    if (window.innerWidth < 868) {
        document.getElementById('nav-toggle').checked = true;
    }
});

const btns = document.querySelectorAll(".acc-btn");

// fn
function accordion() {
    // this = the btn | icon & bg changed
    this.classList.toggle("is-open");

    // the acc-content
    const content = this.nextElementSibling;

    // IF open, close | else open
    if (content.style.maxHeight) content.style.maxHeight = null;
    else content.style.maxHeight = content.scrollHeight + "px";
}

// event
btns.forEach((el) => el.addEventListener("click", accordion));


//dark mode
function changemode() {
    if (darkMode.checked) {
        // Define the dark mode colors
        const darkModeColors = {
            '--background': '#BEDAFF',
            '--navbar-dark-primary': '#18283b',
            '--navbar-dark-secondary': '#2c3e50',
            '--navbar-light-primary': '#f5f6fa',
            '--navbar-light-secondary': '#8392a5',
            '--black': '#000000',
            '--white': '#ffffff',
        };

        // Get the root element
        const root = document.documentElement;



        // Change the colors to dark mode
        for (let color in darkModeColors) {
            root.style.setProperty(color, darkModeColors[color]);

        }

        // Select the img element
        var imgElement = document.querySelector('#nav-footer-avatar img');
        var loader = document.querySelector('#load');

        // Change the src attribute
        imgElement.src = './images/settings-64.png'; // Replace with your new image path

        loader.src = './images/preloader.svg';
    }
    else {
        // Define the light mode colors
        const lightModeColors = {
            '--background': '#2C4970',
            '--navbar-dark-primary': '#dbe4f0',
            '--navbar-dark-secondary': '#8392a5',
            '--navbar-light-primary': '#18283b',
            '--navbar-light-secondary': '#2c3e50',
            '--black': '#ffffff',
            '--white': '#000000',
        };

        // Get the root element
        const root = document.documentElement;


        // Change the colors to light mode
        for (let color in lightModeColors) {
            root.style.setProperty(color, lightModeColors[color]);

        }
        // Select the img element
        var imgElement = document.querySelector('#nav-footer-avatar img');
        var loader = document.querySelector('#load');

        // Change the src attribute
        imgElement.src = './images/settings-64 - dark.png'; // Replace with your new image path
        loader.src = './images/preloader-light.svg';
    }
}

darkMode.addEventListener("click", () => {
    let boolVar1 = darkMode.checked;
    localStorage.setItem("sharedBool2", JSON.stringify(boolVar1));
    changemode();

});



function scrollToBottom() {
    var element = document.getElementById("messages");
    element.scrollTo({
        top: element.scrollHeight,
        behavior: 'smooth' // Add smooth behavior
    });
}

