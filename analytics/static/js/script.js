/*
====================================
LifeOS v1.0
Main JavaScript
====================================
*/


// ====================================
// Show Today's Date
// ====================================

function showDate() {

    const element = document.getElementById("todayDate");

    if (element) {

        const today = new Date();

        element.innerHTML = today.toDateString();

    }

}



// ====================================
// Confirm before leaving page
// ====================================

let formChanged = false;

document.addEventListener("DOMContentLoaded", () => {

    const form = document.querySelector("form");

    if (form) {

        form.addEventListener("change", () => {

            formChanged = true;

        });

    }

});


window.addEventListener("beforeunload", function (e) {

    if (formChanged) {

        e.preventDefault();

        e.returnValue = "";

    }

});



// ====================================
// Disable warning after submit
// ====================================

document.addEventListener("DOMContentLoaded", () => {

    const form = document.querySelector("form");

    if (form) {

        form.addEventListener("submit", () => {

            formChanged = false;

        });

    }

});



// ====================================
// Numbers cannot be negative
// ====================================

document.addEventListener("DOMContentLoaded", () => {

    const inputs = document.querySelectorAll("input[type='number']");

    inputs.forEach(input => {

        input.addEventListener("input", () => {

            if (input.value < 0)

                input.value = 0;

        });

    });

});



// ====================================
// Auto Calculate Total Study
// ====================================

function calculateStudy() {

    const semester =
        parseFloat(document.querySelector("[name='semester_study']")?.value) || 0;

    const project =
        parseFloat(document.querySelector("[name='project']")?.value) || 0;

    const leetcode =
        parseFloat(document.querySelector("[name='leetcode']")?.value) || 0;

    const selfstudy =
        parseFloat(document.querySelector("[name='self_study']")?.value) || 0;

    const total = semester + project + leetcode + selfstudy;

    const label = document.getElementById("totalStudy");

    if (label)

        label.innerHTML = total.toFixed(2) + " hrs";

}



document.addEventListener("input", calculateStudy);



// ====================================
// Water Color Indicator
// ====================================

document.addEventListener("DOMContentLoaded", () => {

    const water = document.querySelector("[name='water']");

    if (!water) return;

    water.addEventListener("input", () => {

        let value = parseFloat(water.value);

        water.classList.remove(
            "border-danger",
            "border-warning",
            "border-success"
        );

        if (value < 2)

            water.classList.add("border-danger");

        else if (value < 3)

            water.classList.add("border-warning");

        else

            water.classList.add("border-success");

    });

});



// ====================================
// Mobile Usage Indicator
// ====================================

document.addEventListener("DOMContentLoaded", () => {

    const mobile = document.querySelector("[name='mobile']");

    if (!mobile) return;

    mobile.addEventListener("input", () => {

        let value = parseFloat(mobile.value);

        mobile.classList.remove(
            "border-success",
            "border-warning",
            "border-danger"
        );

        if (value <= 2)

            mobile.classList.add("border-success");

        else if (value <= 4)

            mobile.classList.add("border-warning");

        else

            mobile.classList.add("border-danger");

    });

});



// ====================================
// Highlight Active Sidebar Link
// ====================================

document.addEventListener("DOMContentLoaded", () => {

    // Select all anchor tags inside the fixed sidebar div
    const links = document.querySelectorAll("div[style*='position:fixed'] a");

    links.forEach(link => {

        // Compare pathname only (ignores trailing slash differences)
        if (link.pathname === window.location.pathname) {

            link.classList.remove("btn-dark");
            link.classList.add("btn-primary");

        }

    });

});



// ====================================
// Smooth Scroll
// ====================================

document.documentElement.style.scrollBehavior = "smooth";



// ====================================
// Bootstrap Tooltips
// ====================================

document.addEventListener("DOMContentLoaded", () => {

    const tooltipTriggerList = [].slice.call(

        document.querySelectorAll('[data-bs-toggle="tooltip"]')

    );

    tooltipTriggerList.map(function (tooltipTriggerEl) {

        return new bootstrap.Tooltip(tooltipTriggerEl);

    });

});



console.log("LifeOS Loaded Successfully");