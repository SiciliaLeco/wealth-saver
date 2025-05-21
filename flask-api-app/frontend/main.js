const API_BASE = "http://127.0.0.1:5000";

document.getElementById('transaction-form').onsubmit = async function(e) {
    e.preventDefault();
    const form = e.target;
    const data = {
        date: form.date.value,
        cost: parseFloat(form.cost.value),
        type: form.type.value
    };
    const res = await fetch(`${API_BASE}/transactions`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    });
    const msg = await res.json();
    document.getElementById('transaction-msg').textContent = msg.message || "Error";
    form.reset();
};

document.getElementById('debt-form').onsubmit = async function(e) {
    e.preventDefault();
    const form = e.target;
    const data = {
        amount: parseFloat(form.amount.value),
        description: form.description.value,
        date: form.date.value
    };
    const res = await fetch(`${API_BASE}/debts`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    });
    const msg = await res.json();
    document.getElementById('debt-msg').textContent = msg.message || "Error";
    form.reset();
};

document.getElementById('suggest-goal-btn').onclick = async function() {
    const res = await fetch(`${API_BASE}/suggest-goal`);
    const data = await res.json();
    document.getElementById('suggested-goal').textContent =
        "Suggested Saving Goal: $" + (data.suggested_saving_goal || 0).toFixed(2);
};