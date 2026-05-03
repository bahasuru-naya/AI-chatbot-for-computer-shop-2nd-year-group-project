const btn = document.querySelector(".bttn");
const video = document.querySelector(".background-video");
const fa = document.getElementById('play');
const preloader = document.querySelector(".preloader");
const darkMode = document.getElementById('dark');
document.getElementById('dark').checked = JSON.parse(localStorage.getItem("sharedBool2"));
changemode();


btn.addEventListener("click", () => {
    if (btn.classList.contains("pause")) {
        btn.classList.remove("pause");
        video.play();
        fa.classList.add("fa-pause");
        fa.classList.remove("fa-play");
    } else {
        btn.classList.add("pause");
        video.pause();
        fa.classList.remove("fa-pause");
        fa.classList.add("fa-play");
    }
});

//shared variable
const nav = document.getElementById('nav-toggle');
nav.addEventListener("click", () => {

    let boolVar = document.getElementById('nav-toggle').checked;
    localStorage.setItem("sharedBool1", JSON.stringify(boolVar));


});

//loading
window.addEventListener("load", () => {
    
    //turn dark mode on default
    document.getElementById('dark').checked = JSON.parse(localStorage.getItem("sharedBool2"));   
    changemode();
    document.getElementById('nav-toggle').checked = JSON.parse(localStorage.getItem("sharedBool1"));
    menuCheckbox();

    preloader.style.animation = "fade-out 0.5s cubic-bezier(0.550, 0.085, 0.680, 0.530) 0.75s both";
    preloader.addEventListener('animationend', () => {
        // Once the animation ends, hide the preloader
        preloader.style.display = 'none'; // Alternatively, you can remove the element with preloader.remove();
    });

});




function navigateToPage() {
    // Specify the URL you want to navigate to
    var url = "./chatbot.html";
    // Navigate to the specified URL
    window.location.href = url;
}


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
        var vidElement = document.querySelector('#homevid');

        // Change the src attribute
        imgElement.src = './images/settings-64.png'; // Replace with your new image path
        vidElement.src = './vid/background-video.mp4'; // Replace with your new video path
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
        var vidElement = document.querySelector('#homevid');

        // Change the src attribute
        imgElement.src = './images/settings-64 - dark.png'; // Replace with your new image path
        vidElement.src = './vid/background-video-light.mp4'; // Replace with your new video path
        loader.src = './images/preloader-light.svg';
    }
}


darkMode.addEventListener("click", () => {
    let boolVar1 = darkMode.checked;
    localStorage.setItem("sharedBool2", JSON.stringify(boolVar1));
    changemode();

});





