// Add event listener for the login form submission
document.getElementById("loginForm").addEventListener("submit", function (e) {
  e.preventDefault(); // Prevent the default form submission

  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  // Show the loading overlay
  const loadingOverlay = document.getElementById("loadingOverlay");
  loadingOverlay.style.display = "flex";

  // Simulate a short delay for redirection (e.g., for server response)
  setTimeout(() => {
    // Check credentials
    if (username === "rkcomputers@gmail.com" && password === "rk123") {
      // Redirect to the specified URL
      window.location.href = "http://127.0.0.1:5000";
    } else {
      // Hide the loading overlay
      loadingOverlay.style.display = "none";

      // Show an alert and reset the form
      alert("Wrong username or password! Please contact the developer if you forgot your password.");
      document.getElementById("username").value = "";
      document.getElementById("password").value = "";
    }
  }, 2000); // Adjust delay as needed
});

const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");

sign_up_btn.addEventListener('click', () =>{
    container.classList.add("sign-up-mode");
});

sign_in_btn.addEventListener('click', () =>{
    container.classList.remove("sign-up-mode");
});