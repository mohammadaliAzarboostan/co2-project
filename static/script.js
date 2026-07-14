let chart1;
let chart2;

// ===== Prediction =====
function predictCO2() {

    let data = {
        engine: document.getElementById("engine").value,
        cylandr: document.getElementById("cylandr").value,
        fuelcity: document.getElementById("fuelcity").value,
        fuelwy: document.getElementById("fuelwy").value,
        fuelcomb: document.getElementById("fuelcomb").value
    };

    if (!data.engine || !data.cylandr) {
        alert("Please fill required fields");
        return;
    }

    document.getElementById("loader").style.display = "block";
    document.getElementById("result").innerText = "--";

    fetch("/predict", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(res => {

        document.getElementById("loader").style.display = "none";
        document.getElementById("result").innerText = res.co2;

        updateCharts(data, res.co2);
    });
}

// ===== Charts =====
function updateCharts(data, co2) {

    // Chart 1 (Engine vs CO2)
    const ctx1 = document.getElementById("chart1");

    if (chart1) chart1.destroy();

    chart1 = new Chart(ctx1, {
        type: "bar",
        data: {
            labels: ["Engine", "CO2"],
            datasets: [{
                label: "Relation",
                data: [data.engine, co2],
                backgroundColor: ["#38bdf8", "#000000"]
            }]
        }
    });

    // Chart 2 (Fuel breakdown)
    const ctx2 = document.getElementById("chart2");

    if (chart2) chart2.destroy();

    chart2 = new Chart(ctx2, {
        type: "doughnut",
        data: {
            labels: ["City", "Highway", "Combined"],
            datasets: [{
                data: [data.fuelcity, data.fuelwy, data.fuelcomb],
                backgroundColor: ["#ef4444", "#facc15", "#a855f7"]
            }]
        }
    });
}

// ===== Theme =====
function toggleTheme() {
    let body = document.body;
    body.dataset.theme = body.dataset.theme === "light" ? "dark" : "light";
}